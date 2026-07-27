# Union of sets
s1={1,3,4,5,7}
s2={2,4,6,7,8}
print(s1.union(s2))
s2.update(s1)
print(s1,s2,"Updated s2\n")
# Intersection of sets
s1={"Tokyo","Madrid","Berlin","Delhi"}
s2={"Tokyo","Seoul","Kabul","Madrid"}
print(s1.intersection(s2))    # Dono sets mein se common terms .
s1.intersection_update(s2)    # 1st set mein jo common h woh hi honge baki ke nhi
print(s1,"~intersection above & this\n")

# Isme common wale nhi lene , different wali values leni hai.
s1={"Tokyo","Madrid","Berlin","Delhi"}
s2={"Tokyo","Seoul","Kabul","Madrid"}
s=s1.symmetric_difference(s2)
print(s,"~sym. diff")

s=s1.difference(s2)   # print usko karna original/1st set mein  jo common nahi ho
print(s,"~difference\n") 

print(s1.isdisjoint(s2))    # Disjoint sets mein koi bhi common term nhi hota h... , yahan common h to false aa rha

print(s1.issuperset(s2))    # s1 ko s2 ka superset bann ne ke liye s2 ke sare element apne pass rakhne honge..
print(s2.issubset(s1))      # agar upar ki condition true ho to yeh bi true hogi

s1.add("Helsinki")
print("\n",s1,"~add")

s1.remove("Delhi")
print(s1,"~remove")
# if you want to delete any value that is not present so use "discard" method instead of "remove" ,, because remove raise error for value that are not present but dicard can't.

p=s1.pop()
print("\n",p,"~Item popped")
print(s1,"~Rest of the string\n")

del(s2)    # After this set will deleted and you can't print it , it will give "Name Error".
# print(s2)

s1.clear()   # if we want to clear only elements not the set so clear method is used.