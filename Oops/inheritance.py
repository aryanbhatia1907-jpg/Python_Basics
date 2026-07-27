class employee:
    def __init__(self,emp_name,emp_id):
        self.emp_name=emp_name
        self.emp_id=emp_id

    def show_case(self):
        print(f"The Name of Employee: {self.emp_id} is {self.emp_name}")

class Programmer(employee):
    def show(self):
        print("The Default Language is Python")


e=(Programmer("RAhul",420))
e.show_case()                   # Employee ka fn
e.show()                        # Programmer ka fn
# e1=(employee("Rohan",421))      # Throws error because employee didn't have access toh show fn (only Programmer has)
# e1.show()                   
    
# Yahan pe Inheritance ka mtlb hai ki ek "employee" class banayi hai jisme fn banaya hai or id liya or dusre fn showcase jisme print karne ke liye statement banayi hai , 
# ,,ab hume agar class ka name change karna hai toh woh inheritance method se karna hoga, ab iss se employee ke saare fn Programmer mein chale gaye (but programmer ke fn ko employee me nahi chala sakte)