from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

class score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}",align="center", font=("Arial",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.score+=1
        self.clear()
        self.update()

