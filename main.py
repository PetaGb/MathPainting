import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)


class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):

        canvas.data[self.x: self.x + self.width, self.y: self.y + self.height] = self.color


canvas = Canvas(20, 30, (255, 255, 255))
r1 = Rectangle(5, 7, 2, 6, (255, 100, 180))
r1.draw(canvas)
s1 = Square(12, 12, 9, (20, 180, 60))
s1.draw(canvas)
canvas.make("canvas.png")
