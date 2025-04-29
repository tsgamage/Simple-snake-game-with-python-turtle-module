from turtle import Turtle

SCORE_TEXT_ALIGNMENT = "center"
FONT = ("courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self, text_color = "white"):
        super().__init__()
        self.hideturtle()
        self.color(text_color)
        self.penup()
        self.goto(0, 275)
        self.score = 0
        self.increase_score()

    def show_score(self):
        self.write(f"Score: {self.score}", move=False, align=SCORE_TEXT_ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.show_score()
        self.score += 1
