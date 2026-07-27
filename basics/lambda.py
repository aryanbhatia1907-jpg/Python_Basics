# def double(x):
#     return x*x   # yeh karne ke bajaye lambda fn ko use karke bhi kara jaa sakta hai

def appl(fx, value):
    return 6 + fx(value)   # yahan pe fn as a argument pass kara jaa rha hai
 
double = lambda x:x*x
avg = lambda x,y : (x+y)/2
print(double(5))
print(avg(5,3))
print(appl(lambda x: x*x , 2))