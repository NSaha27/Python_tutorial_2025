# Calculate discounted amount

amount = float(input("Enter the amount: "))
if amount < 0:
  amount = abs(amount)

discount_rate = 0

if amount <= 1000:
  discount_rate = 10
elif 1000 < amount <= 5000:
  discount_rate = 20
elif 5000 < amount <= 10000:
  discount_rate = 30
else:
  discount_rate = 50

net_amount = amount * (100 - discount_rate) / 100

print(f"The net amount is Rs.{net_amount}")