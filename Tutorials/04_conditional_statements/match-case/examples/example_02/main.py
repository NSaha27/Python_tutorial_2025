# create a calculator program using match-case statement

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    option = int(input(
        "Enter the option:\n[1] for addition\n[2] for subtraction\n[3] for multiplication\n[4] for float division\n[5] for floor division\n[6] for modulus\n[7] for exponentiation\n=> "))
    result = None
    match option:
        case 1:
            result = num1 + num2
        case 2:
            result = abs(num1 - num2)
        case 3:
            result = num1 * num2
        case 4:
            result = num1 / num2
        case 5:
            result = num1 // num2
        case 6:
            result = num1 % num2
        case 7:
            result = num1 ** num2
        case _:
            print("invalid option!")
            continue
    print()
    print(f"Result of your selected operation is '{result}'")
    print()
    cont = input("do you want to continue? (y/n): ")
    if cont in ("y", "Y", "yes", "Yes", "YES"):
        continue
    else:
        print("Thanks for using me!")
        break
