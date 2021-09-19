# File: Payroll.py
# Student: Jingsi Zhou
# UT EID: jz24729
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 09/17/2020
# Date Last Modified: 09/18/2020
# Description of Program: Given a name, number of hours worked, rate of pay, and
# federal and state tax withholding rate, a payroll statement is printed.

name = input("Enter employee's name: ")
numHours = eval(input("Enter number of hours worked in a week: "))
hourlyRate = eval(input("Enter hourly pay rate: "))
fedRate = eval(input("Enter federal tax withholding rate: "))
stateRate = eval(input("Enter state tax withholding rate: "))

gPay = numHours * hourlyRate
federalDeduction = gPay * fedRate 
stateDeduction = gPay * stateRate
totalDeduction = federalDeduction + stateDeduction
netPay = gPay - totalDeduction

print("\nEmployee Name: " + name)
print("Hours Worked:", format(numHours, ".1f"))
print("Pay Rate: $" + str(format(hourlyRate, ".2f")))
print("Gross Pay: $" + str(format(gPay, ".2f")))
print("Deductions:", \
"\n  Federal Witholding (" + str(fedRate * 100) + "%): $" + str(format(federalDeduction, ".2f")) + \
"\n  State Witholding (" + str(stateRate * 100) + "%): $" + str(format(stateDeduction, ".2f")) + \
"\n  Total Deduction: $" + str(format(totalDeduction, ".2f")) + \
"\nNet Pay: $" + str(format(netPay, ".2f")))