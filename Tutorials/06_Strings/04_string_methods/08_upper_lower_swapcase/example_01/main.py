"""
  str.upper()
  ------------
  This method converts all letters of a string to its uppercase form.

  str.lower()
  ------------
  This method converts all letters of a string to its lowercase form.

  *the main difference of casefold and lower method is that, casefold converts the letter to lowercase forcefully which the lower method doesn't do. 

  str.swapcase()
  ---------------
  This method converts uppercase characters of a string to lowercase and lowercase characters to uppercase.

  str.title()
  ------------
  This method converts the first character of all words in a string to uppercase and the remaining characters to lowercase.
"""

s1 = "Hello World!"

print(s1.upper())

s2 = "HELLO WORLD!"

print(s2.lower())

s3 = "Hello World!"

print(s3.swapcase())

print(s3.title())

# program - 2
username = input("Enter your username: ").strip(" ").upper()
name = input("Enter your name: ").strip(" ").title()
email = input("Enter your email id: ").strip(" ").lower()

print(f"Username: {username}\nName: {name}\nEmail ID: {email}")
