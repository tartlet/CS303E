import time 

currentTime = time.time()

totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
currentMinute = totalSeconds // 60 % 60

# total seconds divided by 60 is minutes... divided by 60 is hours...
# one day is 24 hours 

currentHour = totalSeconds // 3600 % 24

print("Current time is", currentHour, ":", currentMinute, ":", currentSecond)


enter interest rate, loan amnt, number of years
compute monthly and total payment


