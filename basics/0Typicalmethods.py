# _~_ kon si problem solutions

i="45"
# print(i+4)        # Not work because 45 is str
i=int(i)
print(i+4,"~1")


# Convert int into list 
num=45
print(type(num),"~2")
num=[num]
print(type(num),"~3")        # But can't do with tuple


# Access every list elements
list=[1,2,3,4,5,6]
for x in list:
    print(x,"~4") 


# List se kuch specific type ke numbers lena

def even(numbers):
    result=[]                       # Important step 1
    for i in numbers:               # Important step 2
        if i%2==0:
            result.append(i)        # Important step 3
    return result
print(even([1,2,3,4,5,6,7,8]),"~5")


# To sum the values of fn
def fn(n):
    if n==0:
        return 0
    return (n%10)+fn(n//10)
print(fn(1234),"~6")


# Adding List Elements Using Recursion
def sum_list(arr):
    # Base case: empty list
    if len(arr) == 0:
        return 0
    
    # Recursive case: first element + sum of rest
    return arr[0] + sum_list(arr[1:])

numbers = [1, 2, 3, 4, 5]
print(sum_list(numbers),"~7")  # 15


students = {'Ramu': 85, 'Shyam': 92, 'Geeta': 78} # Loop keys only for name in
print(students.items(),"~8") 
for name,marks in students.items(): 
    print(f'{name} scored {marks}',"~8") 


# List ke andar tuple mein marks diye hue hai unn marks ke hisaab se names ko descending order mein print karo
pythonstudents = [("Ramu", 85), ("Shyam", 92), ("Geeta", 78), ("Mohan", 95)]
sorted_students = sorted(pythonstudents, key=lambda x: x[1], reverse=True)
print(sorted_students,"~9")


# dict to string method by classes [10]

class Pizza:
    def __init__(self,name,size,price):
        self.name =name
        self.size = size
        self.price = price
    
    @classmethod
    def from_dict(cls, pizza_dict):
        return cls(pizza_dict["name"], pizza_dict["size"], pizza_dict["price"])
    
    def __str__(self):
        return f"Pizza: {self.name} | Size: {self.size} | Price: Rs.{self.price}    ~10"

p3 = Pizza.from_dict({"name": "Pepperoni", "size": "Small", "price": 199},)

print(p3)
