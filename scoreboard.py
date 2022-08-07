from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        self.score_line = Turtle()
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Current Score = {self.score} ", False, align="center", font=("Arial", 14, "bold"))

    def increase_score(self):
        self.score += 1
        self.write(f"Current Score = {self.score} ", False, align="center", font=("Arial", 14, "bold"))

    def borders(self):
        """creates scoreboard and borders with edges (-280, y), (x, 265), (280, x), (x, -260)"""
        self.score_line.hideturtle()
        self.score_line.penup()
        self.score_line.color("white")
        self.score_line.goto(-280, 265)
        self.score_line.pendown()
        self.score_line.forward(540)
        self.score_line.right(90)
        self.score_line.forward(265 + 260)
        self.score_line.right(90)
        self.score_line.forward(540)
        self.score_line.right(90)
        self.score_line.forward(265+260)



