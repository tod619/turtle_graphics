# A project to explore the Turtle module
# 15/06/2023

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

screen = Screen()
screen.exitonclick()
