class person:

    def __init__(self,n,o):                 # This is Parameterized constructor because it passes n and o as arguments, if it only passes self so it is default constructor
        print("Hey I am a Person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a=person("VScode","Editor")         # Obj. calling constructor
b=person("Reva","Coder")
a.info()
b.info()