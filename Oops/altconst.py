class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    # Alternative Constructor
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    
e1=Employee("Rahul",12000)
print(e1.name)
print(e1.salary)

# This method is use if we have string form data , toh hume split ka use karke usse alag karna hai phir indexing se le lena hai 
string="Rohan-14000"
# e2=Employee(string.split("-")[0],string.split("-")[1])      # This is correct but you have to do multiple time
e2=Employee.fromstr(string)                                 # This is convenient method and can be done above as alternative constructor
print(e2.name)
print(e2.salary)