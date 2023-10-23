from turtle import Turtle

INITIAL_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINAL_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.final_line = FINAL_LINE
        self.set_turtle()

    def set_turtle(self):
        """set the turtle to initial position"""
        self.shape("turtle")
        self.penup()
        self.goto(INITIAL_POSITION)
        self.setheading(90)

    def move(self):
        """move the turtle forward"""
        self.forward(MOVE_DISTANCE)

    def reset(self):
        """reset the turtle to its initial position"""
        self.set_turtle()
