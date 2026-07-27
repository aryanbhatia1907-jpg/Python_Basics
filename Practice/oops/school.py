class Student:
    school_name = "Delhi Public School" 
    total_students = 0 
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 
        Student.total_students += 1 


    def get_info(self):
        print(f"Name: {self.name}  | Marks: {self.marks} | School: ",Student.school_name)
        

    @classmethod 
    def change_school(cls, new_name):
        cls.school_name = new_name
    @classmethod 
    def get_count(cls):
        return cls.total_students

s1 = Student("Ramu", 85)
s2 = Student("Shyam", 92)
s3 = Student("Geeta", 78)
s1.get_info()
print(Student.get_count()) 

Student.change_school("Modern School")
s2.get_info()                     # school naam badal gaya!
print(Student.total_students)