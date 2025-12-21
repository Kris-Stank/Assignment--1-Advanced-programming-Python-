equation = input()

if equation[1] == "+":
    print(int(equation[4])-int(equation[2]))
elif equation[1] == "-":
    if equation[0] == "x":
        print(int(equation[2])-int(equation[4]))
    else:
        print(int(equation[0])-int(equation[4]))