
class Punkt:
    def __init__(self, x : float = 0, y : float = 0):
        self._x = x
        self._y = y

    def distance(self, punkt):
        dx = punkt._x - self._x
        dy = punkt._y - self._y
        return (dx**2 + dy**2)**0.5

    def shift(self, x_val, y_val):
        self._x = self._x + x_val
        self._y = self._y + y_val

    def show(self):
        print("Punkt(" + str(self._x) + ", " + str(self._y) + ")")

import math

class Circle:
    def __init__(self, x : float = 0, y : float = 0, radius : float = 1):
        self._radius = radius
        self._x = x
        self._y = y

    def distance(self, k):
        dx = k._x - self._x
        dy = k._y - self._y
        return math.sqrt(dx * dx + dy * dy)

    def shift(self,x_val,y_val):
        self._x = self._x + x_val
        self._y = self._y + y_val

    def show(self):
        print("Kreis: Mittelpunkt(" + str(self._x) + ", " + str(self._y) + "). Radius: " + str(self._radius))

    def scale(self,factor):
        self._radius = self._radius * factor

    def contains(self,p):
        if self.distance(p) < self._radius:
            return True
        else:
            return False

    def intersect(self,c):
        if c._radius < self._radius:
            return True
        else:
            return False


p1 = Punkt()
p1.show()
p1.shift(2,1)
p1.show()
p2 = Punkt(3,1)
p2.show()
print(p1.distance(p2))

k1 = Circle()
k1.show()
k1.shift(2,1)
k1.show()
k1.scale(2)
k1.show()
print(k1.contains(p1))
k2 = Circle(3,4,3)
k2.show()
print(k2.contains(p1))
print(k2.intersect(k1))