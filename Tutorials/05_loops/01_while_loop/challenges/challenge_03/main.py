# Reversing a number

num = int(input("Enter an integer: "))
if num < 0:
    num = int(input("Enter a positive integer: "))

copy_num = num
rev_num = ""

while copy_num > 0:
    rev_num += str(copy_num % 10)
    copy_num //= 10

print(f"The reverse form of {num} is {rev_num}")
