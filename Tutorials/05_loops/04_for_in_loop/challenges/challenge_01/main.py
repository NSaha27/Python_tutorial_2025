# Display multiplication table for a given number
"""
print("Multiplication table for a given number:")
num = int(input("Enter the number: "))
if num < 0:
    num = int(input("Enter a valid number: "))

multiplication_upto = int(
    input("Enter the number upto which you want to multiply: "))
if multiplication_upto < 1:
    multiplication_upto = int(
        input("Enter a valid number upto which you want to multiply: "))

for n in range(1, multiplication_upto + 1):
    print(f"{num} X {n} = {num * n}")
"""

# Find the factorial of a given number

print("Factorial of a given number:")
num = int(input("Enter the number: "))
if num < 0:
    num = int(input("Enter a valid number: "))
fact = 1
for n in range(1, num + 1):
    fact *= n
print(f"Factorial of {num} is : {fact}")
