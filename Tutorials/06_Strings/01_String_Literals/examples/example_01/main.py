# reverse a string
s1 = "Hello World"
rev_s1 = ""
for i in range(len(s1)-1, -1, -1):
    rev_s1 += s1[i]

print(f"The reversed string is: {rev_s1}")
print()

# concatenation of two or more strings
s2 = "Python Tutorial:\n"
s3 = "Python is a high-level, general purpose, dynamically-typed, interpreted, and object-oriented programming language.\n"
s4 = "Python is used in Data Science, Data Visualization, Web Development, Web Scrapping, Machine Learning, Artificial Intelligence etc."
s5 = s2 + s3 + s4
print(s5)

# string repeatition
s6 = "Welcome! "
print(s6 * 3)
