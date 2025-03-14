#ask the user for inputs
num1 = float(input("Enter the first number: "))
operation =(input("Enter the operation [+, -, *, /]"))
num2 = float(input("Enter the second number: "))

#perform the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operation")
#display the result
print(f"{num1} {operation} {num2} = {result}")
             
