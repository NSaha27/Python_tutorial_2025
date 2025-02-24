# check whether a given year is a leap year or not

year = int(input("Enter a year: "))
if year <= 0:
    print("invalid year!")
    year = int(input("Enter a correct year: "))

is_leap_year = True

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 != 0:
            is_leap_year = False
else:
    is_leap_year = False

print(f"{year} is {'a leap' if is_leap_year else 'not a leap'} year!")
