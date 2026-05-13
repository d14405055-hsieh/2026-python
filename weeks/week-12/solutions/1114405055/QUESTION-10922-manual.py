# UVA 10922 — 2 the 9s (Manual Version)

def sum_digits(num_str):
    return sum(int(d) for d in num_str)

while True:
    num_str = input().strip()
    
    if num_str == "0":
        break
    
    digit_sum = sum_digits(num_str)
    
    if digit_sum % 9 != 0:
        print(f"{num_str} is not a multiple of 9.")
    else:
        degree = 1
        current = digit_sum
        
        while current != 9:
            current = sum_digits(str(current))
            degree += 1
        
        print(f"9-degree of {num_str} is {degree}.")
