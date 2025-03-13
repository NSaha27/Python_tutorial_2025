# print prime numbers between 1 and 100

print("print prime numbers among a range of numbers:")
start = int(input("Enter the number from where to start checking: "))
end = int(input("Enter the number at which to end checking: "))
primes = ""
for i in range(start, end + 1):
    if i == 1:
        continue
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        primes += str(i) + ", "

print(f"prime numbers between {start} and {end} are: {primes}")
