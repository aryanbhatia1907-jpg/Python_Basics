# Hiearchiery

class papa:
    def __init__ (self,sname):
        self.sname=sname
    print("papa surname is Bhatia")
class bhai(papa):
    def __init__(self,hobby):
        papa. __init__(self,sname="Bhatia")
        self.hobby=hobby

    def show(self):
        print(f"bhai surname is {self.sname}\n Hobby is {self.hobby}")

class behen(papa):
    def __init__(self,hobby):
        papa. __init__(self,sname="Bhatia")
        self.hobby=hobby

    def show(self):
        print(f"behen surname is {self.sname}\n Hobby is {self.hobby}")
        
a=bhai("Piano")
a.show()
b=behen("Phone dekhna")
b.show()
    
print("\nHybrid Output Below\n")
# Hybrid

class dada:
    def __init__ (self,gem):
        self.gem=gem
        print(f"Dada object created with {self.gem}")

class papa(dada):
    def __init__(self,gem2):
        dada. __init__(self,gem="Netherite")
        self.gem2=gem2

    def show(self):
        print(f"papa has {self.gem2}")

class chacha(dada):
    def __init__(self,gem3):
        dada. __init__(self,gem="Netherite")
        self.gem3=gem3
    def show(self):
        print(f"Chacha has {self.gem3}")

class me(papa,chacha):
    def __init__(self,gem4):
        papa.__init__(self, gem2="Diamond")
        chacha.__init__(self, gem3="Gold")
        self.gem4=gem4

    def show(self):
        print(f"I have {self.gem4}")
        
c=me("Lapis")                                   # yahan pe do baar issliye chal rha kyu "me" se woh seedha woh "papa" mein jayega "mro" ki wajah se phir uss se likhega or usme "dada" ka cons bi hai to "dada" mein jaake phir likhega
print("\n--- Calling my own show method ---")
c.show()
print("\n--- Testing Inherited Properties ---")
print(f"Inherited from Papa: {c.gem2}")
print(f"Inherited from Chacha: {c.gem3}")
print(f"Inherited from Dada: {c.gem}")
    