# OOP Problems — Hinglish Mein Samjho 🐍
### Beginner se Master tak — 10 Problems

---

> **Kaise use karo ye file:**
> - Pehle problem padho
> - Khud try karo — kam se kam 15 min
> - Phir hint dekho
> - Phir solution dekho aur samjho
> - **Solution copy mat karo — khud likho!**

---

## Topics Covered:
| Problem | Topics |
|---------|--------|
| 1 | Classes, Objects, `__init__`, `self` |
| 2 | Instance vs Class Variables, Class Methods |
| 3 | Getters, Setters, `@property` |
| 4 | Access Modifiers — Public, Protected, Private |
| 5 | Static Methods, Class Methods, Alternative Constructors |
| 6 | Magic/Dunder Methods |
| 7 | Single + Multilevel Inheritance, `super()` |
| 8 | Multiple + Hierarchical Inheritance, MRO |
| 9 | Method Overriding, Operator Overloading |
| 10 | `dir()`, `__dict__`, `__slots__`, Full OOP Project |

---

---

# Problem 1 — Bank Account 🏦
### Topics: Classes, Objects, `__init__`, `self`, Instance Variables

---

### Simple bhasha mein kya hai OOP?

Socho tumhare paas ek **blueprint** hai ek ghar ka.
Us blueprint se tum hazaron ghar bana sakte ho — har ghar alag hoga lekin structure same.

```
Blueprint  →  Class
Ghar       →  Object (instance)
Rooms      →  Variables (attributes)
Kaam       →  Methods (functions inside class)
```

---

### Problem:

Ek `BankAccount` class banao jisme:

**Attributes (`__init__` mein):**
- `owner` — account holder ka naam
- `balance` — starting balance (default 0)

**Methods:**
- `deposit(amount)` — paisa add karo, print karo `"Rs.500 deposited. New balance: Rs.1500"`
- `withdraw(amount)` — paisa nikalo, lekin agar balance kam ho toh print karo `"Insufficient balance!"`
- `get_balance()` — current balance return karo

**Test karo:**
```python
acc1 = BankAccount("Ramu", 1000)
acc2 = BankAccount("Shyam")       # balance 0 se start hoga

acc1.deposit(500)                  # Rs.500 deposited. New balance: Rs.1500
acc1.withdraw(200)                 # Rs.200 withdrawn. New balance: Rs.1300
acc1.withdraw(5000)                # Insufficient balance!
print(acc1.get_balance())          # 1300
print(acc2.get_balance())          # 0
```

---

### Concepts Explained — Hinglish mein:

**`class` kya hai?**
```python
class BankAccount:
    # Ye ek blueprint hai
    # Ye khud kuch nahi karta
    # Jab object banate hain TAB kaam shuru hota hai
```

**`__init__` kya hai?**
```python
def __init__(self, owner, balance=0):
    # Ye constructor hai
    # Jab bhi naya object banta hai YE AUTOMATICALLY CHALTA HAI
    # balance=0 matlab default value — dena zaroori nahi
```

**`self` kya hai?**
```python
# self = "mera apna"
# self.balance matlab "IS object ka balance"
# Agar self nahi likha toh Python nahi jaanegi
# ki kaunse object ki baat kar rahe ho!

acc1.deposit(500)
# Yahan Python automatically self = acc1 kar deta hai
# Tumhe pass nahi karna — Python khud karta hai!
```

**Object kaise banta hai?**
```python
acc1 = BankAccount("Ramu", 1000)
#                   ^^^^   ^^^^
#                   owner  balance
# __init__ automatically call hota hai yahan!
```

---

### Hints:
- `__init__` mein `self.owner = owner` aur `self.balance = balance` likhna mat bhoolna
- `withdraw` mein pehle check karo `if amount > self.balance`
- Default parameter: `def __init__(self, owner, balance=0)`

---

### Solution:

```python
class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner        # har object ka apna naam
        self.balance = balance    # har object ka apna balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} deposited. New balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn. New balance: Rs.{self.balance}")

    def get_balance(self):
        return self.balance


# Objects banana
acc1 = BankAccount("Ramu", 1000)
acc2 = BankAccount("Shyam")        # balance = 0 (default)

acc1.deposit(500)
acc1.withdraw(200)
acc1.withdraw(5000)
print(acc1.get_balance())
print(acc2.get_balance())
```

### Output:
```
Rs.500 deposited. New balance: Rs.1500
Rs.200 withdrawn. New balance: Rs.1300
Insufficient balance!
1300
0
```

---

---

# Problem 2 — Student Counter 📊
### Topics: Instance Variables vs Class Variables, `@classmethod`, `cls`

---

### Instance vs Class Variable kya hai?

```
Instance Variable  →  Har object ka APNA alag variable
                       self.name, self.marks etc

Class Variable     →  SABHI objects ka SHARED variable
                       ek jagah change hua — sabko dikhta hai
```

Real life example:
```
Class Variable   →  School ka naam (sab students ka same!)
Instance Variable →  Student ka naam (har student ka alag!)
```

---

### Problem:

Ek `Student` class banao jisme:

**Class Variable:**
- `school_name = "Delhi Public School"` — sab students ka same
- `total_students = 0` — har naya student bante waqt +1 ho

**Instance Variables (`__init__` mein):**
- `name`, `marks`

**Methods:**
- `get_info()` — print karo `"Name: Ramu | Marks: 85 | School: Delhi Public School"`
- `@classmethod change_school(cls, new_name)` — school ka naam badlo
- `@classmethod get_count(cls)` — total students return karo

**Test karo:**
```python
s1 = Student("Ramu", 85)
s2 = Student("Shyam", 92)
s3 = Student("Geeta", 78)

s1.get_info()
print(Student.get_count())        # 3

Student.change_school("Modern School")
s2.get_info()                     # school naam badal gaya!
print(Student.total_students)     # 3
```

---

### Concepts Explained — Hinglish mein:

**Class Variable — kahan likhte hain?**
```python
class Student:
    school_name = "Delhi Public School"   # class ke andar, __init__ ke bahar!
    total_students = 0                    # ye sab objects share karte hain
```

**`__init__` mein `total_students` kaise badhao?**
```python
def __init__(self, name, marks):
    self.name = name
    self.marks = marks
    Student.total_students += 1    # class variable access karna — Student.variable
    # self.total_students nahi — Student.total_students!
```

**`@classmethod` kya hai?**
```python
@classmethod
def change_school(cls, new_name):
    # cls = class itself (self ki tarah lekin class ke liye)
    # cls.school_name change kiya toh sabka badlega!
    cls.school_name = new_name
```

**`self` vs `cls`:**
```
self  →  specific object ke liye  (acc1, acc2, s1, s2)
cls   →  poori class ke liye      (Student, BankAccount)
```

---

### Hints:
- `total_students` ko `__init__` mein `Student.total_students += 1` se badhao
- `@classmethod` mein first parameter hamesha `cls` hota hai — `self` nahi!
- Class variable access: `Student.school_name` ya `cls.school_name`

---

### Solution:

```python
class Student:
    school_name = "Delhi Public School"   # class variable
    total_students = 0                    # class variable

    def __init__(self, name, marks):
        self.name = name                  # instance variable
        self.marks = marks                # instance variable
        Student.total_students += 1       # har naya object bane toh +1

    def get_info(self):
        print(f"Name: {self.name} | Marks: {self.marks} | School: {Student.school_name}")

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name        # sabka school badlega!

    @classmethod
    def get_count(cls):
        return cls.total_students


s1 = Student("Ramu", 85)
s2 = Student("Shyam", 92)
s3 = Student("Geeta", 78)

s1.get_info()
print(Student.get_count())

Student.change_school("Modern School")
s2.get_info()
print(Student.total_students)
```

### Output:
```
Name: Ramu | Marks: 85 | School: Delhi Public School
3
Name: Shyam | Marks: 92 | School: Modern School
3
```

---

---

# Problem 3 — Temperature Converter 🌡️
### Topics: `@property`, Getters, Setters, Validation

---

### `@property` kyun chahiye?

Bina property ke problem:
```python
temp.celsius = -5000    # koi nahi rokta! galat value set ho gayi
```

Property ke saath:
```python
temp.celsius = -5000    # Error! "Temperature -273 se kam nahi ho sakti!"
```

Property = **security guard** jo values check karta hai set hone se pehle!

---

### Problem:

Ek `Temperature` class banao jisme:

**`__init__`:**
- `self.__celsius` — private variable (double underscore!)

**Properties:**
- `@property celsius` — getter — current temp return karo
- `@celsius.setter` — validation ke saath set karo:
  - `-273` se kam nahi ho sakti (absolute zero!)
  - Agar galat value: `raise ValueError("Temperature cannot go below -273!")`
- `@property fahrenheit` — celsius se fahrenheit calculate karke return karo (read only!)

**Test karo:**
```python
t = Temperature(25)
print(t.celsius)       # 25
print(t.fahrenheit)    # 77.0

t.celsius = 100
print(t.fahrenheit)    # 212.0

t.celsius = -300       # ValueError!
```

---

### Concepts Explained — Hinglish mein:

**Private variable kya hai?**
```python
self.__celsius = value
# Double underscore = private
# Matlab: seedha access karna allowed nahi!
# t.__celsius  →  AttributeError!
# Sirf class ke andar access kar sakte ho
```

**`@property` getter:**
```python
@property
def celsius(self):
    return self.__celsius
# Ab t.celsius likhne se ye function chalta hai
# Brackets nahi lagte — t.celsius() nahi, sirf t.celsius!
```

**`@celsius.setter`:**
```python
@celsius.setter
def celsius(self, value):
    if value < -273:
        raise ValueError("Too cold!")
    self.__celsius = value
# Ab t.celsius = 25 likhne se ye function chalta hai
```

**Read-only property:**
```python
@property
def fahrenheit(self):
    return (self.__celsius * 1.8) + 32
# Sirf getter — koi setter nahi
# t.fahrenheit = 100 karna → AttributeError!
```

---

### Hints:
- Private variable: `self.__celsius` (double underscore)
- Formula: `fahrenheit = (celsius * 1.8) + 32`
- `raise ValueError("message")` — custom error uthao
- `@property` ke baad setter ke liye `@celsius.setter` likhte hain

---

### Solution:

```python
class Temperature:

    def __init__(self, celsius):
        self.__celsius = celsius    # private — seedha access nahi

    @property
    def celsius(self):              # getter
        return self.__celsius

    @celsius.setter
    def celsius(self, value):       # setter with validation
        if value < -273:
            raise ValueError("Temperature cannot go below -273!")
        self.__celsius = value

    @property
    def fahrenheit(self):           # read-only property
        return (self.__celsius * 1.8) + 32


t = Temperature(25)
print(t.celsius)        # 25
print(t.fahrenheit)     # 77.0

t.celsius = 100
print(t.fahrenheit)     # 212.0

try:
    t.celsius = -300    # ValueError!
except ValueError as e:
    print(e)
```

### Output:
```
25
77.0
212.0
Temperature cannot go below -273!
```

---

---

# Problem 4 — Employee System 👔
### Topics: Access Modifiers, Static Methods, `@staticmethod`

---

### Access Modifiers — Teen levels:

```
public    →  self.name        — sabke liye accessible
protected →  self._salary     — ek underscore — "please seedha mat use karo"
private   →  self.__password  — double underscore — strictly andar ka kaam
```

Real life:
```
public    →  Employee ka naam   (sabko pata)
protected →  Salary             (sirf HR ko pata)
private   →  Password           (sirf employee ko pata)
```

---

### Problem:

Ek `Employee` class banao:

**Attributes:**
- `self.name` — public
- `self._department` — protected
- `self.__salary` — private

**Methods:**
- `get_details()` — name aur department print karo
- `get_salary()` — salary return karo (private ko access karna!)
- `@staticmethod validate_salary(amount)` — agar 0 se kam ho toh `False` return karo, warna `True`
- `@staticmethod company_info()` — print karo `"Company: TechCorp | Est: 2010"`

**Test karo:**
```python
e1 = Employee("Ramu", "Engineering", 50000)
e1.get_details()
print(e1.get_salary())
print(Employee.validate_salary(50000))   # True
print(Employee.validate_salary(-100))    # False
Employee.company_info()
```

---

### Concepts Explained — Hinglish mein:

**Protected `_salary`:**
```python
self._department = department
# Convention hai — Python strictly nahi rokta
# Matlab: "Bhai seedha mat use karo please"
# Bahar se access hota hai lekin "should not" karna chahiye
```

**Private `__salary`:**
```python
self.__salary = salary
# Python iska naam badal deta hai internally:
# __salary → _Employee__salary
# Isliye bahar se e1.__salary → AttributeError!
# Sirf class ke andar self.__salary se access hota hai
```

**`@staticmethod` kya hai?**
```python
@staticmethod
def validate_salary(amount):
    # self bhi nahi, cls bhi nahi!
    # Class ya object se koi lena dena nahi
    # Ek standalone utility function hai
    # Class ke naam se call karte hain: Employee.validate_salary(100)
```

**`@staticmethod` vs `@classmethod`:**
```
@staticmethod  →  na self, na cls — bilkul independent function
@classmethod   →  cls milta hai — class variables access kar sakta hai
```

---

### Hints:
- Private access karne ke liye class ke andar `self.__salary` use karo
- Static method mein koi bhi parameter nahi hota unless tum khud do
- `Employee.company_info()` — object bina bhi call hota hai!

---

### Solution:

```python
class Employee:

    def __init__(self, name, department, salary):
        self.name = name                    # public
        self._department = department       # protected
        self.__salary = salary              # private

    def get_details(self):
        print(f"Name: {self.name} | Department: {self._department}")

    def get_salary(self):
        return self.__salary                # private ko andar se access karo

    @staticmethod
    def validate_salary(amount):
        return amount > 0                   # True ya False

    @staticmethod
    def company_info():
        print("Company: TechCorp | Est: 2010")


e1 = Employee("Ramu", "Engineering", 50000)
e1.get_details()
print(e1.get_salary())
print(Employee.validate_salary(50000))
print(Employee.validate_salary(-100))
Employee.company_info()

# Private access try karo — error aayega!
# print(e1.__salary)   # AttributeError!
```

### Output:
```
Name: Ramu | Department: Engineering
50000
True
False
Company: TechCorp | Est: 2010
```

---

---

# Problem 5 — Pizza Shop 🍕
### Topics: Alternative Constructors, `@classmethod`, `__str__`

---

### Alternative Constructor kya hai?

Normal constructor:
```python
pizza = Pizza("Margherita", "Medium", 250)
```

Alternative constructor — alag tarike se banana:
```python
pizza = Pizza.from_string("Margherita-Medium-250")  # string se
pizza = Pizza.from_dict({"name": "Margherita", ...}) # dict se
```

Real life: Date object banana — ya direct date do, ya string "2024-01-15" do, ya timestamp do. Teen alag tarike — teen constructors!

---

### Problem:

Ek `Pizza` class banao:

**`__init__`:**
- `name`, `size`, `price`

**Alternative Constructors (`@classmethod`):**
- `from_string(cls, pizza_str)` — `"Margherita-Medium-250"` string se object banao
- `from_dict(cls, pizza_dict)` — `{"name": "Margherita", "size": "Medium", "price": 250}` dict se banao

**`__str__` method:**
- Return karo: `"Pizza: Margherita | Size: Medium | Price: Rs.250"`

**Test karo:**
```python
p1 = Pizza("Farmhouse", "Large", 350)
p2 = Pizza.from_string("Margherita-Medium-250")
p3 = Pizza.from_dict({"name": "Pepperoni", "size": "Small", "price": 199})

print(p1)    # __str__ automatically call hoga!
print(p2)
print(p3)
```

---

### Concepts Explained — Hinglish mein:

**Alternative constructor kyun?**
```python
# Kabhi string milti hai:
"Margherita-Medium-250"

# Kabhi dict milti hai:
{"name": "Margherita", "size": "Medium", "price": 250}

# Dono se object banana chahte ho — isliye alternative constructors!
```

**`from_string` kaise kaam karega:**
```python
@classmethod
def from_string(cls, pizza_str):
    # "Margherita-Medium-250" ko split karo "-" pe
    # ["Margherita", "Medium", "250"] milega
    # cls(...) se object banao — Pizza(...) ki tarah!
    parts = pizza_str.split("-")
    return cls(parts[0], parts[1], int(parts[2]))
```

**`__str__` kya hai?**
```python
def __str__(self):
    return f"Pizza: {self.name} | Size: {self.size} | Price: Rs.{self.price}"
# Jab bhi print(object) karo — ye automatically call hota hai!
# Bina __str__ ke: <__main__.Pizza object at 0x...> aata — useless!
```

---

### Hints:
- `split("-")` use karo string todne ke liye
- `cls(...)` aur `Pizza(...)` same kaam karta hai — `cls` better practice hai
- `from_dict` mein `pizza_dict["name"]` se values nikalo
- `__str__` mein `return` karo — `print` mat karo!

---

### Solution:

```python
class Pizza:

    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    @classmethod
    def from_string(cls, pizza_str):
        parts = pizza_str.split("-")
        return cls(parts[0], parts[1], int(parts[2]))

    @classmethod
    def from_dict(cls, pizza_dict):
        return cls(pizza_dict["name"], pizza_dict["size"], pizza_dict["price"])

    def __str__(self):
        return f"Pizza: {self.name} | Size: {self.size} | Price: Rs.{self.price}"


p1 = Pizza("Farmhouse", "Large", 350)
p2 = Pizza.from_string("Margherita-Medium-250")
p3 = Pizza.from_dict({"name": "Pepperoni", "size": "Small", "price": 199})

print(p1)
print(p2)
print(p3)
```

### Output:
```
Pizza: Farmhouse | Size: Large | Price: Rs.350
Pizza: Margherita | Size: Medium | Price: Rs.250
Pizza: Pepperoni | Size: Small | Price: Rs.199
```

---

---

# Problem 6 — Magic Shopping Cart 🛒
### Topics: Dunder/Magic Methods — `__init__`, `__str__`, `__len__`, `__add__`, `__contains__`

---

### Dunder Methods kya hain?

```
Dunder = Double UNDERscore
__init__, __str__, __len__, __add__ etc

Ye methods Python automatically call karta hai
jab tum kuch specific kaam karte ho:

print(obj)      →   __str__ call hota hai
len(obj)        →   __len__ call hota hai
obj1 + obj2     →   __add__ call hota hai
"item" in obj   →   __contains__ call hota hai
```

---

### Problem:

Ek `ShoppingCart` class banao:

**`__init__`:** empty `items` list

**Dunder Methods:**
- `__str__` — `"Cart has 3 items: Apple, Bread, Milk"`
- `__len__` — number of items return karo
- `__add__` — do carts merge karo (`cart1 + cart2`)
- `__contains__` — check karo item hai ya nahi (`"Apple" in cart`)

**Normal Method:**
- `add_item(item)` — item add karo

**Test karo:**
```python
cart1 = ShoppingCart()
cart1.add_item("Apple")
cart1.add_item("Bread")

cart2 = ShoppingCart()
cart2.add_item("Milk")
cart2.add_item("Eggs")

print(cart1)                    # Cart has 2 items: Apple, Bread
print(len(cart1))               # 2
print("Apple" in cart1)         # True
print("Pizza" in cart1)         # False

cart3 = cart1 + cart2           # merge!
print(cart3)                    # Cart has 4 items: Apple, Bread, Milk, Eggs
print(len(cart3))               # 4
```

---

### Concepts Explained — Hinglish mein:

**`__len__`:**
```python
def __len__(self):
    return len(self.items)
# len(cart1) likhne pe Python khud __len__ call karta hai
```

**`__add__`:**
```python
def __add__(self, other):
    # other = doosra cart
    new_cart = ShoppingCart()
    new_cart.items = self.items + other.items
    return new_cart             # naya merged cart return karo!
# cart1 + cart2 likhne pe Python khud __add__ call karta hai
# cart1.__add__(cart2) same hi hai!
```

**`__contains__`:**
```python
def __contains__(self, item):
    return item in self.items
# "Apple" in cart1 likhne pe Python __contains__ call karta hai
```

---

### Hints:
- `__str__` mein `", ".join(self.items)` use karo items ko comma se jodne ke liye
- `__add__` mein ek naya ShoppingCart object banao aur return karo
- `__contains__` mein `item in self.items` return karo

---

### Solution:

```python
class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        items_str = ", ".join(self.items)
        return f"Cart has {len(self.items)} items: {items_str}"

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.items = self.items + other.items
        return new_cart

    def __contains__(self, item):
        return item in self.items


cart1 = ShoppingCart()
cart1.add_item("Apple")
cart1.add_item("Bread")

cart2 = ShoppingCart()
cart2.add_item("Milk")
cart2.add_item("Eggs")

print(cart1)
print(len(cart1))
print("Apple" in cart1)
print("Pizza" in cart1)

cart3 = cart1 + cart2
print(cart3)
print(len(cart3))
```

### Output:
```
Cart has 2 items: Apple, Bread
2
True
False
Cart has 4 items: Apple, Bread, Milk, Eggs
4
```

---

---

# Problem 7 — Animal Kingdom 🐾
### Topics: Single Inheritance, Multilevel Inheritance, `super()`

---

### Inheritance kya hai?

```
Parent Class  →  Baap ki class — sabse basic
Child Class   →  Beta ki class — parent ka sab kuch + apna extra

Socho:
Animal    →  Parent (sabhi animals mein common: naam, sound)
Dog       →  Child of Animal (+ apna kaam: fetch)
GuideDog  →  Child of Dog (+ apna kaam: guide)
```

Ye hai **Multilevel Inheritance:**
```
Animal → Dog → GuideDog
```

---

### Problem:

**Level 1 — `Animal` class:**
- `__init__`: `name`, `sound`
- `speak()`: print karo `"Tommy says: Woof"`
- `__str__`: return karo `"Animal: Tommy"`

**Level 2 — `Dog(Animal)` class:**
- `__init__`: `name`, `sound`, `breed` — `super()` use karo!
- `fetch(item)`: print karo `"Tommy fetches the ball!"`
- `__str__`: return karo `"Dog: Tommy | Breed: Labrador"`

**Level 3 — `GuideDog(Dog)` class:**
- `__init__`: `name`, `breed`, `owner` — sound hamesha `"Woof"` fix karo
- `guide()`: print karo `"Tommy is guiding Ramu safely"`
- `__str__`: return karo `"GuideDog: Tommy | Owner: Ramu"`

**Test karo:**
```python
a = Animal("Leo", "Roar")
a.speak()

d = Dog("Tommy", "Woof", "Labrador")
d.speak()           # inherited from Animal!
d.fetch("ball")     # Dog ka apna method

g = GuideDog("Max", "Poodle", "Ramu")
g.speak()           # inherited from Animal!
g.fetch("stick")    # inherited from Dog!
g.guide()           # GuideDog ka apna method

print(a)
print(d)
print(g)
```

---

### Concepts Explained — Hinglish mein:

**Inheritance syntax:**
```python
class Dog(Animal):      # Animal = parent
    pass                # Dog ko Animal ki sab cheezein mil jaati hain!
```

**`super()` kya karta hai?**
```python
class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)   # Animal ka __init__ call karo!
        # Super() matlab "apne parent ko call karo"
        # Isse Animal wala naam aur sound set ho jayega
        # Phir apna extra variable add karo:
        self.breed = breed
```

**Method Inheritance:**
```python
# Dog ne speak() khud nahi likha
# Lekin Animal mein hai toh Dog bhi use kar sakta hai!
d = Dog("Tommy", "Woof", "Labrador")
d.speak()   # Animal ka speak() chalega — automatically!
```

**Multilevel:**
```python
# GuideDog → Dog → Animal
# GuideDog ke paas teeno ka sab kuch hai!
g = GuideDog("Max", "Poodle", "Ramu")
g.speak()    # Animal se
g.fetch()    # Dog se
g.guide()    # GuideDog ka apna
```

---

### Hints:
- `super().__init__(name, sound)` — parent ka constructor call karna
- `GuideDog` mein sound fix karna: `super().__init__(name, "Woof", breed)`
- Child class mein parent ke methods automatically available hain

---

### Solution:

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says: {self.sound}")

    def __str__(self):
        return f"Animal: {self.name}"


class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)   # Animal ka __init__ call karo
        self.breed = breed

    def fetch(self, item):
        print(f"{self.name} fetches the {item}!")

    def __str__(self):
        return f"Dog: {self.name} | Breed: {self.breed}"


class GuideDog(Dog):
    def __init__(self, name, breed, owner):
        super().__init__(name, "Woof", breed)   # Dog ka __init__ call karo
        self.owner = owner

    def guide(self):
        print(f"{self.name} is guiding {self.owner} safely")

    def __str__(self):
        return f"GuideDog: {self.name} | Owner: {self.owner}"


a = Animal("Leo", "Roar")
a.speak()

d = Dog("Tommy", "Woof", "Labrador")
d.speak()
d.fetch("ball")

g = GuideDog("Max", "Poodle", "Ramu")
g.speak()
g.fetch("stick")
g.guide()

print(a)
print(d)
print(g)
```

---

---

# Problem 8 — Smart Device 📱
### Topics: Multiple Inheritance, Hierarchical Inheritance, MRO

---

### Multiple Inheritance kya hai?

```
Ek child ke DO parents!

class SmartPhone(Phone, Camera):
#                ^^^^   ^^^^^^
#                parent1  parent2
```

Real life:
```
SmartPhone = Phone + Camera + Computer sabka mix!
```

### Hierarchical Inheritance kya hai?

```
Ek parent ke MULTIPLE children!

         Device
        /      \
    Phone      Laptop
    /    \
SmartPhone TabletPhone
```

---

### Problem:

**Parent 1 — `Caller` class:**
- `make_call(number)`: print karo `"Calling: 9876543210"`
- `end_call()`: print karo `"Call ended"`

**Parent 2 — `Camera` class:**
- `take_photo()`: print karo `"📸 Photo taken!"`
- `record_video()`: print karo `"🎥 Recording started"`

**Parent 3 — `Browser` class:**
- `open_url(url)`: print karo `"Opening: google.com"`

**Child — `SmartPhone(Caller, Camera, Browser)` class:**
- `__init__`: `brand`, `model`
- `specs()`: print karo `"Brand: Samsung | Model: S24"`

**Test karo:**
```python
phone = SmartPhone("Samsung", "S24")
phone.specs()
phone.make_call("9876543210")   # Caller se mila
phone.take_photo()              # Camera se mila
phone.open_url("google.com")    # Browser se mila
phone.end_call()

# MRO check karo:
print(SmartPhone.__mro__)
```

---

### Concepts Explained — Hinglish mein:

**Multiple Inheritance syntax:**
```python
class SmartPhone(Caller, Camera, Browser):
    # Teeno parents ka sab kuch mil gaya!
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

**MRO kya hai? (Method Resolution Order)**
```python
# Agar do parents mein same naam ka method ho
# toh Python kaunsa use karega?
# MRO batata hai order!

print(SmartPhone.__mro__)
# Output: SmartPhone → Caller → Camera → Browser → object
# Python left to right dhundta hai!
```

**Hierarchical — ek parent, multiple children:**
```python
class Caller:           # parent
    pass

class Phone(Caller):    # child 1
    pass

class Tablet(Caller):   # child 2
    pass
# Dono ko Caller ka sab kuch mila — alag alag!
```

---

### Hints:
- Multiple inheritance: `class SmartPhone(Caller, Camera, Browser):`
- Koi `super().__init__()` ki zarurat nahi agar parents mein `__init__` nahi hai
- `__mro__` ek tuple return karta hai — class hierarchy dikhata hai

---

### Solution:

```python
class Caller:
    def make_call(self, number):
        print(f"Calling: {number}")

    def end_call(self):
        print("Call ended")


class Camera:
    def take_photo(self):
        print("Photo taken!")

    def record_video(self):
        print("Recording started")


class Browser:
    def open_url(self, url):
        print(f"Opening: {url}")


class SmartPhone(Caller, Camera, Browser):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def specs(self):
        print(f"Brand: {self.brand} | Model: {self.model}")


phone = SmartPhone("Samsung", "S24")
phone.specs()
phone.make_call("9876543210")
phone.take_photo()
phone.open_url("google.com")
phone.end_call()

print(SmartPhone.__mro__)
```

---

---

# Problem 9 — Shape Calculator 🔷
### Topics: Method Overriding, Operator Overloading, `__eq__`, `__gt__`

---

### Method Overriding kya hai?

```
Parent mein ek method hai
Child mein SAME naam ka method likhte hain
Child ka method parent ka override kar deta hai!

Parent:  def area(): return 0
Child:   def area(): return length * width  ← ye chalega!
```

### Operator Overloading kya hai?

```
Normally + sirf numbers ke liye kaam karta hai
Lekin tum apni class mein batao ki + ka matlab kya ho!

shape1 + shape2  →  areas add karo
shape1 > shape2  →  area compare karo
shape1 == shape2 →  areas equal hain kya
```

---

### Problem:

**Parent — `Shape` class:**
- `__init__`: `color`
- `area()`: return `0` (override hoga!)
- `__str__`: return `"Shape | Color: Red | Area: 0"`

**Child 1 — `Rectangle(Shape)` class:**
- `__init__`: `color`, `length`, `width` — `super()` use karo
- `area()`: override karo — `length * width`
- `__str__`: return `"Rectangle | Color: Blue | Area: 20"`

**Child 2 — `Circle(Shape)` class:**
- `__init__`: `color`, `radius` — `super()` use karo
- `area()`: override karo — `3.14 * radius * radius`
- `__str__`: override karo

**Operator Overloading in `Shape`:**
- `__eq__(self, other)` — areas equal hain kya?
- `__gt__(self, other)` — kaunsa bada hai?
- `__add__(self, other)` — dono areas add karo

**Test karo:**
```python
r = Rectangle("Blue", 4, 5)
c = Circle("Red", 3)

print(r)                    # Rectangle | Color: Blue | Area: 20
print(c)                    # Circle | Color: Red | Area: 28.26
print(r.area())             # 20
print(c.area())             # 28.26

print(r == c)               # False
print(c > r)                # True (28.26 > 20)
print(r + c)                # 48.26
```

---

### Concepts Explained — Hinglish mein:

**Method Overriding:**
```python
class Shape:
    def area(self):
        return 0              # default

class Rectangle(Shape):
    def area(self):           # SAME naam — override!
        return self.length * self.width   # naya logic
# Ab Rectangle ka area() chalega, Shape ka nahi!
```

**`__gt__` — greater than:**
```python
def __gt__(self, other):
    return self.area() > other.area()
# c > r likhne pe Python c.__gt__(r) call karta hai!
```

**`__eq__` — equal:**
```python
def __eq__(self, other):
    return self.area() == other.area()
# r == c likhne pe Python r.__eq__(c) call karta hai!
```

---

### Hints:
- Parent mein `__eq__`, `__gt__`, `__add__` likho — children inherit kar lenge
- `area()` children mein override karo
- `__str__` mein `self.area()` call karo — calculated value aayegi

---

### Solution:

```python
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0

    def __str__(self):
        return f"Shape | Color: {self.color} | Area: {self.area()}"

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __add__(self, other):
        return self.area() + other.area()


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle | Color: {self.color} | Area: {self.area()}"


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return round(3.14 * self.radius * self.radius, 2)

    def __str__(self):
        return f"Circle | Color: {self.color} | Area: {self.area()}"


r = Rectangle("Blue", 4, 5)
c = Circle("Red", 3)

print(r)
print(c)
print(r == c)
print(c > r)
print(r + c)
```

---

---

# Problem 10 — Library System 📚
### Topics: Full OOP Project — `dir()`, `__dict__`, `__slots__`, Hybrid Inheritance

> ⚠️ **Boss Level — Ye sabka combination hai!**
> Seedha solution mat dekho — pehle try karo!

---

### Naye concepts:

**`__dict__`:**
```python
# Kisi bhi object ke saare attributes dictionary mein dekho!
print(book.__dict__)
# {'title': 'Python Basics', 'author': 'Aryan', 'price': 299}
```

**`dir()`:**
```python
# Kisi bhi object ke saare methods aur attributes list mein dekho!
print(dir(book))
# ['__class__', '__init__', 'title', 'borrow', 'return_book', ...]
```

**`__slots__`:**
```python
class Book:
    __slots__ = ['title', 'author', 'price']
    # Sirf ye teen attributes allowed!
    # Naya attribute add karna → AttributeError!
    # Memory efficient bhi hota hai!
```

---

### Problem:

**`LibraryItem` — Base class:**
- `__slots__ = ['title', 'item_id']`
- `__init__`: `title`, `item_id`
- `get_info()`: return `"Item: Python Basics | ID: 001"`

**`Borrowable` — Mixin class:**
- `__init__`: `self.is_borrowed = False`
- `borrow(user)`: agar available ho toh borrow karo, warna `"Already borrowed!"`
- `return_item()`: wapas karo

**`Book(LibraryItem, Borrowable)` — Multiple inheritance:**
- `__init__`: `title`, `item_id`, `author` — dono parents init karo!
- `__str__`: `"Book: Python Basics | Author: Aryan | Available: Yes"`
- `__eq__`: `item_id` same hai toh equal

**`Magazine(LibraryItem, Borrowable)` — Multiple inheritance:**
- `__init__`: `title`, `item_id`, `issue_number`
- `__str__`: `"Magazine: Tech Today | Issue: 42 | Available: Yes"`

**`Library` — Manager class:**
- `__init__`: empty `items` list
- `add_item(item)`: add karo
- `find_by_title(title)`: dhundho
- `show_all()`: sab print karo
- `__len__`: total items

**Test karo:**
```python
b1 = Book("Python Basics", "001", "Aryan")
b2 = Book("Clean Code", "002", "Robert")
m1 = Magazine("Tech Today", "003", 42)

lib = Library()
lib.add_item(b1)
lib.add_item(b2)
lib.add_item(m1)

print(len(lib))              # 3
lib.show_all()

b1.borrow("Ramu")
print(b1)                    # Available: No
b1.borrow("Shyam")          # Already borrowed!
b1.return_item()
print(b1)                    # Available: Yes

# Inspect karo:
print(b1.__dict__)           # __slots__ ke saath kya hoga?
print(dir(b1))               # saari methods!
found = lib.find_by_title("Python Basics")
print(found)
```

---

### Key learning points:

```
1. __slots__ ke saath __dict__ available nahi hota!
   (Ye ek important observation hai — test karo khud!)

2. Multiple inheritance mein super() chain karta hai
   Book → LibraryItem → Borrowable

3. Mixin pattern — Borrowable sirf ek "behavior" add karta hai
   Ye real world OOP pattern hai!

4. dir() mein bahut saari cheezein aati hain — mostly dunder methods
```

---

### Hints:
- `__slots__` sirf `LibraryItem` mein hai — `Borrowable` aur `Library` mein nahi
- `Book.__init__` mein: `LibraryItem.__init__(self, title, item_id)` aur `Borrowable.__init__(self)` dono call karo
- `is_borrowed` ko `__slots__` mein add nahi kiya — isliye `Borrowable` mein hai

---

### Solution:

```python
class LibraryItem:
    __slots__ = ['title', 'item_id']

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def get_info(self):
        return f"Item: {self.title} | ID: {self.item_id}"


class Borrowable:
    def __init__(self):
        self.is_borrowed = False

    def borrow(self, user):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed!")
        else:
            self.is_borrowed = True
            print(f"'{self.title}' borrowed by {user}")

    def return_item(self):
        self.is_borrowed = False
        print(f"'{self.title}' returned successfully!")


class Book(LibraryItem, Borrowable):
    def __init__(self, title, item_id, author):
        LibraryItem.__init__(self, title, item_id)
        Borrowable.__init__(self)
        self.author = author

    def __str__(self):
        available = "No" if self.is_borrowed else "Yes"
        return f"Book: {self.title} | Author: {self.author} | Available: {available}"

    def __eq__(self, other):
        return self.item_id == other.item_id


class Magazine(LibraryItem, Borrowable):
    def __init__(self, title, item_id, issue_number):
        LibraryItem.__init__(self, title, item_id)
        Borrowable.__init__(self)
        self.issue_number = issue_number

    def __str__(self):
        available = "No" if self.is_borrowed else "Yes"
        return f"Magazine: {self.title} | Issue: {self.issue_number} | Available: {available}"


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item.title}")

    def find_by_title(self, title):
        for item in self.items:
            if item.title == title:
                return item
        return None

    def show_all(self):
        print("\n--- Library Collection ---")
        for item in self.items:
            print(item)

    def __len__(self):
        return len(self.items)


# Test
b1 = Book("Python Basics", "001", "Aryan")
b2 = Book("Clean Code", "002", "Robert")
m1 = Magazine("Tech Today", "003", 42)

lib = Library()
lib.add_item(b1)
lib.add_item(b2)
lib.add_item(m1)

print(f"\nTotal items: {len(lib)}")
lib.show_all()

print()
b1.borrow("Ramu")
print(b1)
b1.borrow("Shyam")
b1.return_item()
print(b1)

print("\nInspecting b1:")
try:
    print(b1.__dict__)         # __slots__ ki wajah se error!
except AttributeError as e:
    print(f"__dict__ not available: {e}")

found = lib.find_by_title("Python Basics")
print(f"\nFound: {found}")
```

---

---

## Summary Table — OOP Concepts 🎯

| Concept | Problem | Key Syntax |
|---------|---------|------------|
| Class + Object | 1 | `class Name:` + `obj = Name()` |
| `__init__` + `self` | 1 | `def __init__(self, ...)` |
| Class Variables | 2 | Outside `__init__`, inside class |
| `@classmethod` | 2, 5 | `def method(cls, ...)` |
| `@property` | 3 | Getter + Setter + Validation |
| Access Modifiers | 4 | `name`, `_name`, `__name` |
| `@staticmethod` | 4 | `def method()` — no self/cls |
| Alternative Constructor | 5 | `@classmethod` + `return cls(...)` |
| `__str__` | 5, 6 | `print(obj)` pe call hota hai |
| Dunder Methods | 6 | `__len__`, `__add__`, `__contains__` |
| Inheritance | 7 | `class Child(Parent):` |
| `super()` | 7, 9 | `super().__init__(...)` |
| Multiple Inheritance | 8, 10 | `class Child(P1, P2):` |
| MRO | 8 | `Class.__mro__` |
| Method Overriding | 9 | Same method naam, child mein |
| Operator Overloading | 9 | `__eq__`, `__gt__`, `__add__` |
| `__slots__` | 10 | Memory efficient attributes |
| `__dict__` + `dir()` | 10 | Object inspection |

---

> **Final tip:** OOP ek mindset hai — har cheez ko object ki tarah socho.
> Duniya mein jo bhi hai — Car, Student, Pizza, Library — sab ek class ban sakta hai!
> Jitna practice karoge utna natural lagega. Keep going Aryan! 🚀
