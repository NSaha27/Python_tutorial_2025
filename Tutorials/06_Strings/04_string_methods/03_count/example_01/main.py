"""
  str.count(value, start, end)
  -----------------------------
  working: This method counts the number of times a sub-string occurs in a string.
  return: It returns an integer (number of times a sub-string occurs)
  points: (i) It optionally takes additional two arguments. Where, the 'start' is the index from where to start searching (default is 0), and the 'end' is the index upto where to search (default is the end of the string), (ii) it performs case sensitive search.
"""

str1 = "Hello guys, welcome to python tutorial. Python is one of the most famouse languages in today's era. Python is used in Data Science, ML, AI, Web Development, Web Scrapping, and Mathematical Calculations etc."

print(
    f"The number of times we used the word 'Python' is : {str1.count('Python')}")

print(
    f"The number of times 'Python' is used, starting from 20th index and ending at 50th index : {str1.count('Python', 20, 50)}")
