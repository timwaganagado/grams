import turtle
t = turtle.Turtle()

turtle.bgcolor("lightblue")
t.pen(fillcolor = "white",pensize="5")
t.begin_fill()
t.right(45)
t.forward(100)
for x in range(2):
    t.left(90)
    t.forward(100)
t.left(90)
t.forward(200)
for x in range(3):
    t.right(90)
    t.forward(100)
t.end_fill()
turtle.done()