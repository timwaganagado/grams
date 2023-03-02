import turtle
import random

turtle.getscreen()

y = 10
for x in range(random.randint(0,20)):
    turtle.left(random.randint(30,50))
    turtle.forward(y)
    y += 5

angle = 15
for x in range(8):
    turtle.home()
    turtle.left(angle)
    turtle.forward(100)
    angle+=60
turtle.done()