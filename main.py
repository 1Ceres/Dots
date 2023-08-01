# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 55)
# extracted = []
# print(len(colors))
#
# for i in range(33):
#     extracted.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))
# print(extracted)
# list of rgb colors extracted from image
colors_list = [(240, 242, 245), (223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159),
               (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84),
               (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90),
               (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109),
               (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210),
               (77, 37, 76), (120, 117, 155), (35, 35, 35)]

import turtle
import random
screen = turtle.Screen()
screen.screensize(250, 250)
turtle.colormode(255)

t = turtle.Turtle()

t.speed(0)
turtle.setworldcoordinates(-400, -350, 150, 200)
t.penup()
t.ht()
start = -300
t.goto(-350, start)
for i in range(10):
    for j in range(10):
        t.dot(20, random.choice(colors_list))
        t.fd(50)
    start += 50
    t.goto(-350, start)

screen.exitonclick()
