import turtle
from turtle import *
from random import *
image = '/home/timmy/PycharmProjects/Roomba/sharkcat_100.gif'


class CatShark(Turtle):
    def __init__(self, x=0, y=0):
        turtle.Turtle.__init__(self)
        self.screen = self.getscreen()
        self.screen.register_shape(image)
        self.screen_height = self.getscreen().window_height()
        self.screen_width = self.getscreen().window_width()
        self.shape(image)
        self.penup()
        self.speed(1)
        self.goto(x, y)
        self.direction = self.heading()

    def move(self):
        # image size = 100x142 pixels
        width = (self.screen_width / 2) - 100
        height = (self.screen_height / 2) - 142
        while True:
            self.goto(randint(-width, width), randint(-height, height))


blah = CatShark()
blah.move()
