ticket = input()
sum1, sum2 = 0, 0

for i in range(3):
    sum1 += int(ticket[i])
    sum2 += int(ticket[i+3])

if len(ticket) == 6:
    if sum1 == sum2:
        print("YES")
    else:
        print("NO")