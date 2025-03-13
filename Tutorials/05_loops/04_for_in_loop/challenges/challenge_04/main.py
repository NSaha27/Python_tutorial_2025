# Find the factors of a number

print("Find factorial of a number:")
while True:
    fact = 1
    num = int(input("Enter a number: "))
    if num == 0:
        print("number should be a non-zero number!")
        continue
    elif num < 0:
        for i in range(1, num - 1):
            fact *= i
    else:
        for i in range(1, num + 1):
            fact *= i
    print(f"factorial of {num} is {fact}")
    option = input("do you want to continue? (yes/no): ")
    if option == "no" or option == "No" or option == "NO" or option == "n" or option == "N":
        print("Thanks for trying me, good bye!")
        break
