import math

shape = input().strip().lower()

if shape == "rectangle":
    a = float(input())
    b = float(input())
    print(a * b)

elif shape == "square":
    a = float(input())
    print(a * a)

elif shape == "triangle":
    base = float(input())
    height = float(input())
    print(0.5 * base * height)

elif shape == "circle":
    r = float(input())
    print(math.pi * r * r)

else:
    print("Unknown shape")
