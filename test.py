# This program adds two numbers with basic validation

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a >= 0 and b >= 0:
    print("Sum:", a + b)
else:
    print("Please enter positive numbers only.")
