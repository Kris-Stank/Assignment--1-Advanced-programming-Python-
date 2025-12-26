n = int(input())

k = 1
first = True

while k <= n:
    s = str(k)
    ok = True

    i = 0
    while i < len(s):
        d = int(s[i])
        if d == 0:
            ok = False
            break
        if k % d != 0:
            ok = False
            break
        i += 1

    if ok:
        if first:
            print(k, end="")
            first = False
        else:
            print(" " + str(k), end="")
    k += 1

print()
