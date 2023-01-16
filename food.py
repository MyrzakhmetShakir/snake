from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("red")
        self.shapesize(0.5)
        self.refresh()

    def refresh(self):
        x_random = random.randint(-270, 270)
        y_random = random.randint(-270, 270)
        self.goto(x_random, y_random)