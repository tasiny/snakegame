from turtle import Turtle, Screen
COORDINATE_LIST = [20.00, 40.00, 60.00, 80.00, 100.00, 120.00, 140.00, 160.00, 180.00, 200.00, 220.00, 240.00]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []

    def make_snake(self):
        starting_x_position = 0
        for _ in range(3):
            new_turtle = Turtle()
            self.snake_body.append(new_turtle)
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.shape("square")
            new_turtle.goto(starting_x_position, 0)
            starting_x_position += 20

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






