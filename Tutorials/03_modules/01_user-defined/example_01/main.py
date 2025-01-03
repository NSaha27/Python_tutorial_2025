from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

print("Calculator program:-")
first_number = input("Enter first number: ")
first_number = int(first_number) if isinstance(first_number, int) else float(first_number)
second_number = input("Enter second number: ")
second_number = int(second_number) if isinstance(second_number, int) else float(second_number)

print("Select an option:\n(1) Add\n(2) Subtract\n(3) Multiply\n(4) Divide")
option = int(input("-> "))

match option:
  case 1:
    print(add(first_number, second_number))
  case 2:
    print(subtract(first_number, second_number))
  case 3:
    print(multiply(first_number, second_number))
  case 4:
    print(divide(first_number, second_number))
  case _:
    print("invalid option!")
