"""
  Palindrome Project
  -------------------
  This program will check whether a string is a palindrome or not
"""

str1 = input("Enter a text: ")

rev_str1 = str1[::-1]

print(f"Is {str1} a palindrome? {str1 == rev_str1}")
