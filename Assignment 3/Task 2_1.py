import math

def triangle_area_by_sides(a, b, c):
    p = (a + b + c) / 2.0
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

a = float(input())

one_triangle = triangle_area_by_sides(a, a, a)
print(6 * one_triangle)
