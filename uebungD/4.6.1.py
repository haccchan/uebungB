import turtle as t3

t3.penup()
t3.goto(-50,-50)
t3.pendown()

colors = ["red", "blue", "green", "yellow"]
for i in range(4):
    t3.dot(20, colors[i])
    t3.forward(100)
    t3.left(90)

t3.done()