from turtle import Turtle
import random

COORDINATE_LIST = [float(x) for x in range(-240, 260, 20)]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.speed("fastest")
        random_x = random.choice(COORDINATE_LIST)
        random_y = random.choice(COORDINATE_LIST)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.choice(COORDINATE_LIST)
        random_y = random.choice(COORDINATE_LIST)
        self.goto(random_x, random_y)
