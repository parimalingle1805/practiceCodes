import random
import turtle
import math

random.seed(2023)


SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000
COLORS = ["red", "green", "blue"]
AXIS_LEN = 1000
FLIP_ANGLE = 180
AXIS_SIDE = 500
NINETY_DEG = 90
INIT_SQR_LEN = 50
LEN_INCREASE = 10
FORTY_FIVE_ANGLE = 45

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
t = turtle.Turtle()

for i in range(20):
    t.speed(0)
    t.color(COLORS[random.randint(0, len(COLORS) - 1)])
    t.forward(INIT_SQR_LEN)
    t.left(NINETY_DEG)
    t.forward(INIT_SQR_LEN)
    t.left(NINETY_DEG)
    t.forward(INIT_SQR_LEN)
    t.left(NINETY_DEG)
    t.forward(INIT_SQR_LEN)
    t.penup()
    t.forward(LEN_INCREASE)
    t.right(NINETY_DEG)
    t.forward(LEN_INCREASE)
    t.left(FLIP_ANGLE)
    INIT_SQR_LEN += LEN_INCREASE * 2
    t.pendown()
t.penup()
t.forward(LEN_INCREASE)
t.left(NINETY_DEG)
t.forward(LEN_INCREASE)
t.right(NINETY_DEG)
t.right(FORTY_FIVE_ANGLE)
t.pendown()
INIT_SQR_LEN -= LEN_INCREASE * 2
RADII = math.sqrt(math.pow(INIT_SQR_LEN, 2) + math.pow(INIT_SQR_LEN, 2)) / 2
t.circle(RADII)


t.screen.mainloop()