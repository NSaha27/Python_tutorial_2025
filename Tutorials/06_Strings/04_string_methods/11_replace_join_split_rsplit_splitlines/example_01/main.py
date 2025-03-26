"""
  str.replace(old, new [, count])
  --------------------------------
  This method replaces a sub-string with another sub-string and returns a new string.

  str.join(iterable)
  -------------------
  This method joins 

  str.split([sep, [, max split count]])
  --------------------------------------
  This method splits a string at the specified seperator and returns a list of the splitted parts.

  str.rsplit([sep, [, max split count]])
  ---------------------------------------
  This method splits a string at the specified seperator but from the end, and returns a list of the splitted parts.

  str.splitlines([keepends])
  ---------------------------
  This method splits a string at new-line escape characters (like - \n, \r, \f etc.), and returns a list of the splitted parts.  
"""

s1 = "Python is a dynamically_typed, general_purpose, interpreted, object_oriented programming language."

s1_new_a = s1.replace("_", "-")
print(f"The replaced string is : '{s1_new_a}'")

s2 = ", ".join(["Niladri", "Arnab", "Tista", "Mitin", "Sujit", "Madhuja"])
print(s2)

s3 = ["Anwesha", "Abhimanyu", "Satindra"]
print(", ".join(s3))

s4 = s1.split(" ")
print(s4, type(s4))

s5 = "Indranil, Koustav, Niladri, Sukanta"
print(s5.split(", "))
