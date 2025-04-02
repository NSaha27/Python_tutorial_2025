"""
  Card Payment Receipt Project
  -----------------------------
  This program receives the payment amount and credit or debit card number, formats the card number and print a payment success message including the formatted card number.
"""

amount = int(input("Enter amount: Rs."))
card_number = input("Enter card number: ")

last_4_digits = card_number[-4:]
remaining_digits_and_spaces = card_number[:-4]
formatted_card_number = ""
for c in remaining_digits_and_spaces:
    if c.isspace():
        formatted_card_number += " "
    else:
        formatted_card_number += "X"


trans_message = f"Transaction Alert\nAmount ${amount} has been debited from your card\n{formatted_card_number + last_4_digits}"

print()
print(trans_message.center(40))
