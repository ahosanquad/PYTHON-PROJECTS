operator = input("Enter an Operator(+,-,*,/): ")
number1 = float(input("Enter the 1nd Number: "))
number2 = float(input("Enter the 2nd Number: "))

if operator == "+":
    result = number1 + number2
    print(round(result, 3))
elif operator == "-":
    result = number1 - number2
    print(round(result, 3))
elif operator == "*":
    result = number1 * number2
    print(round(result, 3))
elif operator == "/":
    result = number1 / number2
    print(round(result, 3))
else:
    print(f"{operator} is not a Operator")