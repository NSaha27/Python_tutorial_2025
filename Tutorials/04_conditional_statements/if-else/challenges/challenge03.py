# Find difference between two numbers

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

diff = n1 - n2

if diff >= 0:
    print(f"the difference is {diff}")
else:
    print(f"the difference is {abs(diff)}")
