class American(object):
    @staticmethod
    def printNationality():
        print("America")

anAmerican = American()
# anAmerican.printNationality()
# American.printNationality()

class NewYorker(American):
    pass

aNewYorker = NewYorker()
# print(aNewYorker)

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
# print(aCircle.area())

class Rectangle():
    def __init__(self, l, r):
        self.length = l
        self.width = r

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2, 3)
# print(aRectangle.area())

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print(aSquare.area())
