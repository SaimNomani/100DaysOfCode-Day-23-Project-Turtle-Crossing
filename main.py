from turtle import Turtle, Screen
import time
import random
from car import Car
from player import Player
from scoreboard import Scoreboard

# main screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
#
# creating object of Car class
car = Car()
#
player = Player()
screen.listen()
screen.onkey(player.move, "Up")

score = Scoreboard()
is_on = True
while is_on:
    screen.update()
    time.sleep(car.car_move_speed)
    car.generate_car()
    car.move()
    # detect it player reaches the finish line
    if player.ycor() >= player.final_line:
        score.update_score()
        car.level_up()
        player.reset()
    #
    # detect it turtle collide with any of the car
    for n in car.all_cars:
        if player.distance(n) <= 20:
            score.game_over()
            is_on = False
    if score.current_score == score.final_level:
        score.game_over()
        is_on = False
screen.exitonclick()
