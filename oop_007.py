# Polymorphism
class Square:
    def __init__(self, edge):
        self.edge = edge

    def calculation(self):
        print("Area of Square : ", self.edge **2)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculation(self):
        print("Area of Triangle : ", self.length * self.width)

square = Square(5)
rec = Rectangle(10, 5)

square.calculation()
rec.calculation()
