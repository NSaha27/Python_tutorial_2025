# find prime numbers between 100 and 500

start = 100
copy_start = start
end = 500
prime_nums = ""
while copy_start <= end:
    counter = 2
    is_prime = True
    while counter < copy_start:
        if copy_start % counter == 0:
            is_prime = False
            break
        counter += 1
    if is_prime:
        prime_nums += str(copy_start) + ", "
    copy_start += 1

print(f"prime numbers between {start} and {end} are : {prime_nums}")
