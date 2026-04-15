# R2: Star unpacking

def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)


scores = [98, 92, 85, 91, 100]
print("average without first/last ->", drop_first_last(scores))

record = ("Dave", "dave@example.com", "773-555-1212", "847-555-1212")
name, email, *phone_numbers = record
print("name/email/phones ->", name, email, phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print("trailing/current ->", trailing, current)
