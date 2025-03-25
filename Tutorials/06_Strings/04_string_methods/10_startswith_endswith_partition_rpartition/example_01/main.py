"""
  str.startswith(string/tuple of strings, start, end)
  ----------------------------------------------------
  This method returns True if a string starts with a particular sub-string or any of the sub-strings in a given tuple. Other paramters are optional.
  
  str.endswith(string/tuple of strings, start, end)
  --------------------------------------------------
  This method returns True if a string ends with a particular sub-string or any of the sub-strings in a given tuple. other parameters are optional.

  str.partition(seperator)
  -------------------------
  This method splits a string into 3 parts and return them as a tuple. The first part will be the part of the string before the seperator, the second part will be the seperator, and the third part will be the part of the string after the seperator. It creates the partition from left side of the string.

  str.rpartition(seperator)
  --------------------------
  This method splits a string into 3 parts and return them as a tuple. The first part will be the part of the string after the seperator, the second part will be the seperator, and the third part will be the part of the string before the seperator. It creates the partition from right side of the string.
"""

s1 = "Python is an easy language"
print(f"Is the string starting with 'Py'? {s1.startswith("Py")}")
print(f"Is the string ending with 'language'? {s1.endswith("language")}")

print(s1.partition(" "))
print(s1.rpartition(" "))
