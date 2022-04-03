from turtle import Turtle


class Crosser(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.reset_pos()

    def reset_pos(self):
        self.goto(0, -280)

    def up(self):
        self.forward(10)
