import turtle as t4

c = input("Geben Sie die Farbe ein (z.B: red, green, yellow,... )")
t4.color(c)
t4.fillcolor(c)


t4.penup()
t4.goto(-100,-100)
t4.pendown()

t4.begin_fill()
for i in range(4):
    t4.forward(200)
    t4.left(90)

t4.end_fill()
t4.done()