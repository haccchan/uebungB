import math

from uebung913 import Figur

class Punkt:
    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    def distance(self, other: "Punkt") -> float:
        dx = other._x - self._x
        dy = other._y - self._y
        return math.sqrt(dx*dx + dy*dy)

    def shift(self, x_val, y_val):
        self._x += x_val
        self._y += y_val

    def show(self):
        return f"Punkt({self._x}, {self._y})"

class Circle(Figur):
    def __init__(self, x: float = 0, y: float = 0, radius: float = 1):
        self._x = x
        self._y = y
        self._radius = radius
        super().__init__("Kreis")

    def contains(self, p):
        dx = p._x - self._x
        dy = p._y - self._y
        abstand = math.sqrt(dx*dx + dy*dy)
        return abstand <= self._radius

    def intersect(self, c):
        dx = c._x - self._x
        dy = c._y - self._y
        abstand = math.sqrt(dx*dx + dy*dy)
        return abstand <= self._radius + c._radius

    def distance(self, obj):
        dx = obj._x - self._x
        dy = obj._y - self._y
        abstand = math.sqrt(dx*dx + dy*dy)

        if isinstance(obj, Punkt):
            return max(0, abstand - self._radius)

        if isinstance(obj, Circle):
            return max(0, abstand - (self._radius + obj._radius))

    def shift(self, x_val, y_val):
        self._x += x_val
        self._y += y_val

    def scale(self, faktor):
        self._radius *= faktor

    def show(self):
        return f"{self.name}: Mittelpunkt({self._x}, {self._y}), Radius: {self._radius}"

class Polygon(Figur):
    def __init__(self, a: int, c: list[int]):
        self._a = a
        self._c = c
        super().__init__("Polygon")

    def show(self):
        return f"{self.name}(Anzahl Seiten : {self._a}, die Seitenlängen{self._c})"

    def scale(self, faktor):
        for i in range(len(self._c)):
            self._c[i] *= faktor

    def umfang(self):
        s = 0
        for i in range(len(self._c)):
            s += self._c[i]
        return s

class Dreieck(Polygon):
    def ist_gleichseitig(self):
        return self._c[0] == self._c[1]  == self._c[2]

    def ist_gleichschenklig(self):
        return (self._c[0] == self._c[1]) or (self._c[0] == self._c[2]) or (self._c[1] == self._c[2])

    def ist_valid(self):
        return (self._c[0] + self._c[1]) > self._c[2] and (self._c[0] + self._c[2]) > self._c[1] and (self._c[1] + self._c[2]) > self._c[0]

    def flaeche(self):
        u = (self.umfang())/2
        return (u*(u-self._c[0])*(u-self._c[1])*(u-self._c[2]))**(1/2)

    def umkreis_Radius(self):
        return (self._c[0]*self._c[1]*self._c[2]) / (4*self.flaeche())

class Viereck(Polygon):
    def ist_Quadrat(self):
        return self._c[0] == self._c[1] == self._c[2] == self._c[3]

    def ist_Rechteck(self):
        return (self._c[0] == self._c[2]) and (self._c[1] == self._c[3])

    def flaeche(self):
        if self.ist_Rechteck():
            return self._c[0] * self._c[1]
        return None