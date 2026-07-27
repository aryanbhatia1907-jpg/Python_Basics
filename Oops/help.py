# dir Method
x=[1,2,4,6]
print(dir(x))
print(x.__add__)
# yeh batata hai ki x ke andar kon se methods hote hai  
print("\n")

# dict Method
class person:
    def __init__(self,name,age,version):
        self.name=name
        self.age=age
        self.version=version

p=person("John",21,1)
print(p.__dict__)
# class ke andar jitne bhi attributes hai sab dictionary ki form mein mil jayenge 
print("\n")

# Help Method
print(help(person))