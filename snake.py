from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_body = []
        self.position = 0



    def create_snake(self, number):
        for number in range(number):
            snake = Turtle()
            snake.color("yellow")
            snake.shape("circle")
            snake.penup()
            snake.setpos(self.position, 0)
            self.position -= 20
            self.snake_body.append(snake)

    def move(self):
        for num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[num - 1].xcor()
            new_y = self.snake_body[num - 1].ycor()
            self.snake_body[num].goto(new_x, new_y)
        self.snake_body[0].forward(20)

    def add_segment(self):
        last_segment_coord = self.snake_body[len(self.snake_body)-1].pos()
        snake = Turtle()
        snake.color("yellow")
        snake.shape("circle")
        snake.penup()
        snake.setpos(last_segment_coord[0], last_segment_coord[1])
        self.snake_body.append(snake)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake(3)

    def left(self):
        if self.snake_body[0].heading() == 90:
            self.snake_body[0].left(90)
        elif self.snake_body[0].heading() == 270:
            self.snake_body[0].right(90)

    def right(self):
        if self.snake_body[0].heading() == 90:
            self.snake_body[0].right(90)
        elif self.snake_body[0].heading() == 270:
            self.snake_body[0].left(90)

    def up(self):
        if self.snake_body[0].heading() == 0:
            self.snake_body[0].left(90)
        elif self.snake_body[0].heading() == 180:
            self.snake_body[0].right(90)
    def down(self):
        if self.snake_body[0].heading() == 0:
            self.snake_body[0].right(90)
        elif self.snake_body[0].heading() == 180:
            self.snake_body[0].left(90)