# U2. 星號解包可處理不定長，且 * 接收結果一定是 list（1.2）

record1 = ("Dave", "dave@example.com")
name1, email1, *phones1 = record1
print("case1:", name1, email1, phones1, type(phones1))

record2 = ("Tom", "tom@example.com", "0912-000-001", "02-1234-5678")
name2, email2, *phones2 = record2
print("case2:", name2, email2, phones2, type(phones2))
