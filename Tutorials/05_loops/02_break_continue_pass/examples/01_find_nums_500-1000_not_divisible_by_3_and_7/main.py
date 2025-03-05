# find numbers between 500 and 1000 that are not divisible by 3 and 7

start = 800
end = 1000
copy_start = start
numbers = ""
while copy_start <= end:
    if copy_start % 3 == 0 or copy_start % 7 == 0:
        pass
    else:
        numbers += str(copy_start) + ", "
    copy_start += 1

print(
    f"Numbers between {start} and {end} that are not divisible by 3 and 7 are : {numbers}")
