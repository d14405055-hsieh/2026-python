# R03. 字串清理、對齊、拼接與格式化（2.11-2.16）
# 主題：strip / ljust/rjust/center / join / format / format_map / textwrap

import textwrap


def demo_strip():
    """2.11 清理頭尾字元。"""
    print("=== 2.11 清理字元 ===")
    raw = "  hello world \n"

    # strip() 預設移除頭尾空白字元（空格、\n、\t 等）。
    print("strip ->", repr(raw.strip()))
    print("lstrip ->", repr(raw.lstrip()))
    print("rstrip ->", repr(raw.rstrip()))

    # 傳入參數時，表示「要移除的字元集合」，不是完整字串片段。
    print("custom strip '-=' ->", repr("-----hello=====".strip("-=")))


def demo_alignment():
    """2.13 對齊與寬度控制。"""
    print("\n=== 2.13 字串對齊 ===")
    text = "Hello World"
    print("ljust(20) ->", repr(text.ljust(20)))
    print("rjust(20) ->", repr(text.rjust(20)))
    print("center(20, '*') ->", repr(text.center(20, "*")))

    # format 規格同時可用在字串與數字。
    print("format(text, '^20') ->", repr(format(text, "^20")))
    print("format(1.2345, '>10.2f') ->", repr(format(1.2345, ">10.2f")))


def demo_join_and_format():
    """2.14-2.15 拼接與插值。"""
    print("\n=== 2.14 合併拼接 ===")
    parts = ["Is", "Chicago", "Not", "Chicago?"]
    print("' '.join(parts) ->", " ".join(parts))
    print("','.join(parts) ->", ",".join(parts))

    # join 只能接收字串序列，非字串元素需先轉型。
    data = ["ACME", 50, 91.1]
    print("join after str conversion ->", ",".join(str(item) for item in data))

    print("\n=== 2.15 插入變量 ===")
    name, n = "Guido", 37
    template = "{name} has {n} messages."
    print("format ->", template.format(name=name, n=n))
    print("format_map(vars()) ->", template.format_map(vars()))
    print("f-string ->", f"{name} has {n} messages.")


def demo_textwrap():
    """2.16 指定列寬輸出。"""
    print("\n=== 2.16 textwrap 填充文本 ===")
    long_s = (
        "Look into my eyes, look into my eyes, the eyes, "
        "not around the eyes, look into my eyes, you're under."
    )
    print(textwrap.fill(long_s, 40))
    print("\nwith initial indent:")
    print(textwrap.fill(long_s, 40, initial_indent="    "))
    print("\nwith hanging indent:")
    print(textwrap.fill(long_s, 40, subsequent_indent="    "))


if __name__ == "__main__":
    demo_strip()
    demo_alignment()
    demo_join_and_format()
    demo_textwrap()
