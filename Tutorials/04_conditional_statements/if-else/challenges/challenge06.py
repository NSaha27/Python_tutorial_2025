# marksheet program 2 - where a student will only pass if he/she has got pass marks (45) in each subjects, and has also passed in total (50%).

pass_mark_in_each = 45
pass_percentage_in_total = 50

# getting student details
stu_roll = input("Enter the roll number: ")
stu_name = input("Enter student name: ")

# getting marks
print()
print("Enter the following marks:")
ACCOUNTANCY = float(input("Enter marks in Accountancy: "))
BEBM = float(
    input("Enter marks in Business Economics and Business Math(BEBM): "))
BM = float(input("Enter marks in Business Management(BM): "))
CMA = float(input("Enter marks in Cost and Management Accounting(CMA): "))
ECOGEO = float(input("Enter marks in Economic Geography(ECOGEO): "))

isPassedTheExam = True

# setting pass condition
if ACCOUNTANCY < 0 and ACCOUNTANCY > 100:
    print("invalid marks in Accountancy!")
    ACCOUNTANCY = float(input("Enter a valid marks in Accountancy (0-100): "))
if ACCOUNTANCY < pass_mark_in_each:
    isPassedTheExam = False

if BEBM < 0 and BEBM > 100:
    print("invalid marks in BEBM!")
    BEBM = float(input(
        "Enter a valid marks in Business Economics and Business Math(BEBM) (0-100): "))
if BEBM < pass_mark_in_each:
    isPassedTheExam = False

if BM < 0 and BM > 100:
    print("invalid marks in BM!")
    BM = float(input("Enter a valid marks in Business Management(BM) (0-100): "))
if BM < pass_mark_in_each:
    isPassedTheExam = False

if CMA < 0 and CMA > 100:
    print("invalid marks in CMA!")
    CMA = float(
        input("Enter a valid marks in Cost and Management Accounting(CMA) (0-100): "))
if CMA < pass_mark_in_each:
    isPassedTheExam = False

if ECOGEO < 0 and ECOGEO > 100:
    print("invalid marks in ECOGEO!")
    ECOGEO = float(
        input("Enter a valid marks in Economic Geography(ECOGEO) (0-100): "))
if ECOGEO < pass_mark_in_each:
    isPassedTheExam = False

total_marks = ACCOUNTANCY + BEBM + BM + CMA + ECOGEO
percentage = total_marks * 100 / (100 * 5)

if percentage < pass_percentage_in_total:
    isPassedTheExam = False

print()
print(f"{stu_name}({stu_roll}) {'passed' if isPassedTheExam else 'did not pass'} the exam")
