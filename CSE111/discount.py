"""
Author: Vincenzo Panes
Program: Calculate the customer discount on Tuesaday or Wednesday
"""

from datetime import datetime
DISCOUNT_RATE = .1
TAX_RATE = .06

#Determinate the day of the week
today = datetime.now()
day_of_week = today.weekday()

#Ask the User for subtotal
subtotal = float(input("Enter the subtotal: "))
print(f"Total order: {subtotal}")

#Compute and print the discount amount
discount = 0
if day_of_week == 1 or day_of_week == 2:
    if subtotal > 50:
        discount = subtotal * DISCOUNT_RATE
print(f"Discount: {discount}")
subtotal -= discount

#Calculate the tax
tax = subtotal * TAX_RATE

#Calculate the total amount
total = subtotal + tax

#Print the tax and total amount
print(f"Tax: {tax}")
print(f"Total Due: {total}")