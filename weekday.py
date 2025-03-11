# Write a program that outputs whether or not today is a weekday

# Find out what day it is
from datetime import date
import calendar
my_date = date.today()
today = calendar.day_name[my_date.weekday()]

weekday = ("Monday","Tuesday","Wednesday","Thursday","Friday")

if today in weekday:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")




