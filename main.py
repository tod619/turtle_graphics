# A project to explore the Turtle module
# 15/06/2023

from turtle import Turtle, Screen

tim = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# Draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# Draw a dashed line
for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()
