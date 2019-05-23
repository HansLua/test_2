''''
方法重写与重载
'''


class Shape(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getPerimeter(self):
        c = (self.length + self.width) * 2
        print(c)


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getPerimeter(self):
        c = (self.b + self.a) * 2
        print(c,'this is rewrite in Rectangle!')


class Square(Shape):
    def __init__(self,side):
        self.side = side

    def getPerimeter(self):
        c = self.side*4
        print(c,'this is rewrite in Sqare!')

if __name__ == '__main__':
    shape = Shape(4,5)
    shape.getPerimeter()
    rectangle = Rectangle(7,8)
    rectangle.getPerimeter()
    square = Square(5)
    square.getPerimeter()
