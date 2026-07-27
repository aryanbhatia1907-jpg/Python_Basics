from random import randint
x=randint(1,100)
count=0
while True:
    y=input("Enter Guess:")
    if(y=="quit"):
        print("Thanks for quitt!")
        break
    y=int(y)
    if (y>x):
        print("High")
        count+=1
    elif(y<x):
        print("Low")
        count+=1

    elif(y==x):
        print("correct!")
        count+=1
        break
print("Completed After",count,"try!")
print("Good! The number is -",x)