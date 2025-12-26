n = int(input())

d = 1
first = True
while d <= n:
    if n % d == 0:
        if first:
            print(d, end="")
            first = False
        else:
            print(" " + str(d), end="")
    d += 1

print()
