class Cardinal():

    Sud = "Sud"
    Ouest = "Ouest"
    Est = "Est"
    Nord = "Nord"

    def __init__(self, value):
        self._value = value

    def __eq__(self, otherCardinal):
        return self._value == otherCardinal._value

class Orientation:

    def __init__(self, cardinal:Cardinal):
        self._cardinal = cardinal

    def __eq__(self, otherOrientation):
        return self._cardinal == otherOrientation._cardinal

    def tournedroite(self):
        if self._cardinal == Cardinal("Sud"): return Cardinal("Ouest")



class Position:
    
    def __init__(self, y=0, x=0):
        self._y = y
        self._x = x
        self._position = x, y
        
    def __eq__(self, otherPosition):
        return self._position == otherPosition._position
    
    def avance(self):
        if self._cardinal == Cardinal("Sud"): return self.y == self.y - 1
        if self._cardinal == Cardinal("Nord"): return self.y == self.y + 1
        if self._cardinal == Cardinal("Est"): return self.x == self.x + 1
        if self._cardinal == Cardinal("Ouest"): return self.x == self.x - 1
        if self.x > 10: return self.x == 10
        if self.x < 0: return self.x == 0
        if self.y > 10: return self.y == 0
        if self.y < 0: return self.y == 10

        #je suis pas sure du return ._. mais il faut récuperer position
        return self._position == self.x, self.y

    def recule(self):
        if self._cardinal == Cardinal("Sud"): return self.y == self.y + 1
        if self._cardinal == Cardinal("Nord"): return self.y == self.y - 1
        if self._cardinal == Cardinal("Est"): return self.x == self.x - 1
        if self._cardinal == Cardinal("Ouest"): return self.x == self.x + 1
        if self.x > 10: return self.x == 10
        if self.x < 0: return self.x == 0
        if self.y > 10: return self.y == 0
        if self.y < 0: return self.y == 10

        #je suis pas sure du return ._. mais il faut récuperer position
        return self._position == self.x, self.y


class Rover:

    def __init__(self, orientation: Orientation, position: Position):
        self._orientation = orientation
        self._position = position
    
    def getOrientation(self):
        return self._orientation

    def getPosition(self):
        return self._position

    def tournedroite(self):
        self._orientation.tournedroite()

    def avance(self):
        self._position.avance()
