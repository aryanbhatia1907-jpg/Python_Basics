f="Hey my name is {} and i am form {}"
country="India"
name=str(input("Enter Your Name: "))
# Old method of doing this type is it ,, but this create problemif using like this
print(f.format(country,name))
# New Method by using "f-String" 
print(f"Hey my name is {name} and i am form {country}")
print(f"We Use f-string like this:Hey my name is {{name}} and i am form {{country}}")

price=3.142857
txt=f"Value of pi is {price:.2f}"
print(txt)

print(f"{2*30}")       # Here the value is in the type of string ,, This is used to create value as an string
