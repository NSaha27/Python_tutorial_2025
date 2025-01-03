"""
  id() functions:-
  -----------------
  In cpython (i.e. official python package), this function is used to get the memory address of a value/object stored.
"""
first_name: str = "Niladri"
last_name: str = "Saha"
email: str = "sahaniladri25y@gmail.com"

print(id(first_name))
print(id(last_name))
print(id(email))

"""
  type() function:-
  ------------------
  This function is used to find the datatype of a value/object.
"""
city = "Kolkata"
state = "West Bengal"
country = "India"
zip_code = 700075
eligible_for_voting = True

print(type(city))
print(type(state))
print(type(country))
print(type(zip_code))
print(type(eligible_for_voting))

"""
  bin() function:-
  -----------------
  This function returns the binary representation of an integer.
"""
_id = 23
print(bin(_id))
_id = 12
print(bin(_id))

"""
  pow(base, power, modulas) function:-
  ----------------------------
  This function returns a number raised to a certain number.
  It is an alternate of the exponent operator
"""
n1 = 2
n2 = 9

print(f"The value of {n1}, raised to 3 is : {pow(n1, 3)}")
print(f"The value of {n2}, raised to 2 is : {pow(n2, 2)}")

"""
  round(decimal_value, round_upto_this) function:-
  -------------------------------------------------
  This function rounds a decimal value to the mentioned decimal point. If no decimal point is mentioned, it rounds the value to the nearest integer. 
"""
n3 = 23.679
n4 = 51.0823
n5 = 78.524

print(f"rounded value of {n3} to 2 decimal point is : {round(n3, 2)}")
print(f"rounded value of {n4} to 1 decimal point is : {round(n4, 1)}")
print(f"rounded value of {n5} to 0 decimal point is : {round(n5)}")

"""
  abs(value) function:-
  ----------------------
  This function returns the absolute value of a certain number.
"""
n6 = -12
n7 = 7.26
n8 = 92

print(abs(n6))
print(abs(n7))
print(abs(n8))
