x=int(input("Enter Your Age:"))
print("Your Age is \"",x,"\"")
if(x>18):
    print("You can Drive")
elif(x==18):
    print("Make Licence then Drive")
else:
    print("You Can't Drive")
print("\"This is outside from if-else Indentation ,So it prints everytime\"")

# Conditional Operator [>,<,>=,<=,==,!=]
print(x>18)
print(x>=18)
print(x<18)
print(x<=18)
print(x==18)
print(x!=18)


# Shorthand If-Else

a=224
b=24
print("A") if a>b else print("B") if a<b else print ("=")
#  ~Syntax:  result = value_if_true if condition else value_if_false
c= 9 if a>b else ""
print(c)    # By using variable