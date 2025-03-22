"""
  str.ljust(width, fill)
  -----------------------
  This method adds leading characters(specified in the second parameter) to a string, and returns a new string.

  str.rjust(width, fill)
  -----------------------
  This method adds trailing characters(specified in the second parameter) to a string, and returns a new string.

  str.center(width, fill)
  ------------------------
  This method adds equal number of leading and trailing characters(specified in the second parameter) to a string, and returns a new string.

  *by default the blank space is set for the 'fill' parameter. 

  str.lstrip([chars])
  --------------------
  This method strips out leading characters that are mentioned in the parameter. It can be a single character or multiple characters given in the form of a string. 

  str.rstrip([chars])
  --------------------
  This method strips out trailing characters that are mentioned in the parameter. It can be a single character or multiple characters given in the form of a string.

  str.strip([chars])
  -------------------
  This method strips out both leading and trailing characters that are mentioned in the parameter. It can be a single character or multiple characters given in the form of a string.
"""

s1 = "Hello World"

print(s1.ljust(15))
print(s1.rjust(15, "_"))
print(s1.center(15, "*"))

s2 = "   Hello World   "
s3 = "... ... ** Hello World ** ... ..."

print(s2.lstrip(" "))
print(s2.rstrip(" "))
print(s3.strip(".* "))
