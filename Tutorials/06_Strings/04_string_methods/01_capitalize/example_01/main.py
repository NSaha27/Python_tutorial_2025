"""
  str.capitalize()
  -----------------
  working: This method converts the first letter of a string to uppercase and other letters to lowercase.
  return: This method returns a string.
  points: If the first letter of the string is a number, it doesn't convert it to anything, but converts other alphabetical characters to lowercase.
"""

s1 = "hello and welcome to the tutorial on String Methods of Python"

print(s1.capitalize())

print()

s2 = input("Left your message here...\n=> ")

print(f"Your remarks to us:\n{s2.capitalize()}")
