class Temperature:
    def __init__(self,celsius):
        self.__celsius = celsius

    @property 
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self,value):
        if value < -273:
            raise ValueError("Temperature cannot go below -273!")
        self.__celsius = value

    @property 
    def fahrenheit(self):
        return (self.__celsius * 1.8) + 32

t = Temperature(25)
print(t.celsius)       # 25
print(t.fahrenheit)    # 77.0

t.celsius = 100
print(t.fahrenheit)    # 212.0


try:
    t.celsius = -300    # ValueError!
except ValueError as e:
    print(e)