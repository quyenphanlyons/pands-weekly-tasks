# Task 5
# Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
# You will need to search the web to find how you work out what day it is.
# Write a program that outputs whether or not today is a weekday

# -------------------


from datetime import date
import calendar
my_date = date.today()
today = calendar.day_name[my_date.weekday()]

weekday = ("Monday","Tuesday","Wednesday","Thursday","Friday")

if today in weekday:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")


# Ressources
# Find out what day it is Source stackoverflow



