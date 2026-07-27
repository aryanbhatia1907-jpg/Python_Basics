tup=(1,2,3,4,55,77,"Tuple",2,3,2,4)
print(type(tup),tup,len(tup))
# If single value of tuple is used , Comma must be used {tup=(1,)} , otherwise it will define type as integer

# tup[0]=99 ***
# tuple can't be changed later as list

print(tup[0])
print(tup[6])

if 55 in tup:
    print("Yes 55 is Present")

print(tup[1:6:2],"Slicing")

c=tup.count(2)
# Count total number of defined Variable
print(c,"count")

c=tup.index(2)
# Show first index of Number , not others 
print(c,"Index")

c=tup.index(2, 6,10)
# Here specific part of index is choosed, 2 is the number and 6-10 is the Index Range
print(c,"spc.Index")

# Manipulating Tuples
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

