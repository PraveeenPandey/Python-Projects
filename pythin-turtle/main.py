from turtle import Turtle,Screen
import random

colours = [" yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "gray", "white"]

prince_turtle = Turtle()
prince_turtle.back(50)
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        prince_turtle.forward(100)
        prince_turtle.right(angle)

for shape_side_n in range(3, 11):
    prince_turtle.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
