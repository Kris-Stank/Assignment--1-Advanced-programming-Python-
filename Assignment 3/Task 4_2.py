def inside_circle(x, y, a, b, r):
    dx = x - a
    dy = y - b
    return dx * dx + dy * dy <= r * r

a = float(input())
b = float(input())
r = float(input())

count = 0
k = 0
while k < 3:
    x = float(input())
    y = float(input())
    if inside_circle(x, y, a, b, r):
        count += 1
    k += 1

print(count)
