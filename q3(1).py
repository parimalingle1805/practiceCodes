import random
import turtle

random.seed(2023)


SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000
COLORS = ["beige", "coral", "gold", "blue", "green"]
AXIS_LEN = 1000
FLIP_ANGLE = 180
AXIS_SIDE = 500
NINETY_DEG = 90
INIT_CIRCLE_RAD = 50
RAD_INCREASE = 10
SQUARE_SIDE = 680

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Python Turtle Graphics")
t = turtle.Turtle()
t.speed(10)
#drawing the axes
t.left(FLIP_ANGLE)
t.penup()
t.forward(AXIS_SIDE)
t.pendown()
t.right(FLIP_ANGLE)
t.forward(AXIS_LEN)
# t.left(FLIP_ANGLE)
# t.penup()
# t.forward(AXIS_SIDE)
t.home()
t.left(NINETY_DEG)
t.penup()
t.forward(AXIS_SIDE)
t.pendown()
t.left(FLIP_ANGLE)
t.forward(AXIS_LEN)

t.home()
t.forward(INIT_CIRCLE_RAD - RAD_INCREASE)
# t.left(NINETY_DEG)
for i in range(30):
    t.speed(0)
    t.color(COLORS[random.randint(0, len(COLORS) - 1)])
    t.forward(RAD_INCREASE)
    t.left(NINETY_DEG)
    t.circle(INIT_CIRCLE_RAD)
    INIT_CIRCLE_RAD += 10
    t.right(NINETY_DEG)

t.left(NINETY_DEG) 
t.color("red")
t.forward(SQUARE_SIDE / 2)
t.left(NINETY_DEG)
t.forward(SQUARE_SIDE)
t.left(NINETY_DEG)
t.forward(SQUARE_SIDE)
t.left(NINETY_DEG)
t.forward(SQUARE_SIDE)
t.left(NINETY_DEG)
t.forward(SQUARE_SIDE / 2)


t.screen.mainloop()