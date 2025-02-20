# should you wear a jacket and take an umbrella or take only an umbrella with you, based on rain and temperature outside.

is_rain_outside = input("Is there rain outside? (yes/no): ")
rain_outside = True if is_rain_outside else False
temperature = float(input("Enter the outside temperature (in celsius): "))

if rain_outside:
    print("you should bring an umbrella")
else:
    print("you don't need to bring an umbrella.")

if temperature >= 17:
    print(", and you need not wear a jacket")
else:
    print(", and you should wear a jacket")
