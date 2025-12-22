# letter num num num letter letter
n = int(input())

for i in range(n):
    LicensePlate = input()
    flag = "No"
    suitable_letters = "ABCEHKMOPTXY"

    if len(LicensePlate) == 6:
        letters = LicensePlate[0] + LicensePlate[5:]
        nums = LicensePlate[1:4]

        if nums.isdigit():
            flag = "Yes"
            for ch in letters:
                if ch not in suitable_letters:
                    flag = "No"
                    break 
    
    print(flag)