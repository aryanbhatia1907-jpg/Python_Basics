# This is Common method to find cube of numbers in list.
def cube(x):
    return x*x*x
l=[1,2,3,4,6,8]

newl=[]
for items in l:
    newl.append(cube(items))

# MAP
# This can be done in single Line By Map Object

# newl=list(map(cube,l))             # Can also be return as tuple*   Syntax :- map(fn.Name, list)

print(newl)

# FILTER
def fn_fil(a):
    return a>3
# Filter ke liye fn bata ke usse bata diya ki return kya phir filter m woh fn daal ke list de di

nowl= tuple(filter(fn_fil, l))
print(nowl)

# REDUCE
from functools import reduce   
# Without Import Reduce fn doesn't works

numbers = [1, 2, 3, 4, 5]
# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)       # yahan pe yeh numbers se pheli do values le rha hai or unhe reduce kar rha hai single value mein by using fn/lambda fn , Yeh process repeat ho rhi hai
# Print the sum
print(sum)