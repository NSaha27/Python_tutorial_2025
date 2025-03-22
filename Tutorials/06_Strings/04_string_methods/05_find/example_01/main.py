"""
  str.find(value, start, end)
  ----------------------------
  working: This method returns the first position(index) of a string where the given sub-string(here 'value') is found.
  return: This method returns an integer(the index)
  points: (i) We can pass optional parameters i.e. start and end, to specify from where to start search and at which position to end search.
"""

str1 = "Hello and welcome to the world's best Python course. Python is a general purpose, interpreted, dynamically typed, platform independant, object oriented programming langauge used in data science, data visualization, web development, web scrapping, machine learning, artificial intelligence etc. Python supports both procedural and object-oriented way of programming."

if str1.find("Python") != -1:
    print("The word 'Python' is present in the text.")
else:
    print("The word 'Python' is not present in the text.")

print()

# program - 2
while True:
    username = input("Enter username: ")
    if username.find(" ") != -1:
        print("Enter a valid username: ")
        continue

    email = input("Enter email id: ")
    if email.find("@") == -1 or not email.endswith((".com", ".in", ".org", ".net", ".au")):
        print("Enter a valid email id: ")
        continue

    password = input("Enter password: ")

    alpUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpLower = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    symb = "@#$&_-."
    hasOneUppercase = False
    hasOneLowercase = False
    hasOneNumber = False
    hasOneSymbol = False
    for ch in password:
        if alpUpper.find(ch) != -1:
            hasOneUppercase = True
        if alpLower.find(ch) != -1:
            hasOneLowercase = True
        if num.find(ch) != -1:
            hasOneNumber = True
        if symb.find(ch) != -1:
            hasOneSymbol = True
    if not (hasOneUppercase and hasOneLowercase and hasOneNumber and hasOneSymbol):
        print("Enter a valid password (must have atleat one uppercase alphabet, one lowercase alphabet, one number and one special symbol)!")
        continue

    if username and email and password:
        print("*registration successful!")
        break
