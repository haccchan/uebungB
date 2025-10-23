import turtle

t1 = turtle.Turtle()

t1.penup()
t1.goto(100, 0)
t1.pendown()
t1.hideturtle()

for i in range(4):
    t1.forward(200)
    t1.left(90)

t1.penup()
t1.goto(100, 100 )
t1.pendown()
t1.right(45)

for i in range(4):
    t1.forward(140)
    t1.left(90)

r = float(input("Ratio (z.B: 1.0, 0.5,...): "))

t1.left(45)
t1.penup()
t1.goto(-200, 0)
t1.pendown()
t1.hideturtle()

for i in range(4):
    t1.forward(r * 200)
    t1.left(90)

t1.penup()
t1.goto(-200, r * 100 )
t1.pendown()
t1.right(45)

for i in range(4):
    t1.forward(r * 140)
    t1.left(90)

turtle.done()
