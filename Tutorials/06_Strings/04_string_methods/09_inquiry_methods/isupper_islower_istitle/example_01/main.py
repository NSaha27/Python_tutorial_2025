"""
  str.isupper()
  --------------
  Returns True if all the characters of the string is in uppercase, otherwise returns False.

  str.islower()
  --------------
  Returns True if all the characters of the string is in lowercase, otherwise returns False.

  str.istitle()
  --------------
  Returns True if all the characters of the string is in titlecase, otherwise returns False.
"""

s1 = "Hello World"
print(f"is all letters in uppercase? {s1.isupper()}")

s2 = "HELLO WORLD 2"
print(f"is all letters in uppercase? {s2.isupper()}")

s3 = "hello world 2"
print(f"is all letters in lowercase? {s3.islower()}")

s4 = "Hello World 2"
print(f"is the s3 sentence in titlecase? {s3.istitle()}")
print(f"is the s4 sentence in titlecase? {s4.istitle()}")
