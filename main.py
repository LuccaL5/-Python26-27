import turtle
from myFunctions import *

turtle.title("Neon Spiral")

turtle.bgcolor("midnightblue")
bob.speed(0)
bob.width(2)

colors = ["cyan", "magenta", "yellow",
          "orange", "lime", "white"]


for times in range(160):

    color = colors[times % 6]
    size = 8 + times * 3

    draw_shape(6, size, color)

    bob.right(9)

bob.hideturtle()
turtle.done()
