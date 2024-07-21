import turtle
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SKIP_DISTANCE = 40
SIDE_LENGTH = 60
NINETY_DEGREE = 90
REVERSE_DEGREE = 180
RADIUS = 70
REDUCTION_DIST = 5

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

t = turtle.Turtle()
t.speed(0)

t.penup()
t.forward(100)
t.pendown()

while RADIUS >= 0:
    print(RADIUS)
    t.circle(RADIUS)
    RADIUS -= 5
    t.penup()
    t.left(NINETY_DEGREE)
    t.forward(REDUCTION_DIST)
    t.right(NINETY_DEGREE)
    t.pendown()
t.home()







t.screen.mainloop()