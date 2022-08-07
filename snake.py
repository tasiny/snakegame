from turtle import Turtle

DOWN = 90
UP = 270
LEFT = 0
RIGHT = 180


class Snake:
    def __init__(self):
        self.snake_body = []

    def make_snake(self):
        for coord in [-20.0, 0.0, 20.00]:
            new_turtle = Turtle()
            self.snake_body.append(new_turtle)
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.shape("square")
            new_turtle.goto(coord, 0)

    def add_segment(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        self.snake_body.append(new_segment)

    def move_up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def turn_right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def turn_left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def move_down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)






