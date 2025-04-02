"""
  Restaurant Menu Project
  ------------------------
  This program will take 4 menu items and their respective prices as inputs, then format and print them.
"""

print("Enter menu items and their prices:")
counter = 1
menu = ""
while counter <= 4:
    item_name = input(f"Enter item {counter} name: ").strip()
    item_price = int(input(f"Enter item {counter} price: $").strip())
    dash = "-" * (20 - len(item_name) - (len(str(item_price)) + 1))
    menu += item_name + dash + "$" + str(item_price) + "\n"
    # or
    # item = item_name.ljust(
    #     (20 - (len(str(item_price)) + 1)), "-") + "$" + str(item_price)
    # menu += item + "\n"
    counter += 1

print()
print("Restaurant Menu:")
print(menu)
