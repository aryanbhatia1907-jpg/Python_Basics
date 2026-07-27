# default argument
def name(fname, mname = "Jhon", lname = "Whatson"): # Here fn takes default value even if value not provided
    print("Hello,", fname, mname, lname)
name("Amy")
# Keyword Argument mein last mein name define karna hai usme default me nhi hoga
# Required Argument mein all argument  pass hone chahiye agar nahi ho pate toh wo "Type Error" dega

# Variable arbitary
def name(*name):
    print("Hello,", name[0], name[1], name[2])
name("James", "Buchanan", "Barnes")
# * using star symbol tuple is created & using ** argument act as dictionary

def avg(*num):
    sum=0
    for i in num:
        sum=sum+i
    print("Avg is",sum/len(num))
avg(7,10)



# Return Statement
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
print(name("James", "Buchanan", "Barnes"))

def avg(*num):
    sum=0
    for i in num:
        sum=sum+i
    return sum/len(num)
c= avg(7,10)
print(c, "~ Avg Return karke print kara yahan")



