for t in range(3):
    line = input().split()

    nums = []
    i = 0
    while i < len(line):
        nums.append(int(line[i]))
        i += 1

    s = 0
    i = 0
    while i < len(nums):
        s += nums[i]
        i += 1

    mean = s / len(nums)
    print(s, mean)
