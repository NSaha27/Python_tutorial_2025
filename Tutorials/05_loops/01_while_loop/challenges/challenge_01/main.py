# counting the number of digits in a number

num = int(input("Enter a number: "))
if num < 0:
    print("the required number cannot be a negetive number!")
    num = int(input("Enter a positive number: "))

copy_num = num
counter = 0

while copy_num > 0:
    counter += 1
    copy_num //= 10

print(f"{num} has {counter} digits")
