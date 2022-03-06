import turtle
import time

t = turtle.Turtle()
screen = turtle.Screen ( )
screen.bgcolor("skyblue")

#flower
# Set initial position
turtle.penup ()
turtle.left (90)
turtle.fd (10)
turtle.pendown ()
turtle.right (90)
 
# flower base
turtle.fillcolor ("red")
turtle.begin_fill ()
turtle.pensize(3)
turtle.speed (200)
turtle.circle (10,180)
turtle.circle (25,110)
turtle.left (50)
turtle.circle (60,45)
turtle.circle (20,170)
turtle.right (24)
turtle.fd (30)
turtle.left (10)
turtle.circle (30,110)
turtle.fd (20)
turtle.left (40)
turtle.circle (90,70)
turtle.circle (30,150)
turtle.right (30)
turtle.fd (15)
turtle.circle (80,90)
turtle.left (15)
turtle.fd (45)
turtle.right (165)
turtle.fd (20)
turtle.left (155)
turtle.circle (150,80)
turtle.left (50)
turtle.circle (150,90)
turtle.end_fill ()
 
# Petal 1
turtle.left (150)
turtle.circle (-90,70)
turtle.left (20)
turtle.circle (75,105)
turtle.setheading (60)
turtle.circle (80,98)
turtle.circle (-90,40)
 
# Petal 2
turtle.left (180)
turtle.circle (90,40)
turtle.circle (-80,98)
turtle.setheading (-83)
 
# Leaves 1
turtle.fd (30)
turtle.left (90)
turtle.fd (25)
turtle.left (45)
turtle.fillcolor ("green")
turtle.begin_fill ()
turtle.circle (-80,90)
turtle.right (90)
turtle.circle (-80,90)
turtle.end_fill ()
turtle.right (135)
turtle.fd (60)
turtle.left (180)
turtle.fd (85)
turtle.left (90)
turtle.fd (80)
 
# Leaves 2
turtle.right (90)
turtle.right (45)
turtle.fillcolor ("green")
turtle.begin_fill ()
turtle.circle (80,90)
turtle.left (90)
turtle.circle (80,90)
turtle.end_fill ()
turtle.left (135)
turtle.fd (60)
turtle.left (180)
turtle.fd (60)
turtle.right (90)
turtle.circle (200,60)

t.penup()
t.goto(-80,300)
time.sleep(1)
t.pendown()
t.shapesize(1,2,1)

sun = turtle.Turtle()

# define function
# for drawing rays of Sun
def drawFourRays(t, length, radius):
	
	for i in range(4):
		t.penup()
		t.forward(radius)
		t.pendown()
		t.forward(length)
		t.penup()
		t.backward(length + radius)
		t.left(90)


# Draw circle
# to make sun
sun.penup()
sun.goto(85, 310)
sun.fillcolor("yellow")
sun.pensize(3)
sun.speed(10)
sun.pendown()
sun.begin_fill()
sun.circle(45)
sun.end_fill()

# Use the defined
# function to draw rays
sun.penup()
sun.goto(85, 359)
sun.pensize(3)
sun.speed(10)
sun.pendown()
drawFourRays(sun, 85, 54)
sun.right(45)
drawFourRays(sun, 85, 54)
sun.left(45)
# end sun