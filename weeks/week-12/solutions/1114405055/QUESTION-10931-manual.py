# UVA 10931 — Parity (Manual Version)

while True:
    n = int(input())
    
    if n == 0:
        break
    
    binary = bin(n)[2:]
    count = binary.count('1')
    
    print(f"The parity of {binary} is {count} (mod 2).")
