import random
from turtle import Turtle

class Food(Turtle):
    
    def __init__(self, color = "green"):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
