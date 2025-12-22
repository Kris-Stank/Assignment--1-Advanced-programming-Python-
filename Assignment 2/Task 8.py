s1, s2 = input(), input()

if len(s1) != len(s2):
    print("NO")
else:
    countr = [0]*26

    for ch in s1:
        countr[ord(ch)-ord("A")] += 1
    for ch in s2:
        countr[ord(ch)-ord("A")] -= 1

    if all(x==0 for x in countr):
        print("YES")
    else:
        print("NO")
