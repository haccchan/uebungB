import turtle as t2

t2.hideturtle()

def zeichnen():
    t2.penup()
    t2.goto(-150, 100)
    t2.pendown()
    for i in range(2):
        t2.forward(100)
        t2.dot(10)
        t2.right(90)
        t2.forward(100)
        t2.dot(5)
        t2.left(90)

for i in range(16):
    zeichnen()
    t2.right(360/14)

t2.done()
