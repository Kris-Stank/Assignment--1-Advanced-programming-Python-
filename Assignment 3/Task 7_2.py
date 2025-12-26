n = int(input())

oct_str = oct(n)
oct_str = oct_str[2:] 

while len(oct_str) < 10:
    oct_str = "0" + oct_str

print(oct_str)
