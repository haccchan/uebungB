import turtle as t

t.penup()
t.goto(-50, -50)
t.pendown()

# Vier Farben, weil gegenüberliegende Ecken gleiche Farben haben sollen
colors = ["red", "blue", "green", "yellow"]

# Acht Farbenliste erstellen (jede Farbe zweimal)
color_cycle = colors * 2   # => ["red","blue","green","yellow","red","blue","green","yellow"]

for i in range(8):
    t.dot(20, color_cycle[i])
    t.forward(80)     # Seitenlänge beliebig
    t.left(45)        # 360° / 8 = 45 Grad

t.done()