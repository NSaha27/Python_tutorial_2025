# print day of a date based on the day number
import datetime

date = input("Enter a date (dd/mm/yyyy): ")
day = int(date.split("/")[0])
month = int(date.split("/")[1])
year = int(date.split("/")[2])
weekday_num = int(datetime.datetime(year, month, day).strftime("%u"))
weekday = ""
match weekday_num:
    case 1:
        weekday = "Sunday"
    case 2:
        weekday = "Monday"
    case 3:
        weekday = "Tuesday"
    case 4:
        weekday = "Wednesday"
    case 5:
        weekday = "Thursday"
    case 6:
        weekday = "Friday"
    case 7:
        weekday = "Saturday"
    case _:
        weekday = "invalid"

print(f"The weekday on {date} is : {weekday}")
