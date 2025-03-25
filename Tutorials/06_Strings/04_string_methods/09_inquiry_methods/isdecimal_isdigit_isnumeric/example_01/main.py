"""
  str.isdecimal()
  ----------------
  This method returns True only if the string has decimal values (i.e. integer values)

  str.isdigit()
  --------------
  This method returns True if the string has digits only. It can accept digits extended to decimal exponents.

  str.isnumeric() [consider this method over the above methods]
  ----------------
  This method returns True if the string has any numeric values. It can accept numbers extended to any exponent (i.e. decimal or non-decimal exponents).
"""

s1a = "1024"
print(f"is s1a a valid decimal value? {s1a.isdecimal()}")

s1b = "1024.54"
print(f"Is s1b a valid decimal value? {s1b.isdecimal()}")

s2a = "102.8"
print(f"Is s2a a valid digit? {s2a.isdigit()}")

s2b = "102"
print(f"Is s2b a valid digit? {s2b.isdigit()}")

s3a = "52.5"
print(f"Is s3a a valid numeric value? {s3a.isnumeric()}")

s3b = "52"
print(f"Is s3b a valid numeric value? {s3b.isnumeric()}")
