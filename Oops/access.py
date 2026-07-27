class employee:
    def __init__(self):
        self.__name="Python"

a=employee()
# print(a.__name)          # __" lagane se yeh public se private ho gya h or ab isse directly access nhi kar skte
print(a._employee__name)   # but indiectly ess tarike se access kara jaa sakta hai [Name Mangling]
print(a.__dir__())         # Shows all methods


class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName()) 