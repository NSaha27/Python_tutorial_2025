# reverse any integer number

n = int(input("Enter an integer: "))

if n <= 0:
    n = int(input("Enter a valid integer: "))

copy_n = n

rev = ""

while copy_n > 0:
    digit = copy_n % 10
    copy_n //= 10
    rev += str(digit)

print(f"The reversed form of {n} is : {int(rev)}")
