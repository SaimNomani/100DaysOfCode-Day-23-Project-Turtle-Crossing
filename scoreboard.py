from turtle import Turtle

ALIGNMENT = 'center'
FONT_SMALL = ('Courier', 16, "bold")
FONT_LARGE = ('Courier', 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("black")
        self.penup()
        self.goto(-200, 260)
        self.current_score = 0
        self.final_level = 5
        self.display_score()

    def display_score(self):
        """display the score"""
        self.write(f"Level: {self.current_score}/{self.final_level}", align=ALIGNMENT, font=FONT_SMALL)

    def update_score(self):
        """update the score"""
        self.clear()
        self.current_score += 1
        self.display_score()

    def game_over(self):
        """game over message"""
        print("game over")
        print(f"{self.current_score}")
        self.goto(0, 0)
        if self.current_score == self.final_level:
            self.write(f"Game Over\nYou win", align=ALIGNMENT, font=FONT_LARGE)
        else:
            self.write(f"Game Over\nYou lose", align=ALIGNMENT, font=FONT_LARGE)
