interestRate = eval(input("Hewwo pls put anal rate!"))
loanAmount = eval(input("ok how much u givin' up?"))
numberOfYears = eval(input("ok years how many?!"))

monthlyRate = interestRate / 1200

monthlyPayment = (loanAmount * monthlyRate) / (1 - 1 / (1 + monthlyRate)**(numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

print("You must fork over", int(monthlyPayment * 100) / 100 , "every month")
print("Total loss if you make it out of debt before you die is:", int(totalPayment * 100) / 100) 
