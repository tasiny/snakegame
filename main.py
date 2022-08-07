from turtle import Screen, Turtle
import time
from snake import Snake
import random
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.mode("standard")
screen.tracer(0)
snake_controls = Snake()
snake_controls.make_snake()
game_on = True
food = Food()
score_board = ScoreBoard()
game_line = score_board.borders()
for item in snake_controls.snake_body:
    screen.listen()
    screen.onkeypress(fun=snake_controls.turn_right, key="d")
    screen.onkeypress(fun=snake_controls.move_up, key="w")
    screen.onkeypress(fun=snake_controls.move_down, key="s")
    screen.onkeypress(fun=snake_controls.turn_left, key="a")


while game_on:
    screen.update()
    time.sleep(.1)

    for seg_num in range(len(snake_controls.snake_body) - 1, 0, -1):
        new_x = snake_controls.snake_body[seg_num - 1].xcor()
        new_y = snake_controls.snake_body[seg_num - 1].ycor()
        snake_controls.snake_body[seg_num].goto(new_x, new_y)
    snake_controls.snake_body[0].back(20)


    for segment in [x for x in snake_controls.snake_body if x != snake_controls.snake_body[0]]:
        """maybe change order of segments to solve issue"""
        if snake_controls.snake_body[0].distance(segment) < 15:
            game_on = False
    if snake_controls.snake_body[0].distance(food) < 15:
        snake_controls.add_segment()
        score_board.clear()
        score_board.increase_score()
        food.refresh()
    elif snake_controls.snake_body[0].xcor() == -300 or snake_controls.snake_body[0].xcor() == 280 or \
            snake_controls.snake_body[0].ycor() == 280 or snake_controls.snake_body[0].ycor() == -280:
        game_on = False


screen.exitonclick()
