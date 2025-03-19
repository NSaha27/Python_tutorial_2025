"""
  str.casefold()
  ---------------
  working: This method forcefully converts a string to lowercase.
  return: This method returns a string.
  points: It doesn't care whatever is the case of a string, it just converts it into lowercase by removing all case distinctions in that string.
"""

s1 = "hello World, WELCOME to the best ever PYTHON Tutorial"

print(f"The converted string is : '{s1.casefold()}'")

name = input("Enter your name: ")
email = input("Enter your email address: ")
password = input("Enter your password (lowercase only): ")

name = name.capitalize()
email = email.casefold()
password = password.casefold()

print(
    f"\nyou've typed the following -\nName: {name}\nEmail ID: {email}\nPassword (encoded): {password}")
