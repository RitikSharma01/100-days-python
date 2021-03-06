from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courior', 10, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.setpos(0, 280)
        self.hideturtle()
        self.score = 0
        self.write(f"Score: {self.score}",
                   align=ALIGNMENT, font=FONT)
        self.update_scoreboard()

    def refresh(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",
                   align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",
                   align=ALIGNMENT, font=FONT)
