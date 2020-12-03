'''
-------------------------------------------------------------------------------
Name:		minutes_days.py
Purpose:	Converts Minutes to days, hours and minutes

Author:	Lui.G

Created:	03/12/2020
------------------------------------------------------------------------------
'''
# Variables for the converter
minutes = int(input("How many minutes would you like to convert? "))
hours = minutes // 60
days = hours // 24
minutes_left = minutes - (hours * 60)
hours_left = hours - (days * 24)

# Output of the minutes to days, hours and days calculator
print(minutes, "minutes is equal to", days, "days", hours_left, "hours and", minutes_left, "minutes.")