import math             # yahan pe math module ko import kar rhe h 
result = math.sqrt(9)

# From keyword ka use karke math module ko laa ke uske specific fn ko use kar sakte hai 
from math import sqrt,pi
result = sqrt(9)

# It's also possible to import all functions and variables from a module using the * 
from math import *
result = sqrt(9)

# As Keyword ka use karke Module ka Name change kar sakte hai
import math as m
result = m.sqrt(9)

print(result)

# dir keyword woh sab fn print kar dega jo math module ke andar hai 
import math

print(dir(math))
print(math.nan ,type(math.nan))

from namefn import hello,namefn
hello()
print(namefn)


from random import randint      # randint function used to import random number b/w two..
x=randint(1,100)
print(x)

# value of pi after rounded off to 4 digits
print(f"{math.pi:.4f}")

