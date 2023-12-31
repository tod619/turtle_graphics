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


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim2.color(random_color())
        tim2.circle(100)
        tim2.setheading(tim2.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
