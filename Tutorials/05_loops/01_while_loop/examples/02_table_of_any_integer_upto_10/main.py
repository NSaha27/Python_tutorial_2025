# table of an integer

n = int(input("Enter an integer: "))
if n < 0:
    print("invalid number!")
    n = int(input("Enter a valid integer: "))

counter = 0

while counter <= 10:
    rslt = n * counter
    print(f"{n} X {counter} = {rslt}")
    counter += 1
