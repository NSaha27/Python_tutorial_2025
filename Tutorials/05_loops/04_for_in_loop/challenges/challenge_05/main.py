# Check if a number is prime or not

print("Check if the entered number is prime or not:")
while True:
    isPrime = True
    num = int(input("Enter a number: "))
    if num <= 0:
        print("invalid number!")
        continue
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    print(f"{num} is {'a' if isPrime else 'not a'} prime number.")
    option = input("do you want to check again? (y/n): ")
    if option in ("No", "NO", "no", "n"):
        print("Thanks for visit!")
        break
