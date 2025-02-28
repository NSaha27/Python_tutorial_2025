# check if a number is a Palindrome

num = int(input("Enter a number: "))
if num < 0:
    num = int(input("Enter a positive number: "))

copy_num = num
rev_num = ""

while copy_num > 0:
    rev_num += str(copy_num % 10)
    copy_num //= 10

rev_num = int(rev_num)

print(f"{num} {'is' if num == rev_num else 'is not'} a Palindrome number.")
