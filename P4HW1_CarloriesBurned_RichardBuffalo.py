# A brief description of the project
# 04/16/19
# CTI-110 P4HW1 - Calories Burned
# Richard Buffalo
#



#This treadmill burns 5 calories/ per minute. 
#We need to find how many calories will be burned after 20,35,45 minutes.
#if 5 minute =  25 calories

caloriesBurnedperminute = 5

for nOm in range(20 ,45 , 5):
    numberOfCaloriesBurned = nOm * caloriesBurnedperminute
    print("You will burn", numberOfCaloriesBurned ,"in", nOm)
