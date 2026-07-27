l=[11,48,45,5,4,1,2,3,1,1,1]
print(l,"Original")

l.reverse()
# To Reverse the Original List 
print(l,"Reverse")

l.append(99)
# To add one more int/str at the end of the List 
print(l,"Append")

l.sort()
# To Sort List in the Ascending Order
print(l,"Sort-A")

l.sort(reverse=True)
# To Sort List in the Decending Order
print(l,"Sort-D")

print(l.index(48),"is the Index of Number")

print(l.count(1),"Count")

m=l        # if you use "l.copy" instead of "l" , so there will no change in "l"
m[0]=111   # yahan pe humne "m" new variable leke l ke barabar kar or "m" mein change kar diya to woh change "l" mein bi ho gya 
print(l,"Copy")

l.insert(3,786)    # 3 = Index ,, 786 = Value
# To insert new value to the Index.
print(l,"Insert")

n=[900,1000,1100]
l.extend(n)
# isko karne se "n" ki joh bi list hogi woh "l" ke end mein chali jayegi
print(l,"Extend")

k=l+n  # Concatenation
# isme 3rd variable leke dono ki value ko concatenate kar skate hai
print(k,"Concatenation")