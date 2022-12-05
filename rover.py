class Cardinal():

    Sud = "Sud"
    Ouest = "Ouest"

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

class Position(Orientation):

    #j'ai besoin que tu finisses Orientation() ^^
    
    def __init__(self, cordonner):
        self._cordonner = cordonner
        
    def __eq__(self, otherPosition):
        return self._cordonner == otherPosition._cordonner

class Deplacement(Position):

    def __init__(self, cardinal:Cardinal, position:Position):
        self._cardinal = cardinal
        self._position = position
    
    def avance(self):
        # a enlever
        x = 5
        y = 5
        #
        if self._cardinal == Cardinal("Sud"): return y == y - 1
        if self._cardinal == Cardinal("Nord"): return y == y + 1 
        if self._cardinal == Cardinal("Est"): return x == x + 1
        if self._cardinal == Cardinal("Ouest"): return x == x - 1
        if x > 10: return x == 10
        if x < 0: return x == 0
        if y > 10: return y == 0
        if y < 0: return y == 10

    def recule(self):
        # a enlever
        x = 5
        y = 5
        #
        if self._cardinal == Cardinal("Sud"): return y == y + 1 
        if self._cardinal == Cardinal("Nord"): return y == y - 1
        if self._cardinal == Cardinal("Est"): return x == x - 1
        if self._cardinal == Cardinal("Ouest"): return x == x + 1
        if x > 10: return x == 10
        if x < 0: return x == 0
        if y > 10: return y == 0
        if y < 0: return y == 10


class Rover:

    def __init__(self, orientation: Orientation):
        self._orientation = orientation

    def getOrientation(self):
        return self._orientation

    def tournedroite(self):
        self._orientation.tournedroite()
