a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))

if b != 0:
    result = a // b
else:
    result = "Cannot divide by zero"

print("Result =", result)