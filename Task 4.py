num = int(input())
summ = 0

if num >= 1:
    for i in range(1, num+1):
        summ += i
else:
    for i in range(num, 2):
        summ += i

print(summ)
