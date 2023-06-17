import turtle as t
import random

t.colormode(255)
tim2 = t.Turtle()
tim2.speed("fastest")
# generate a random RGB Color


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


screen = t.Screen()
screen.exitonclick()
