from turtle import Screen, Turtle
import time
from snake import Snake, COORDINATE_LIST
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.mode("standard")
screen.tracer(0)
snake_controls = Snake()
snake_controls.make_snake()
game_on = True
score = 0
fruit_list = []


def make_fruit():
    """Making fruit"""
    random_x = random.choice(COORDINATE_LIST)
    random_y = random.choice(COORDINATE_LIST)
    fruit = Turtle("circle")
    fruit.penup()
    fruit.color("white")
    fruit.goto(random_x, random_y)
    fruit_list.append(fruit)
    return fruit.position()


for item in snake_controls.snake_body:
    screen.listen()
    screen.onkeypress(fun=snake_controls.turn_right, key="d")
    screen.onkeypress(fun=snake_controls.move_up, key="w")
    screen.onkeypress(fun=snake_controls.move_down, key="s")
    screen.onkeypress(fun=snake_controls.turn_left, key="a")

make_fruit()

while game_on:
    screen.update()
    time.sleep(.1)

    for seg_num in range(len(snake_controls.snake_body) - 1, 0, -1):
        new_x = snake_controls.snake_body[seg_num - 1].xcor()
        new_y = snake_controls.snake_body[seg_num - 1].ycor()
        snake_controls.snake_body[seg_num].goto(new_x, new_y)
    snake_controls.snake_body[0].forward(20)

    if snake_controls.snake_body[0].position() == fruit_list[0].position():
        score += 1
        fruit_list[0].reset()
        fruit_list.clear()
        make_fruit()
        print(fruit_list)
        print(fruit_list[0].position())
        print(score)


screen.exitonclick()
