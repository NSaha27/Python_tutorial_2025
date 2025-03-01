# Find sum of positive and negetive numbers seperately

num_of_given_numbers = int(
    input("Enter the number of the given numbers you want to sum up: "))

if num_of_given_numbers <= 0:
    num_of_given_numbers = int(
        input("Enter a valid number: "))

counter = 1
sum_of_positives = 0
sum_of_negetives = 0

while counter <= num_of_given_numbers:
    value = float(input(f"Enter number {counter}: "))
    if value <= 0:
        sum_of_negetives += value
    if value > 0:
        sum_of_positives += value
    counter += 1

print(
    f"sum of positive numbers is {sum_of_positives} and sum of negetive numbers is {sum_of_negetives}")
