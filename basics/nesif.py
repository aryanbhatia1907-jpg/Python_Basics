x=int(input("Enter a Number:"))
if(x>=100):
    print("Number is 3-Digit or more")
elif(x<100 and x>=0):
    if(x<100 and x>=10):
        print("Number is 2-digit")
    elif(x>0 and x<10):
        print("Number is single digit")
    else: 
        print("Number is 0")
else: 
    print("Number is Negative")                                                                                                                                                                                                                                                                                                                                                                                      