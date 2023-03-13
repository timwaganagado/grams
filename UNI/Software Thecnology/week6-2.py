import turtle
import random

t = turtle.Turtle()

turtle.bgcolor("black")
t.penup()
size = turtle.screensize()

def square(size):
    for x in range(4):
        t.forward(size)
        t.left(90)
t.pencolor("white")
for x in range(random.randint(10,15)):
    
    t.penup()
    t.setpos(random.randint(-size[0],size[0]),random.randint(-size[1],size[1]))
    t.pendown()

    t.pen(fillcolor= "white",pensize="2")
    t.begin_fill()
    square(3)
    t.end_fill()
t.penup()
t.setpos((-size[0],0))
print(size)
print(t.pos())
t.pendown()
t.pencolor("grey")
t.pen(fillcolor = "grey",pensize="5")

instruc = [(50,True,50),(40,False,30),(20,True,80),(40,False,30),(40,False,30),(50,True,50),(40,False,30),(20,True,80),(40,False,30),(40,False,30),(50,True,50),(40,False,30),(20,True,80),(40,False,30),(40,False,30), (40,False,30),(50,True,20),(40,False,30),(50,True,20),(40,False,30),(50,True,20)]

t.begin_fill()
for x in instruc:
    t.forward(x[0])
    if x[1]:
        t.left(90)
        t.forward(x[2])
        t.right(90)
    else:
        t.right(90)
        t.forward(x[2])
        t.left(90)

t.setpos((size[0],-size[1]-100))
print(t.pos())
t.setpos((-size[0],-size[1]-100))

t.end_fill()

def window(spotx,spoty):
    t.penup()
    t.goto(spotx,spoty)
    t.pendown()

    t.pen(fillcolor= "white",pensize="2")

    t.begin_fill()
    square(15)
    t.end_fill()

window(-100,100)
window(100,150)

turtle.done()