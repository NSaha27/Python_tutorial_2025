# Take a day number and display day name

day_number = int(input("Enter a day number (0-6): "))
day = ""

if day_number == 0:
    day = "Monday"
elif day_number == 1:
    day = "Tuesday"
elif day_number == 2:
    day = "Wednessday"
elif day_number == 3:
    day = "Thursday"
elif day_number == 4:
    day = "Friday"
elif day_number == 5:
    day = "Saturday"
elif day_number == 6:
    day = "Sunday"
else:
    day = "Invalid"

print(f"The day is {day}")
