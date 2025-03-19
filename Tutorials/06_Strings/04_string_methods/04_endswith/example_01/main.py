"""
  str.endswith(value/tuple, start, end)
  ---------------------------------------
  working: This method returns True if a string ends with a particular value, or any of the tuple of values, otherwise, it returns False.
  return: This method returns a boolean value
  points: (i) We can pass 2 optional parameters, i.e. start and end to start searching from a certain index and/or end searching at a certain index.
"""

email1 = "sahaniladri25y@gmail.com"

print(f"Is this email a commercial email? {email1.endswith('.com')}")

website = "www.ignou.edu.in"

print(
    f"is this website a valid website? {website.endswith((".com", ".in", ".au"))}")
print(
    f"is this website an educational or a networking based website? {website.endswith((".edu.in", ".edu.net", ".net"))}")
