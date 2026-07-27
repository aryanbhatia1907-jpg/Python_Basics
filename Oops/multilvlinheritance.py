class dada:
    def __init__ (self,name,house):
        self.name=name 
        self.house=house

    def Prop (self):
        print(f"Grandfather Property: {self.house}")
    
class papa(dada):
    def __init__(self,name,car):
        dada.__init__ (self,name,house="Ghar")
        self.car=car

    def Prop (self):
        dada.Prop(self)
        print(f"Papa Property: {self.car}")

class me(papa):
    def __init__ (self,name,laptop):
        papa.__init__ (self,name,car="gadi")
        self.laptop=laptop

    def Prop (self):
        papa.Prop(self)
        print(f"{self.name} Property: {self.laptop}")
        
a=me("Aryan","Lenovo")
a.Prop()
