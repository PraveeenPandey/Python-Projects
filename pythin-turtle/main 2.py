import turtle
from turtle import Turtle, Screen
import random

prince_turtle = Turtle()
turtle.colormode(255)

def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
prince_turtle.pensize(15)
prince_turtle.speed("fastest")
for _ in range(200):
    prince_turtle.color(random_color())
    prince_turtle.forward(30)
    prince_turtle.setheading(random.choice(directions))
screen = Screen()
screen.exitonclick()