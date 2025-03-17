# use of 'in' and 'not in' operator

while True:
    login_username = "NILADRISAHA"
    login_password = "Tist@Dutta#07"

    username = input("Enter username: ")
    print("Enter password")
    password = input(
        "(must have atleast one alphabet, one number, and one special symbol like - $@#&_- etc.): ")

    hasAlphabets = False
    hasNumbers = False
    hasSymbols = False

    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "$@#&_-"

    for char in password:
        if char in alphabets:
            hasAlphabets = True
        if char in numbers:
            hasNumbers = True
        if char in symbols:
            hasSymbols = True

    if hasAlphabets and hasNumbers and hasSymbols:
        print("*valid password!")
    else:
        print("*invalid password!")
        print("*please enter a valid password!")
        continue

    if username == login_username and password == login_password:
        print("*login successful!")
        break
    else:
        print("*invalid login credentials!")
        continue
