# simple variable declaration
username = "niladrisaha"
name = "Niladri Saha"
phone = "8981684201"
email = "sahaniladri25y@gmail.com"
password = "Nil12345"

print("User details:"), print("Username:", username), print("Name:", name), print("Phone:", phone), print("Email Id:", email), print("Password:", password)

print()

# variable declaration in single line
street, city, state, zipcode = "Rani Rasmoni Avenue", "Kolkata", "West Bengal", "700075"

print("Address details:")
print("Street:", street)
print("City:", city)
print("State:", state)
print("Zip Code:", zipcode)

# variable annotation (mention what would be the datatype)
firstname:str = "Niladri"
lastname:str = "Saha"
year_of_birth:int = 1992
weight:float = 62.3
is_an_adult:bool = True

print()
print("Full name:", firstname, lastname)
print("Year of birth:", year_of_birth)
print("Weight:", weight)
print("Is an adult?:", is_an_adult)

# delete a variable (If the variable is called again after deletion, it will throw a NameError)
del weight
del is_an_adult

print("Now the weight is:", weight)
print("Is an adult now?:", is_an_adult)
