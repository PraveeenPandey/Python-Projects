import turtle
from turtle import Turtle, Screen
import random

prince_turtle = Turtle()
turtle.colormode(255)

def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

prince_turtle.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        prince_turtle.color(random_color())
        prince_turtle.circle(100)
        prince_turtle.setheading(prince_turtle.heading() + size_of_gap)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
