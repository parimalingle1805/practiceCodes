import turtle, math, random


random.seed(2023)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SIDE_LENGTH = 60
NINETY_DEGREE = 90
REVERSE_DEGREE = 180
RADIUS = 50



screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

t = turtle.Turtle()

t.speed(0)

t.penup()
t.forward(200)
t.left(NINETY_DEGREE)
t.forward(200)
t.right(NINETY_DEGREE)
t.forward(50)
t.left(NINETY_DEGREE)
t.pendown()
t.circle(50)
t.penup()
t.home()

t.left(NINETY_DEGREE)
t.penup()
t.forward(200)
t.left(NINETY_DEGREE)
t.forward(200)
t.right(NINETY_DEGREE)
t.forward(50)
t.left(NINETY_DEGREE)
t.pendown()
t.circle(50)
t.penup()
t.home()

t.left(180)
t.penup()
t.forward(200)
t.left(NINETY_DEGREE)
t.forward(200)
t.right(NINETY_DEGREE)
t.forward(50)
t.left(NINETY_DEGREE)
t.pendown()
t.circle(50)
t.penup()
t.home()
t.pendown()

t.left(270)
t.penup()
t.forward(200)
t.left(NINETY_DEGREE)
t.forward(200)
t.right(NINETY_DEGREE)
t.forward(50)
t.left(NINETY_DEGREE)
t.pendown()
t.circle(50)
t.penup()
t.home()
t.pendown()


cnt = 0
while cnt < 4:
    rand_angle = random.uniform(0, 360)
    rand_dist = random.uniform(0, 500)
    distance = math.sqrt(rand_dist ** 2)

    coordinate = (distance * math.cos(rand_angle), distance * math.sin(rand_angle))
    print(coordinate)
    x = coordinate[0]
    y = coordinate[1]
    if math.sqrt(abs(x - 200) + abs(y - 200)) >=30 or math.sqrt(abs(x + 200) + abs(y - 200)) >= 30 or math.sqrt(abs(x - 200) + abs(y + 200)) >= 30 or math.sqrt(abs(x + 200) + abs(y + 200)) >= 30:
        cnt += 1 

        t.left(rand_angle)
        t.forward(rand_dist)
        t.home()










t.screen.mainloop() 



