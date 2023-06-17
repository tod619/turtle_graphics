# import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim3 = turtle_module.Turtle()
tim3.speed("fastest")

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
color_list = [(139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162), (151, 68, 58), (137, 68, 76), (229, 212, 107), (47, 36, 41), (145, 29, 36), (28, 53, 47), (55, 108, 89),
              (228, 167, 173), (189, 99, 107), (139, 33, 28), (194, 92, 79), (49, 40, 36), (228, 173, 166), (20, 92, 69), (177, 189, 212), (29, 62, 107), (113, 123, 155), (172, 202, 190), (51, 149, 193), (166, 200, 213)]

tim3.penup()
tim3.hideturtle()
tim3.setheading(225)
tim3.forward(300)
tim3.setheading(0)

number_of_dots = 101


for dot_count in range(1, number_of_dots):
    tim3.dot(20, random.choice(color_list))
    tim3.forward(50)

    if dot_count % 10 == 0:
        tim3.setheading(90)
        tim3.forward(50)
        tim3.setheading(180)
        tim3.forward(500)
        tim3.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
