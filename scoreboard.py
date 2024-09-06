from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font= FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()