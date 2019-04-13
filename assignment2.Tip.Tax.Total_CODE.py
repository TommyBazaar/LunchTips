#
# CTI-110 
# P3HW2 - MealTipTax 
# Richard Buffalo
# 4/11/19


#My variables
Charge = float(input("Please enter the cost of your food: " ))
tax= 0.07
mealTax = totalCost + Charge
totalCost = Charge + tax


print("The cost of meal with tax is: " +str(mealtax))

tipPercent = int(input("How generous are you feeling in percent?\n1. 15%\n2. 18%\n3. 20%"))
                    
if  tipPercent == 1:
    totalAmount = totalCost * 0.15
    totaltoCustomer = mealTax + totalAmount
    print("The 15% tip for a " +str(mealTax) +"dollar meal is: "+str(totalAmount))
    print("The grand total is " +str(totaltoCustomer))

elif tipPercent == 2:
     totalAmount = totalCost * 0.18
     totaltoCustomer = mealTax + totalAmount
     print("The 18% tip for a " +str(mealTax) +"dollar meal is: "+str(totalAmount))
     print("The grand total is " +str(totaltoCustomer))

else:
     totalAmount = totalCost * 0.20
     totaltoCustomer = mealTax + totalAmount
     print("The 20% tip for a " +str(mealTax) +"dollar meal is: "+str(totalAmount))
     print("The grand total is " +str(totaltoCustomer))                   
                   



loop()

