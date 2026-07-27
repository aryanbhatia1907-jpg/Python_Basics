a=[2,3]
b=[2,3]

print( a is b)      # Exact location of one object in the memory
print( a == b)      # Check Values

# Is or "==" ke values immutable yaa jo change naa ho ske or same ho toh True dega (eg. Int,str,tuple) otherwise agar list ho toh "==" True dega if values same ho lekin Is nahi, if both different then False