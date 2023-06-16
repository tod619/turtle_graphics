# A project to explore the Turtle module
# 15/06/2023

from turtle import Turtle, Screen

tim = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# Draw a square
for i in range(4):
    tim.forward(100)
    tim.left(90)

screen = Screen()
screen.exitonclick()
