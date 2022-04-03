from turtle import Turtle


class LevelController(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.goto(-390, 265)
        self.write(f"Level: {self.level}", align='left', font=("Courier", 20, 'normal'))

    def game_over(self):
        self.goto((0, 0))
        self.write(f"GAME OVER", False, align='center', font=("Courier", 40, 'normal'))