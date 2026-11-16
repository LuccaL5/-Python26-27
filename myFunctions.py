
import turtle
bob = turtle.Turtle()

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()


import turtle

bob = turtle.Turtle()


def draw_shape(sides, size, color):
    bob.color(color)

    for times in range(sides):
        bob.forward(size)
        bob.right(360 / sides)
