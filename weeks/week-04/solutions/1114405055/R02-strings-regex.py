# R02. 正則表達式：搜尋、替換、旗標（2.4-2.8）
# 主題：re.compile / findall / finditer / sub / IGNORECASE / 非貪婪 / DOTALL

import re


def demo_search_and_extract():
    """2.4 匹配與搜尋：match/findall/finditer 差異。"""
    text = "Today is 11/27/2012. PyCon starts 3/13/2013."
    date_pat = re.compile(r"(\d+)/(\d+)/(\d+)")

    print("=== 2.4 匹配和搜尋 ===")
    # findall：一次找所有匹配，回傳 list。
    print("findall ->", date_pat.findall(text))

    # match：只從字串開頭嘗試匹配。
    m = date_pat.match("11/27/2012")
    assert m is not None
    print("match group(0) ->", m.group(0), ", groups ->", m.groups())

    # finditer：逐筆回傳 Match 物件，適合大型文字或需逐筆處理。
    print("finditer (轉成 day/month/year):")
    for item in date_pat.finditer(text):
        month, day, year = item.groups()
        print(f"  {day}/{month}/{year}")


def demo_substitution():
    """2.5 取代與命名群組。"""
    text = "Today is 11/27/2012. PyCon starts 3/13/2013."
    print("\n=== 2.5 搜尋和替換 ===")

    # 位置群組反向引用：\1, \2, \3。
    replaced = re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
    print("positional groups ->", replaced)

    # 命名群組讓樣式更可讀，尤其群組較多時更清楚。
    replaced_named = re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
    print("named groups ->", replaced_named)

    # subn 會多回傳替換次數，常用在報表或驗證流程。
    _, count = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
    print("replacement count ->", count)


def demo_flags_and_greediness():
    """2.6-2.7 忽略大小寫與貪婪/非貪婪。"""
    print("\n=== 2.6 忽略大小寫 ===")
    s = "UPPER PYTHON, lower python, Mixed Python"
    print("IGNORECASE findall ->", re.findall("python", s, flags=re.IGNORECASE))

    print("\n=== 2.7 貪婪 vs 非貪婪 ===")
    text2 = 'Computer says "no." Phone says "yes."'
    greedy = re.compile(r'"(.*)"').findall(text2)
    nongreedy = re.compile(r'"(.*?)"').findall(text2)
    print("greedy ->", greedy)
    print("non-greedy ->", nongreedy)


def demo_dotall():
    """2.8 跨行匹配。"""
    code = "/* this is a\nmultiline comment */"
    print("\n=== 2.8 DOTALL 跨行匹配 ===")
    # DOTALL 讓 . 可以匹配換行字元，否則預設不會跨行。
    result = re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code)
    print(result)


if __name__ == "__main__":
    demo_search_and_extract()
    demo_substitution()
    demo_flags_and_greediness()
    demo_dotall()
