from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 5
        self.y_move = 5

    def move(self):
        new_xval = self.xcor() + self.x_move
        new_yval = self.ycor() + self.y_move
        self.goto(new_xval, new_yval)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0,0)
        self.x_move *= -1




