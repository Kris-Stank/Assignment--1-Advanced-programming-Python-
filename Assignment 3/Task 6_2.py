import math

def triangle_area_by_sides(a, b, c):
    p = (a + b + c) / 2.0
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

a = float(input())
b = float(input())
c = float(input())
d = float(input())
diag = float(input())

s1 = triangle_area_by_sides(a, b, diag)
s2 = triangle_area_by_sides(c, d, diag)

print(s1 + s2)
