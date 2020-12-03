'''
-------------------------------------------------------------------------------
Name:		windchill.py
Purpose:	Calculates the windchill from temperature and wind speed

Author:	Lui.G

Created:	03/12/2020
------------------------------------------------------------------------------
'''
# Variables for the calculator
temperature =  float(input("Enter temperate (celsius) for the calculations: "))
windspeed = float(input("Enter speed (km/h) for the calculations: "))

# Calculate the windchill
windchill = 13.12 + (0.6215 * temperature) - (11.37 *(windspeed**0.16)) + (0.3965 * temperature * (windspeed**0.16))

# Output the calculations
print("The windchill of", str(temperature) + "°C and", str(windspeed) + "km/h is", round(windchill))