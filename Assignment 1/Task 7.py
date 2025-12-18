num1 = int(input("First number: "))
sign = input("Operation: ")
num2 = int(input("Second number: "))

if sign == "+":
    print(num1 + num2)
elif sign == "*":
    print(num1 * num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "/":
    if num2 != 0:
        print(num1 // num2)
    else:
        print("Error")