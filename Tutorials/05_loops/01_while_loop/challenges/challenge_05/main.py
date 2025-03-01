# Find sum of given numbers as input

num_of_given_numbers = int(
    input("Enter the number of the given numbers you want to sum up: "))

if num_of_given_numbers <= 0:
    num_of_given_numbers = int(
        input("Enter a valid number: "))

counter = 1
sum = 0
while counter <= num_of_given_numbers:
    value = float(input(f"Enter value {counter}: "))
    sum += value
    counter += 1

print(f"summation of {counter-1} numbers is : {sum}")
