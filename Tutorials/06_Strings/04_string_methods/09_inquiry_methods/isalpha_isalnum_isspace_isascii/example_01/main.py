"""
  str.isalpha()
  --------------
  Returns True if all the characters in the string are alphabets, otherwise returns False.

  str.isalnum()
  --------------
  Returns True if the string is a collection of alpha-numeric characters.

  str.isspace()
  --------------
  Returns True if all the characters in the string are white spaces.

  str.isascii()
  --------------
  Returns True if all the characters in the string is ascii characters.
"""

s1 = "Love you 3000"
print(f"are all characters alphabets? {s1.isalpha()}")

s2 = "HelloWorld"
print(f"are all characters alphabets? {s2.isalpha()}")

s3 = "Loveyou3000"
print(f"are characters alpha-numeric? {s3.isalnum()}")

s4 = "     "
print(f"are all characters spaces? {s4.isspace()}")

s5 = "Hello$World!"
print(f"are all characters ascii? {s5.isascii()}")

# program - 1
print()
print("Enter the following customer details:")
username = input("Enter username (should be in uppercase): ").strip()
if not (username.isupper() and username.isalnum()):
    username = input(
        "Enter valid username (should be in uppercase and have alpha-numeric characters): ").strip()

name = input("Enter name: ").strip()
if not (name.istitle() and name.isascii()):
    name = input("Enter valid name (ex. John Doe): ").strip()

phone = input("Enter phone number: ").strip()
if not (phone.isnumeric() and len(phone) == 10):
    phone = input(
        "Enter valid phone number (digits only, having length 10): ").strip()

email = input("Enter email ID: ").strip()
if not (email.islower() and email.isascii() and email.find("@") != -1 and email.endswith((".com", ".in", ".org", ".net", ".au", ".ai", ".edu.in"))):
    email = input("Enter valid email ID: ").strip()

password = input("Enter password: ").strip()
if not (password.isascii() and len(password) > 6 and len(password) <= 20):
    password = input("Enter valid password (length 6-20): ").strip()

print()
print(
    f"Customer Details:\nUsername: {username}\nName: {name}\nPhone: {phone}\nEmail: {email}\nPassword: {password}")
