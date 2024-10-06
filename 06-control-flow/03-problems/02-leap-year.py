def utility():
    #The line below takes input
    y= int(input("Enter a year: "))
    isLeap=False
    #Assign True or False to isLeap
    if y%4==0 and y%100!=0:
        isLeap = True
    elif y%400==0:
        isLeap = True
    print(isLeap)
    
    
    
utility()