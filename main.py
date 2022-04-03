from turtle import Screen
from time import sleep
from crosser import Crosser
from car import CarManager
from level_controller import LevelController

screen = Screen()
screen.title("Road Crossing")
screen.setup(width=800, height=600)
screen.tracer(0)

crosser = Crosser()
car_manager = CarManager()
level_controller = LevelController()

screen.listen()
screen.onkeypress(crosser.up, "Up")

game_on = True
while game_on:
    screen.update()
    sleep(0.001)

    car_manager.create_car()
    car_manager.move()
    car_manager.memory_control()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(crosser) < 18:
            level_controller.game_over()
            game_on = False

    # Detect successful cross
    if crosser.ycor() > 280:
        level_controller.update_level()
        crosser.reset_pos()
        car_manager.level_up()

screen.exitonclick()
