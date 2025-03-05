# find factorial of any number between 1 and 10
import random

rand_num = random.randint(1, 10)
copy_rand_num = rand_num
fact = 1
while copy_rand_num > 0:
    fact *= copy_rand_num
    copy_rand_num -= 1

print(f"factorial of {rand_num} is {fact}")
