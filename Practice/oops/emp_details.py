class Employee:
    def __init__(self,name,department,salary):
        self.name = name
        self._department = department
        self.__salary = salary

    def get_details(self):
        print(f"Name of Employee: {self.name} || Department: {self._department}")
    
    def get_salary(self):
        return self.__salary
    
    @staticmethod
    def validate_salary(amount):
        if (amount <= 0):   return False
        else:   return True

    @staticmethod
    def company_info():
        print("Company: TechCorp | Est: 2010")

e1 = Employee("Ramu", "Engineering", 50000)
e1.get_details()
print(e1.get_salary())
print(Employee.validate_salary(50000))   # True
print(Employee.validate_salary(-100))    # False
Employee.company_info()