equation = input()

if equation[1] == "+":
    if equation[0] == "x":
        print(int(equation[4]) - int(equation[2]))
    elif equation[2] == "x":
        print(int(equation[4]) - int(equation[0]))
    else:
        print(int(equation[0]) + int(equation[2]))

elif equation[1] == "-":
    if equation[0] == "x":
        print(int(equation[4]) + int(equation[2]))
    elif equation[2] == "x":
        print(int(equation[0]) - int(equation[4]))
    else:
        print(int(equation[0]) - int(equation[2]))
