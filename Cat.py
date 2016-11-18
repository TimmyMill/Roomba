import turtle
from turtle import *
from random import *
image = '/home/timmy/PycharmProjects/Roomba/sharkcat_100.gif'


class Cat(Turtle):
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
        while True:

            # heading east
            if self.direction == 0:
                print(str(self.position))
                # self.position() returns a two element list containing the current (x, y) coordinates
                max_forward = (self.screen_width / 2) - self.position()[0]
                # if current x position is positive
                self.forward(uniform(0, max_forward)) if self.position()[0] >= 0 \
                    else self.forward(uniform(self.position()[0], max_forward))
                # else x position is negative
                self.right(90)

            # heading south
            elif self.direction == 270:
                print(str(self.position))
                max_forward = (self.screen_height / 2) - self.position()[1]
                # if current y position is positive
                self.forward(uniform(self.position()[1], max_forward)) if self.position()[1] >= 0 \
                    else self.forward(uniform(0, max_forward))
                # else y position is negative
                self.right(90)

            # heading west
            elif self.direction == 180:
                print(str(self.position))
                max_forward = (self.screen_width / 2) - self.position()[0]
                # if current x position is positive
                self.forward(uniform(self.position()[0], max_forward)) if self.position()[0] >= 0 \
                    else self.forward(uniform(0, max_forward))
                # else x position is negative
                self.right(90)

            # heading north
            elif self.direction == 90:
                print(str(self.position))
                max_forward = (self.screen_height / 2) - self.position()[1]
                # if current y position is positive
                self.forward(uniform(0, max_forward)) if self.position()[1] >= 0 \
                    else self.forward(uniform(0, max_forward))
                # else y position is negative
                self.right(90)

roomba = Cat()
roomba.move()
