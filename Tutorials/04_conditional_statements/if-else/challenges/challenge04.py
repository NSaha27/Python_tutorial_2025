# marksheet program

print("Enter the following details of the student:")

# student personal details
stu_roll = input("Enter roll number: ")
if len(stu_roll) == 0 or len(stu_roll) > 8:
    print("invalid roll number!")
    stu_roll = input("Enter a valid roll number: ")

stu_name = input("Enter name: ")

# student marks details
marks_in_bengali = float(input("Enter marks in Bengali: "))
if 0 < marks_in_bengali > 100:
    print("invalid marks!")
    marks_in_bengali = float(input("Enter a valid marks: "))

marks_in_english = float(input("Enter marks in English: "))
if 0 < marks_in_english > 100:
    print("invalid marks!")
    marks_in_english = float(input("Enter a valid marks: "))

marks_in_math = float(input("Enter marks in Math: "))
if 0 < marks_in_math > 100:
    print("invalid marks!")
    marks_in_math = float(input("Enter a valid marks: "))

marks_in_life_science = float(input("Enter marks in Life-science: "))
if 0 < marks_in_life_science > 100:
    print("invalid marks!")
    marks_in_life_science = float(input("Enter a valid marks: "))

marks_in_physical_science = float(input("Enter marks in Physical-science: "))
if 0 < marks_in_physical_science > 100:
    print("invalid marks!")
    marks_in_physical_science = float(input("Enter a valid marks: "))

marks_in_history = float(input("Enter marks in History: "))
if 0 < marks_in_history > 100:
    print("invalid marks!")
    marks_in_history = float(input("Enter a valid marks: "))

marks_in_geography = float(input("Enter marks in Geography: "))
if 0 < marks_in_geography > 100:
    print("invalid marks!")
    marks_in_geography = float(input("Enter a valid marks: "))

marks_in_additionals = float(input("Enter marks in additional subjects: "))
if 0 < marks_in_additionals > 100:
    print("invalid marks!")
    marks_in_additionals = float(input("Enter a valid marks: "))

marks_in_env_science = float(input("Enter marks in Environmental-science: "))
if 0 < marks_in_env_science > 100:
    print("invalid marks!")
    marks_in_env_science = float(input("Enter a valid marks: "))

calc_percentage = round(((marks_in_bengali + marks_in_english + marks_in_math + marks_in_life_science +
                          marks_in_physical_science + marks_in_history + marks_in_geography + marks_in_additionals) * 100 / 800), 2)

calc_grade = None

if calc_percentage > 90 and calc_percentage <= 100:
    calc_grade = "A+"
elif calc_percentage > 75 and calc_percentage <= 90:
    calc_grade = "A"
elif calc_percentage > 60 and calc_percentage <= 75:
    calc_grade = "B"
elif calc_percentage > 45 and calc_percentage <= 60:
    calc_grade = "C"
elif calc_percentage > 30 and calc_percentage <= 45:
    calc_grade = "D"
else:
    calc_grade = "F"

print()

print(f"Student name: {stu_name}")
print(f"Student roll no.: {stu_roll}")
print("Marksheet:")
print("Bengali          English          Math             Life Science     Physical Science History          Geography        Additional       Env. Science     Total Percentage Grade")
print(f"{marks_in_bengali}              {marks_in_english}              {marks_in_math}              {marks_in_life_science}              {marks_in_physical_science}              {marks_in_history}              {marks_in_geography}              {marks_in_additionals}              {marks_in_env_science}              {calc_percentage}              {calc_grade}")
