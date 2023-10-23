from turtle import Turtle
import random

colors = ['red', 'orange', 'yellow', 'purple', 'brown', 'blue', 'green']


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.move_dist = 10
        self.car_move_speed = 0.1

    def generate_car(self):
        """generate cars of random colors at random positions"""
        chance = random.randint(1, 5)
        # print(chance)
        if chance == 1:
            # print("generated")
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(colors))
            new_car.penup()
            random_y = random.randint(-240, 240)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def move(self):
        """function to move cars"""
        for car in self.all_cars:
            car.back(self.move_dist)

    def level_up(self):
        """increase the speed of cars"""
        if self.car_move_speed > 0.01:
            self.car_move_speed *= 0.9
