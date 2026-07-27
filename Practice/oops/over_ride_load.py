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