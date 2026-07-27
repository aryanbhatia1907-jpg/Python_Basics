names = "Aryan,Anchal,fwo"
print(names[6:12])
print(len(names))
print("")

# Some length SLicing
fruit="Mango"
print(fruit[0:4])  # 0 means 1st Index and 4 means 3rd Index or Total 4 Characters
print(fruit[1:3])
print(fruit[0:-3]) # -3 means len(fruit) i.e 5 - 3 = 2 .'. This prints [0:2]
print(fruit[:])    # This automatically Takes 0 and total length of character 
print(fruit[-3:3]) # Follows same Logic as ln 10
print(fruit[::-1]) # Reverse string
# string[start : end : step]