# Find sum of digits in a number

num = int(input("Enter a number: "))
if num < 0:
    num = int(input("Enter a positive number: "))

copy_num = num
sum = 0
while copy_num > 0:
    sum += copy_num % 10
    copy_num //= 10

print(f"sum of all digits of {num} is {sum}")
