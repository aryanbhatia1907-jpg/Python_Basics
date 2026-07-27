a="1"
b="23"
print(a+b)  #WHy it wouldn't add these numbers ,because of Typecasting , here we declared these nos. as string not as int
# for Integer
print("The Sum is", int(a)+int(b))

# Now taking User Input
x=input("Enter")
print("My Name is",x)

# add numbers using input from user 
m=input("Enter 1st Number")
n=input("Enter 2nd Number")      
print(int(m)+int(n))

u=12
v=11.33
p=u*v
print(p)
print(type(u),type(v),type(p))