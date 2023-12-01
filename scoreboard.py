from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Segoe UI', 14, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.goto(x=0, y=270)
        self.update_scoreboard()
        self.speed = 0.12

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def speed_up(self):
        self.speed -= 0.02

    def score_counting(self):
        self.score += 1
        self.update_scoreboard()
        if self.score % 10 == 0 and self.score < 50:
            self.speed_up()
        elif self.score >= 50:
            self.speed = 0.02
