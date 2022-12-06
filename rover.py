class Cardinal():

    Sud = "Sud"
    Ouest = "Ouest"
    Est = "Est"
    Nord = "Nord"

    def __init__(self, value):
        self._value = value

    def __eq__(self, otherCardinal):
        return self._value == otherCardinal._value

class Orientation():

    def __init__(self, cardinal:Cardinal):
        self._cardinal = cardinal

    #besoin d'explication pour cette methode
    def __eq__(self, otherOrientation):
        return self._cardinal == otherOrientation._cardinal

    def tourne_droite(self):
        if self._cardinal == Cardinal("Sud"): return Cardinal("Ouest")
        if self._cardinal == Cardinal("Ouest"): return Cardinal("Nord")
        if self._cardinal == Cardinal("Nord"): return Cardinal("Est")
        if self._cardinal == Cardinal("Est"): return Cardinal("Sud")

    def tourne_gauche(self):
        if self._cardinal == Cardinal("Sud"): return Cardinal("Est")
        if self._cardinal == Cardinal("Est"): return Cardinal("Nord")
        if self._cardinal == Cardinal("Nord"): return Cardinal("Ouest")
        if self._cardinal == Cardinal("Ouest"): return Cardinal("Sud")

class Position():
    
    def __init__(self, y, x):
        self.axe_y = y
        self.axe_x = x
        self._position = self.axe_y, self.axe_x
        
    def __eq__(self, otherPosition):
        return self._position == otherPosition._position
    
    def avance(self):
        if self._cardinal == Cardinal("Sud"): return self.axe_y == self.axe_y - 1
        if self._cardinal == Cardinal("Nord"): return self.axe_y == self.axe_y + 1
        if self._cardinal == Cardinal("Est"): return self.axe_x == self.axe_x + 1
        if self._cardinal == Cardinal("Ouest"): return self.axe_x == self.axe_x - 1
        if self.axe_x > 10: return self.axe_x == 10
        if self.axe_x < 0: return self.axe_x == 0
        if self.axe_y > 10: return self.axe_y == 0
        if self.axe_y < 0: return self.axe_y == 10
        self._position == self.axe_x, self.axe_y


class Rover():

    def __init__(self, orientation: Orientation, position: Position):
        self._orientation = orientation
        self._position = position
        
    def getOrientation(self):
        return self._orientation

    def getPosition(self):
        return self._position

    def tournedroite(self):
        self._orientation.tourne_droite()

    def avance(self):
        self._position.avance()


##########   tests   ###########
# rover = Rover("Nord",(5,5))
# print(rover._orientation, rover._position)
# rover.avance
# rover.tournedroite
# print(rover._orientation, rover._position)
