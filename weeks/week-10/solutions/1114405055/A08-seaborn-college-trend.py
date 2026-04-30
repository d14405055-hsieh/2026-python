# A08. 用 seaborn 畫 109~114 學年各學院生源分析圖
# Bloom: Apply — 把 A07 的統計成果交給視覺化套件
#
# 需要：pip install seaborn matplotlib pandas
#
# 用到的 I/O 技巧延續 A07：
#   5.7  zipfile 不解壓讀 CSV
#   5.1  utf-8-sig 去 BOM
#   5.6  io.StringIO → csv
#   5.11 pathlib
#   5.5  open('x') 不覆蓋輸出檔

import csv
import io
import platform
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# ── 中文字型：依平台挑一個有的 ─────────────────────────
# matplotlib 在 macOS 預設抓不到 PingFang TC，用系統內建的 Heiti TC / Arial Unicode MS
_CJK_FONTS = {
    "Darwin":  ["Heiti TC", "Arial Unicode MS", "PingFang TC"],
    "Windows": ["Microsoft JhengHei", "Microsoft YaHei"],
    "Linux":   ["Noto Sans CJK TC", "WenQuanYi Zen Hei"],
}.get(platform.system(), ["sans-serif"])


def _apply_cjk_font():
    """sns.set_theme 會重設 rcParams，需要在它之後再套一次。"""
    plt.rcParams["font.sans-serif"] = _CJK_FONTS + plt.rcParams["font.sans-serif"]
    # 明確設定首選中文字型為第一個 CJK 字型（若可用）
    try:
        # 嘗試加入系統 Noto 字型檔，並使用其 family 名稱
        from matplotlib import font_manager
        font_path = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
        if Path(font_path).exists():
            font_manager.fontManager.addfont(font_path)
            plt.rcParams["font.family"] = _CJK_FONTS[0]
        else:
            plt.rcParams["font.family"] = _CJK_FONTS[0]
    except Exception:
        plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.unicode_minus"] = False


_apply_cjk_font()

# 如果系統有 Noto CJK 的 font 檔，建立一個 FontProperties 供個別文字使用
from matplotlib.font_manager import FontProperties
_NOTO_PATH = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
NotoFont = FontProperties(fname=_NOTO_PATH) if Path(_NOTO_PATH).exists() else None


def _text_kwargs(size: int = 10, weight: str | None = None):
    kwargs = {"fontsize": size}
    if weight:
        kwargs["fontweight"] = weight
    if NotoFont:
        kwargs["fontproperties"] = NotoFont
    return kwargs


def _smooth_xy(x_values, y_values, points_per_segment: int = 40):
    """用簡單的 Catmull-Rom 內插產生平滑曲線，不依賴 scipy。"""
    x = np.asarray(x_values, dtype=float)
    y = np.asarray(y_values, dtype=float)
    if len(x) < 3:
        return x, y

    xs, ys = [], []
    for index in range(len(x) - 1):
        x0 = x[index - 1] if index > 0 else x[index]
        x1 = x[index]
        x2 = x[index + 1]
        x3 = x[index + 2] if index + 2 < len(x) else x[index + 1]

        y0 = y[index - 1] if index > 0 else y[index]
        y1 = y[index]
        y2 = y[index + 1]
        y3 = y[index + 2] if index + 2 < len(x) else y[index + 1]

        t = np.linspace(0, 1, points_per_segment, endpoint=False)
        t2 = t * t
        t3 = t2 * t
        segment_x = x1 + (x2 - x1) * t
        segment_y = 0.5 * (
            (2 * y1)
            + (-y0 + y2) * t
            + (2 * y0 - 5 * y1 + 4 * y2 - y3) * t2
            + (-y0 + 3 * y1 - 3 * y2 + y3) * t3
        )
        xs.append(segment_x)
        ys.append(segment_y)

    xs.append(np.array([x[-1]]))
    ys.append(np.array([y[-1]]))
    return np.concatenate(xs), np.concatenate(ys)

# ── 系所 → 學院 對照表（NPU 三大學院） ─────────────────
DEPT_TO_COLLEGE = {
    # 人文暨管理學院
    "應用外語系":       "人文暨管理學院",
    "航運管理系":       "人文暨管理學院",
    "行銷與物流管理系": "人文暨管理學院",
    "觀光休閒系":       "人文暨管理學院",
    "資訊管理系":       "人文暨管理學院",
    "餐旅管理系":       "人文暨管理學院",
    # 海洋資源暨工程學院
    "水產養殖系":       "海洋資源暨工程學院",
    "海洋遊憩系":       "海洋資源暨工程學院",
    "食品科學系":       "海洋資源暨工程學院",
    # 電資工程學院
    "資訊工程系":       "電資工程學院",
    "電信工程系":       "電資工程學院",
    "電機工程系":       "電資工程學院",
}

# ── 5.11 定位資料 ─────────────────────────────────────
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到：{ZIP_PATH}"


# ── 5.7 + 5.6 + 5.1 讀 zip 內所有 CSV 成一張 long-form 表 ─
def load_long_frame(zip_path: Path) -> pd.DataFrame:
    records = []
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            if not info.filename.endswith(".csv"):
                continue
            year = info.filename[:3]                     # '109'..'114'
            text = z.read(info).decode("utf-8-sig")      # 去 BOM
            reader = csv.DictReader(io.StringIO(text))   # 當檔讀
            for row in reader:
                dept = row.get("系所名稱", "").strip()
                if not dept:
                    continue
                records.append({
                    "學年": int(year),
                    "學院": DEPT_TO_COLLEGE.get(dept, "其他"),
                    "系所": dept,
                })
    return pd.DataFrame.from_records(records)


df = load_long_frame(ZIP_PATH)
print("總筆數:", len(df))
print(df.head())

# 樞紐：各學年 × 各學院 的人數
pivot = (df.groupby(["學年", "學院"])
           .size()
           .reset_index(name="人數"))
print("\n各學年各學院:")
print(pivot.pivot(index="學年", columns="學院", values="人數"))


# ── seaborn 繪圖 ──────────────────────────────────────
sns.set_theme(style="whitegrid", context="notebook")
_apply_cjk_font()  # 蓋回中文字型

# 白底、學術分析儀表板、4k 輸出基底
fig, axes = plt.subplots(1, 2, figsize=(16, 9), facecolor="white",
                         gridspec_kw={"width_ratios": [1.25, 1]})
for axis in axes:
    axis.set_facecolor("white")
    axis.grid(True, axis="y", linestyle="--", linewidth=0.8, color="#D9DEE7", alpha=0.9)
    axis.grid(False, axis="x")
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)
    axis.spines["left"].set_color("#B7C0CC")
    axis.spines["bottom"].set_color("#B7C0CC")

# 圖 A：折線＋散點 —— 各學院逐年趨勢
palette = {
    "人文暨管理學院": "#2FBF71",   # Emerald Green
    "海洋資源暨工程學院": "#F2B75C", # Soft Amber
    "電資工程學院": "#1F3A5F",     # Deep Navy
}

for college, subset in pivot.groupby("學院"):
    ordered = subset.sort_values("學年")
    smooth_x, smooth_y = _smooth_xy(ordered["學年"].to_numpy(), ordered["人數"].to_numpy())
    axes[0].plot(smooth_x, smooth_y, color=palette.get(college, "#7F8C8D"), linewidth=2.6)
    axes[0].scatter(ordered["學年"], ordered["人數"], s=36,
                    color=palette.get(college, "#7F8C8D"), edgecolor="white", linewidth=0.9,
                    zorder=4, label=college)

axes[0].set_title("109–114 各學院新生人數趨勢", **_text_kwargs(15, "bold"), pad=12)
xticks = sorted(pivot["學年"].unique())
axes[0].set_xticks(xticks)
# 顯示為中文年度標籤，例如 '109學年'，並縮小 x 標籤字型
if NotoFont:
    axes[0].set_xticklabels([f"{y}學年" for y in xticks], fontsize=9, fontproperties=NotoFont)
else:
    axes[0].set_xticklabels([f"{y}學年" for y in xticks], fontsize=9)
axes[0].legend(title="學院", frameon=False,
               bbox_to_anchor=(1.02, 1), loc="upper left", borderaxespad=0,
               prop=NotoFont if NotoFont else None, title_fontsize=9)

# 在每個點上標註人數
for _, r in pivot.iterrows():
    # 若數值接近上緣，往上偏移並加白底以免被其他元素遮蔽
    if NotoFont:
        axes[0].annotate(int(r["人數"]),
                         (r["學年"], r["人數"]),
                         textcoords="offset points", xytext=(0, 10),
                         ha="center", fontsize=7, alpha=0.95,
                         bbox=dict(boxstyle="round,pad=0.15", fc="white", alpha=0.92, lw=0),
                         zorder=5, clip_on=False, fontproperties=NotoFont)
    else:
        axes[0].annotate(int(r["人數"]),
                         (r["學年"], r["人數"]),
                         textcoords="offset points", xytext=(0, 10),
                         ha="center", fontsize=7, alpha=0.95,
                         bbox=dict(boxstyle="round,pad=0.15", fc="white", alpha=0.92, lw=0),
                         zorder=5, clip_on=False)

# 增加 y 軸上限，避免標註或文字壓到刻度（例如 600）
max_y = pivot["人數"].max()
axes[0].set_ylim(0, max_y * 1.15)

# 圖 B：堆疊長條 —— 每年學院占比
pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)
pivot_wide = pivot_wide[["人文暨管理學院", "海洋資源暨工程學院", "電資工程學院"]]
pivot_wide.plot(kind="bar", stacked=True,
                ax=axes[1], color=[palette[c] for c in pivot_wide.columns],
                width=0.68, edgecolor="white", linewidth=0.8)
axes[1].set_title("各學年學院結構（堆疊）", **_text_kwargs(15, "bold"), pad=12)
axes[1].set_ylabel("人數", **_text_kwargs(10))
# 右側版面較窄，改成斜放以避免年份標籤互相重疊
axes[1].tick_params(axis="x", rotation=22, labelsize=8)
# 右側長條圖也使用中文年度標籤並縮小字型
if NotoFont:
    axes[1].set_xticklabels([f"{y}學年" for y in pivot_wide.index], fontsize=8, fontproperties=NotoFont, rotation=22, ha="right")
else:
    axes[1].set_xticklabels([f"{y}學年" for y in pivot_wide.index], fontsize=8, rotation=22, ha="right")
axes[1].legend(title="學院", fontsize=8,
               bbox_to_anchor=(1.02, 1), loc="upper left", borderaxespad=0,
               frameon=False, prop=NotoFont if NotoFont else None, title_fontsize=9)

# 增加堆疊長條的上方空間，避免與標題/圖例重疊
max_stack = pivot_wide.sum(axis=1).max()
axes[1].set_ylim(0, max_stack * 1.12)

fig.suptitle("國立澎湖科技大學  109–114 學年新生生源分析",
             **_text_kwargs(18, "bold"), y=0.985)
if NotoFont:
    fig.text(0.5, 0.955, "Academic analytics · corporate style · ultra-clean layout", ha="center",
             color="#475467", fontsize=10, fontproperties=NotoFont)
else:
    fig.text(0.5, 0.955, "Academic analytics · corporate style · ultra-clean layout", ha="center",
             color="#475467", fontsize=10)
# 留出上方與右側空間給 suptitle 與圖例，並增加子圖間距
fig.tight_layout(rect=[0.02, 0.04, 0.82, 0.93])
fig.subplots_adjust(wspace=0.24)

# 再把右側子圖往右挪一點，保留中間文字區
right_pos = axes[1].get_position()
axes[1].set_position([
    right_pos.x0 + 0.10,
    right_pos.y0,
    right_pos.width - 0.10,
    right_pos.height,
])

# ── 輸出：預設覆蓋舊檔以便快速重繪（如需保留舊檔請自行備份）
OUT = HERE / "A08-college-trend.png"
fig.savefig(OUT, dpi=300, bbox_inches="tight")
print(f"\n圖檔已寫入（覆蓋）：{OUT.name}")

plt.show()

# ── 延伸挑戰 ──────────────────────────────────────────
# 1) 改畫「各系所」熱力圖：sns.heatmap(pivot_by_dept, annot=True, fmt='d')
# 2) 加一張圓餅圖：114 學年學院占比
# 3) 把年度 x 軸改成 '109學年'~'114學年' 字串（需轉型 + set_xticklabels）
