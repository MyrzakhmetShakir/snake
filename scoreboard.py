from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        with open("./score.txt") as text:
            self.high_score = int(text.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.update()

    def update(self):
        self.goto(0, 220)
        self.color("yellow")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal", "bold"))
        self.color("white")
        self.goto(0, 270)
        self.write(f"High_score: {self.high_score}", align="center", font=("Arial", 15, "normal", "bold"))

    def high_score_set(self):
        self.clear()
        if self.score > self.high_score:
            with open("./score.txt", mode="w") as text:
                text.write(str(self.score))
            self.high_score = self.score
            self.update()

    def reset(self):
        self.clear()
        self.score = 0
        self.update()


    def add_score(self):
        self.clear()
        self.score += 1
        self.update()