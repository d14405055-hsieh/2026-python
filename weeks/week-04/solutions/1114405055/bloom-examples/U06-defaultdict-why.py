# U6. defaultdict 為何比手動初始化乾淨（1.6）

from collections import defaultdict

pairs = [("a", 1), ("a", 2), ("b", 3), ("a", 4)]

# 手動版：每次都要先檢查 key 是否存在。
normal_dict = {}
for key, value in pairs:
    if key not in normal_dict:
        normal_dict[key] = []
    normal_dict[key].append(value)

# defaultdict：首次存取不存在 key 時，會自動建立空 list。
default_dict = defaultdict(list)
for key, value in pairs:
    default_dict[key].append(value)

print("normal:", normal_dict)
print("defaultdict:", dict(default_dict))
