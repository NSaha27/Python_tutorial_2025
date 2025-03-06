# for loop with range function

# for num in range(0, 10):
#     print(num)

# for num in range(5, 12):
#     print(num)

# for num in range(0, 20, 3):
#     # this will print values starting from 0 and ending at 20 but skipping 2 values each time
#     print(num)

# for num in range(20, 0, -2):
#     # this will print values starting from 20 and ending at 0 i.e. printing backwards, but skipping 1 step each time
#     print(num)

# --- write a program to print all even and odd values between 100 and 500 seperately ---

evens = ""
odds = ""

for num in range(100, 500):
    if num % 2 == 0:
        evens += str(num) + ", "
    else:
        odds += str(num) + ", "

print(
    f"even numbers between 100 and 500 are : {evens}\n\nodd numbers between 100 and 500 are : {odds}")
