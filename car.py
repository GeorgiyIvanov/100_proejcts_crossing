from turtle import Turtle
import random
speed = 3
COLORS = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']
X = 400


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        if random.randint(1, 8) == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=1.8)
            new_car.goto(x=X, y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(speed)

    def level_up(self):
        global speed
        speed += 3

    def memory_control(self):
        if len(self.all_cars) > 64:
            car = self.all_cars.pop(0)
            car.hideturtle()
