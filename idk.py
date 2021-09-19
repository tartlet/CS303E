import random

number = random.randint(0,100)
userinput = eval(input("Enter your guess: "))

while userinput != number:
	if userinput > number:
		print("Your guess is too high")
	if userinput < number:
		print("Your guess is too low")
	userinput = eval(input("Enter your guess: "))
        
print("Yes the number is", number)