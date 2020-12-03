'''
-------------------------------------------------------------------------------
Name:		days_hours.py
Purpose:	Converts hours to day and hours

Author:	Lui.G

Created:	03/12/2020
------------------------------------------------------------------------------
'''

# Variables for the converter
hours = int(input("How many hours would you like to convert? "))
days = hours // 24
hours_left = hours - (days * 24)

# Output of the hours to day and hours calculator
print(hours, "hours is equal to", days, "days and", hours_left, "hours.")



