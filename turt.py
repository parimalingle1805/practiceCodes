import turtle
import math

#avoid magic numbers
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SKIP_DISTANCE = 40
SIDE_LENGTH = 60
NINETY_DEGREE = 90
REVERSE_DEGREE = 180
RADIUS = 70
triangle_side = 100
equilateral_angle = 120

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

t = turtle.Turtle()

t.speed(2)  #1-10 #1-slowest

t.forward(triangle_side)
t.left(equilateral_angle)
t.forward(triangle_side)
t.left(equilateral_angle)
t.forward(triangle_side)
t.left(equilateral_angle)

t.penup()
t.forward(triangle_side / 2)
t.pendown()
#t.left(NINETY_DEGREE)

median_length = math.sqrt(math.pow(triangle_side, 2) - math.pow(triangle_side / 2, 2))
radius = median_length / 3
t.circle(radius)









# t.forward(200)


# #move right without drawing
# t.penup()
# t.forward(SKIP_DISTANCE)
# t.pendown()

# #reverse and draw a green circle
# t.right(REVERSE_DEGREE)
# t.color("green")
# t.circle(RADIUS)

# #reverse and draw a blue square
# t.right(REVERSE_DEGREE)
# t.color("blue")
# t.forward(SIDE_LENGTH)
# t.left(NINETY_DEGREE)
# t.forward(SIDE_LENGTH)
# t.left(NINETY_DEGREE)
# t.forward(SIDE_LENGTH)
# t.left(NINETY_DEGREE)
# t.forward(SIDE_LENGTH)











t.screen.mainloop()  #last statement #To keep the screen open



