#We will be making a code to calculate the total amount of purchase
#04/03/2019
#CTI-110 P2HW2 - Meal Tip Calculator
#Richard T Buffalo
#


#Get their input with the chargeTotal variable.
chargeTotal = float(input('Enter the amount of meal: '))

#Tie in the variables tip and amount and do your calculations.
tip = chargeTotal * .15
amount = chargeTotal + tip

#Display the amount + tip and format it to two decimals out and float
print('Your total is $ ',format(chargeTotal + tip, '.2f'))

      

chargeTotal = float(input('Enter the amount of meal: '))

tip = chargeTotal * .18
amount = chargeTotal + tip

print('Your total comes out to be $ ',format(chargeTotal + tip, '.2f'))

      
chargeTotal = float(input('Enter the amount of meal: '))

tip = chargeTotal * .20
amount = chargeTotal + tip

print('Wow you really eat alot. I hope you tip for that.. $',format(chargeTotal + tip, '.2f'))

