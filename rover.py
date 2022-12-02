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

class Rover:

    def __init__(self, orientation: Orientation):
        self._orientation = orientation

    def getOrientation(self):
        return self._orientation

    def tournedroite(self):
        self._orientation.tournedroite()
