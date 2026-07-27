class employee:
    company="Apple"
    def show(self):
        print(f"The Employee Name is {self.name} and company is {self.company}")

    @classmethod                        # classmethod mein decorator laga ke yeh agle fn ki class change kar rha by using 'cls' , Bydefault Instance change hota issliye isske hatane se company name change nahi hota 
    def changecompany(cls ,newCompany):
        cls.company=newCompany
        

a=employee()
a.name="Python"
a.show()
a.changecompany("Tesla")
a.show()
print(employee.company)        # yeh bata raha hai ki kon si company name hai class mein
