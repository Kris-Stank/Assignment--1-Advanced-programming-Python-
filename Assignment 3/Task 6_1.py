A = int(input())
B = int(input())

a = A
b = B
while b != 0:
    r = a % b
    a = b
    b = r

g = a
l = (A * B) // g

print(g, l)
