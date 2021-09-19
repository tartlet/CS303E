"""n1 = eval(input("First Num? "))
n2 = eval(input("Second Num? "))
k = 1

while k <= n1 and k <= n2:
	if n1 % k == 0 and n2 % k == 0:
		gcd = k
	k += 1
	
print("GCD is", gcd) """  #GCD Program

#Future Tuition:
"""current1 = 10000
yearcount = 0
ncurrent = 10000
nextyear = 0

while nextyear <= 2*current1:
    nextyear = ncurrent * 1.07
    ncurrent = nextyear
    yearcount += 1
  
print("It took", yearcount, "years for tuition to double")
print("The tuition is now", format(ncurrent, ".2f"))"""

#DIsplay 50 prime numbers
count = 0
number = 2
numPerLine = 10

print("The first 50 prime numbers are")

while count < 50:
    prime = True
    div = 2
    while div <= number/2:
        if number % div == 0:
            prime = False
            break
        div += 1
    if prime == True:
        print(format(number, "5d"), end = '')
        count += 1
        if count % numPerLine == 0:
            print()
    number += 1
    