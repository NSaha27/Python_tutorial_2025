"""
  str.index(value, start, end)
  -----------------------------
  This method searches the position(index) of the string from beginning at which it finds a substring(here 'value') and returns it, otherwise, it throws a ValueError.

  str.rindex(value, start, end)
  ------------------------------
  This method does the same thing as above but it starts searching from the end.
"""

s1 = "Hello and welcome to the world's best Python course. Python is a general purpose, interpreted, dynamically typed, platform independant, object oriented programming langauge used in data science, data visualization, web development, web scrapping, machine learning, artificial intelligence etc. Python supports both procedural and object-oriented way of programming."

print(
    f"The word 'object oriented programming' is found at index {s1.index('object oriented programming')}")

try:
    foundAt = s1.index('procedural programming')
    print(f"The word 'procedural programming' is found at index {foundAt}")
except:
    print(
        f"The word 'procedural programming' is not there in the above string.")

# str.rindex()

try:
    # foundAt = s1.rindex('interpreted', 70, 80)
    # foundAt = s1.rindex('interpreted', 85)
    foundAt = s1.rindex('interpreted')
    print(
        f"The sub-string 'interpreted' is found in the above string at index {foundAt}")
except:
    print(f"The sub-string 'interpreted' is not found in the above string.")
