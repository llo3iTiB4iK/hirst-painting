# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
#
# print(rgb_colors)
from turtle import Turtle, Screen, colormode
from random import choice

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

colormode(255)
pointer = Turtle()
pointer.speed("fastest")
pointer.penup()
pointer.hideturtle()

for i in range(10):
    pointer.setheading(225)
    pointer.forward(300)
    pointer.setheading(0)
    pointer.sety(pointer.ycor() + 50 * i)
    for _ in range(10):
        pointer.dot(20, choice(color_list))
        pointer.forward(50)
    pointer.home()

screen = Screen()
screen.exitonclick()
