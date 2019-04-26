# CTI-110 
# P3HW1 - Color Mixer 
# Richard Buffalo
# 4/10/19
#



color1 = input("Please enter color1: ")
color2 = input("Please enter color2: ")





if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    print("Your color is purple")

elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    print("Your color is orange")

elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
    print("Your color is green")



else:

    print("Error")
    
