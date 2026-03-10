"""
Author: Vincenzo Panes
Propouse: This program calcualte the volume of a tire
The option to buy the tire and enter the phone number was added
"""
import math
from datetime import datetime, timedelta

#Ask the user for the data
width = float(input("Enter the width of the tire in mm: "))
a_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

#Calculate the volume
volume = math.pi * width **2 *a_ratio * (width * a_ratio + 2540 * diameter) / 10000000000

#Ask the user if wants to buy the tire
buy_tire = input("Do you want to buy this tire? (yes/no): ").lower()
if buy_tire == "yes":
    phone = input("Please enter your phone number: ")
else:
    phone = ""

#Print the volume
print(f"The approximate volume is {volume:.2f} liters")

#Calculate the current date and time
current_date_and_time = datetime.now().strftime("%Y-%m-%d")

#Open in a text
with open("volumes.txt", "a") as file:
    file.write(f"{current_date_and_time}, {width:.0f}, {a_ratio:.0f}, {diameter:.0f}, {volume:.2f}, {phone}\n")