

# while True:
#     operand = input("Enter the number1: ")
#     try:
#         operand = float(operand)
#         break
#     except:
#         print("Invalid input. Please enter a numeric value.")

# while True:
#     operand2 = input("Enter the number2: ")
#     try:
#         operand2 = float(operand2)
#         break
#     except:
#         print("Invalid input. Please enter a numeric value.")


# def get_number():
#     while True:
#         operand = input("Enter the number: ")
#         try:
#             operand = float(operand)
#             return operand
#         except:
#             print("Invalid input. Please enter a numeric value.")


# operand = get_number()
# operand2 = get_number()

def get_number(prompt):
    while True:
        operand = input(prompt)
        try:
            operand = float(operand)
            return operand
        except:
            print("Invalid input. Please enter a numeric value.")


operand = get_number("Enter the number1: ")
operand2 = get_number("Enter the number2: ")
result = 0
sign = input("Enter the operation (+, -, *, /): ")
if sign == "+":
    result = operand + operand2
    print(f"The result of {operand} + {operand2} is {result}")
elif sign == "-":
    result = operand - operand2
    print(f"The result of {operand} - {operand2} is {result}")
elif sign == "*":
    result = operand * operand2
    print(f"The result of {operand} * {operand2} is {result}")
elif sign == "/":
    if operand == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = operand / operand2
        print(f"The result of {operand} / {operand2} is {result}")

print("rest of the operation is: ", result)
