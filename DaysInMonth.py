# File: DaysInMonth.py
# Student: Jingsi Zhou
# UT EID: jz24729
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 09/25/2020
# Date Last Modified: 09/25/2020
# Description of Program: User inputs a month and year in integer form and program 
# outputs how many days the month has for any given year. Intended for use with the modern
# calendar but also accepts obscure numbers for the year.

month = eval(input("Enter a month of the year as an integer from 1-12: "))

#display error message if month input is not in the valid range
if month > 12 or month < 1:
    print("Please input an integer from 1-12...  ;A;")
    exit()
    
year = eval(input("Enter a year: "))

if month == 4:
    days = 30
elif month == 6:
    days = 30
elif month == 9:
    days = 30
elif month == 11:
    days = 30
else:
    days = 31


if month == 1:
    month = "January"
elif month == 2:
    month = "February"
    #looked up how to find if year is leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
        days = 29
    else: 
        days = 28
elif month == 3:
    month = "March"
elif month == 4:
    month = "April"
elif month == 5:
    month = "May"
elif month == 6:
    month = "June"
elif month == 7:
    month = "July"
elif month == 8:
    month = "August"
elif month == 9:
    month = "September"
elif month == 10:
    month = "October"
elif month == 11:
    month = "November"
else:
    month = "December"
    
print(month, year, "has", days, "days")
