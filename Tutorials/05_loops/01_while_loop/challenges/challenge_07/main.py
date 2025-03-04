# find maximum number from the given numbers

"""
num_of_numbers = int(input("Enter how many numbers you want to compare: "))

if num_of_numbers <= 0:
    num_of_numbers = int(
        input("invalid input! enter a value greater than zero: "))

counter = 1
maximum = 0

while counter <= num_of_numbers:
    value = float(input("Enter the value you want to compare: "))
    # if value > maximum:
    #     maximum = value
    # --- or ---
    maximum = max(maximum, value)
    counter += 1

print(f"The maximum number among the numbers you typed, was: {maximum}")

"""

# --- convert a decimal number to a binary number ---

val = int(input("Enter a decimal value: "))

binary = format(val, "b")

print(f"The binary form of {val} is {binary}")
