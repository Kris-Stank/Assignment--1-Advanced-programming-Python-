def swap_first_last(arr):
    if len(arr) > 1:
        tmp = arr[0]
        arr[0] = arr[len(arr) - 1]
        arr[len(arr) - 1] = tmp

m = int(input())
line = input().split()

arr = []
i = 0
while i < len(line):
    arr.append(int(line[i]))
    i += 1

print("Original:", arr)
swap_first_last(arr)
print("Result:", arr)
