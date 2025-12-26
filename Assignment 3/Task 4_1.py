def gcd(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

A = int(input())
B = int(input())
C = int(input())
D = int(input())

num = A * D
den = B * C

g = gcd(num, den)
num = num // g
den = den // g

print(num, den)
