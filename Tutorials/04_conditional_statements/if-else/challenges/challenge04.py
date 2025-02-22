# check if a person is authorised for admin access

admin_id = "NILADRISAHA"
admin_password = "Niladri12345"

id = input("Enter admin ID: ")
password = input("Enter password: ")

if id == admin_id and password == admin_password:
    print("Welcome back admin!")
else:
    print("Invalid admin ID or password!")
