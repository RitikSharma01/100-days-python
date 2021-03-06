from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, cordinate):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed(0)
        self.penup()
        self.goto(cordinate)

    def upward(self):
        new_ycor = self.ycor()+20
        self.goto(self.xcor(), new_ycor)

    def downward(self):
        new_ycor = self.ycor()-20
        self.goto(self.xcor(), new_ycor)
