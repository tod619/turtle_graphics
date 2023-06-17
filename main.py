# A project to explore the Turtle module
# 15/06/2023

from turtle import Turtle, Screen
import random

tim = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# Draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# Draw a dashed line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat",
           "SlateGray", "SeaGreen"]

diricetions = [0, 90, 180, 270]

# Draw a variety of shapes with different colours using Turtle
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# for i in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(i)

# Generate a random walk
def generate_random_walk(steps):
    for _ in range(steps):
        tim.color(random.choice(colours))
        tim.forward(30)
        tim.setheading(random.choice(diricetions))


generate_random_walk(100)

screen = Screen()
screen.exitonclick()
