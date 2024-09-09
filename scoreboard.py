from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.hideturtle()
        self.teleport(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def add_score(self):
        self.score += 1

        self.update_scoreboard()