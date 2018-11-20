class Shape:
    def __init__(self, length, high):
        self.length = length
        self.high = high


class Triangle(Shape):
    def area(self):
        area = self.length*self.high/2
        return area


class Rectangle(Shape):
    def area(self):
        area = self.length*self.high
        return area
        

t = Triangle(100, 40)
print(t.area())

r = Rectangle(100, 40)
print(r.area())
