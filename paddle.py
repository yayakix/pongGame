from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.goto(x_cor, 0)
        self.shapesize(5, 1)
        self.ycor()

    def move_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)


    def move_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)
