import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Cross Turtle Game")
screen.tracer(0)


player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.generate_cars()
    car.move_cars()
    # Detect the collision with the cars
    for each_car in car.all_cars:
        if each_car.distance(player) < 20:
            print("Game Over!")
            game_is_on = False
            scoreboard.game_over()

    # Detect the collision with the opposite walls

    if player.ycor() > 250:
        player.goto(0, -280)
        car.move_faster()
        scoreboard.point()


screen.exitonclick()

