from turtle import Turtle
CURRENT_SCORE = 0


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        with open("C:\\Users\\91877\\PycharmProjects\\day-20,21-snake_game\\high_score.txt") as score:
            high_score = score.read()
        self.high = int(high_score)
        self.scores()

    def scores(self):
        self.clear()
        global CURRENT_SCORE
        self.goto(0, 280)
        self.write(arg=f"SCORE: {CURRENT_SCORE}  HIGH SCORE: {self.high}",
                   align="center", font=('Arial', 14, 'normal'))
        CURRENT_SCORE += 1

    def high_score(self):
        global CURRENT_SCORE
        if CURRENT_SCORE > self.high:
            self.high = CURRENT_SCORE
            with open("C:\\Users\\91877\\PycharmProjects\\day-20,21-snake_game\\high_score.txt", mode="w") as file:
                file.write(f"{self.high}")

    def game_over(self):
        self.goto(-50, 0)
        self.write(arg="GAME OVER", font=('Arial', 16, 'normal'))
