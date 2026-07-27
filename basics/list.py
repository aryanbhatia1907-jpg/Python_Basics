l=[1,2,3,4,"Python"]
print(l)
print(type(l)) 
print(l[0])      #Here Index of [1] is *0*
print(l[-2])     #Negative Index { len(l)-2 = Index } , len = Index + 1 

if 3 in l:
    print("Yess")
else:
    print("Noo")
# Same thing applied for String!!
if "pOy" in "python":
    print("Yess")

k=[11,12,13,14,15,16,17,18,19]
print(k[:])
print(k[2:8])      #Same Concept as String Slicing
print(k[2:8:2])    #Jump Index
print("\n")

#List Comprehension 
lst=[i*i for i in range(10)]
print(lst)
lst=[i*i for i in range(10) if i%2==0]
print(lst)