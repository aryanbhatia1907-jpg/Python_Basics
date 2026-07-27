class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says: {self.sound}")

    def __str__(self):
        return f"Animal:{self.name}"
    
class Dog(Animal):
    def __init__(self, name, sound,breed):
        super().__init__(name, sound)
        self.breed = breed

    def fetch(self,item):
        print(f"Tommy fetches the {item}!")


    def __str__(self):
        return f"Dog: {self.name}| Breed: {self.breed}"

class GuideDog(Dog):
    def __init__(self, name,breed, owner):
        super().__init__(name, breed,"Woof")
        self.owner = owner

    def guide(self):
        print(f"{self.name} is guiding {self.owner} safely")

    def __str__(self):
        return f"GuideDog: {self.name} | Owner: {self.owner}"
    
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