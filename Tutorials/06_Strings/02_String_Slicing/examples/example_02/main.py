s1 = "Niladri Saha"

space_index = s1.index(" ")

name = s1[0:space_index:1]
surname = s1[space_index+1::1]

print(f"Name of the person : {name}\nSurname of the person : {surname}")
