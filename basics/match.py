x=int(input("Enter the value of X"))
match x:
    case _ if (x==10):
        print("x is in case 1")
    case _ if(x>0):
        print(x,"is Greater than 0")
    case _:
        print("Default Case")

        # Match case is a type of Switch Case in Python 
        # _ means Default Case in this.
        # Match case checks Condition from Top to BOttom.