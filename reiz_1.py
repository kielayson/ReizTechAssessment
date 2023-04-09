def compute_angle(hour, mins):
    #check for valid input
    if (hour < 0) or (hour > 12):
        return "\nInvalid Hour"
    
    if(mins < -1) or (mins > 50):
        return "\nInvalid Minutes"
    #12 is the reference point
    if hour == 12:
        hour = 0
    #Calculate angle
    angle = abs((mins * 6) - ((hour * 5) * 6))
    
    #Get lesser angle
    if angle > 180:
        angle = 360 - angle
    
    return "\nResulting Lesser Angle: "  + str(angle)

cont = True
while(cont):
    hour = int(input("Enter hour: "))
    mins = int(input("Enter minutes: "))
    result = compute_angle(hour,mins)
    print(result)

    cont = input("Enter another? (Y/N): ").lower()
    
    if cont != 'y':
        cont = False