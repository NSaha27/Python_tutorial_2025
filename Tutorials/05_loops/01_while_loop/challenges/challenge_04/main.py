# check if a number is a Palindrome

num = int(input("Enter a number: "))
if num < 0:
    num = int(input("Enter a positive number: "))

copy_num = num
rev_num = 0

while copy_num > 0:
    r = copy_num % 10
    copy_num //= 10
    rev_num = rev_num * 10 + r


print(f"{num} {'is' if num == rev_num else 'is not'} a Palindrome number.")
