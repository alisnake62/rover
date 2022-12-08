class Cardinal():

    Sud = "Sud"
    Ouest = "Ouest"
    Est = "Est"
    Nord = "Nord"

    def __init__(self, value):
        self._value = value

    def __eq__(self, otherCardinal):
        return self._value == otherCardinal._value

# class Orientation():

#     def __init__(self, cardinal:Cardinal):
#         self._cardinal = cardinal

#     #besoin d'explication pour cette methode
#     def __eq__(self, otherOrientation):
#         return self._cardinal == otherOrientation._cardinal

#     def tourne_droite(self):
#         if self._cardinal == Cardinal("Nord"): return Cardinal("Est")
        

class Position():
    
    def __init__(self, point_y, point_x, cardinal: Cardinal):
        self._cardinal = cardinal
        self.axe_y = point_y
        self.axe_x = point_x

    def position(self):
        print(self.axe_y, self.axe_x, self._cardinal)

class Deplacement(Position):

    def avance(self):
        #avancement enfonction de la direction
        if self._cardinal == "Sud":     self.axe_y += -1
        if self._cardinal == "Nord":    self.axe_y += 1
        if self._cardinal == "Est":     self.axe_x += 1
        if self._cardinal == "Ouest":   self.axe_x += -1

        #verification qu'il soit toujours sur la map
        if self.axe_x > 10: self.axe_x == 10
        if self.axe_x < 0:  self.axe_x == 0
        if self.axe_y > 10: self.axe_y == 0
        if self.axe_y < 0:  self.axe_y == 10

    def recule(self):
        #recule enfonction de la direction
        if self._cardinal == "Sud":     self.axe_y += 1
        if self._cardinal == "Nord":    self.axe_y += -1
        if self._cardinal == "Est":     self.axe_x += -1
        if self._cardinal == "Ouest":   self.axe_x += 1

        #verification qu'il soit toujours sur la map
        if self.axe_x > 10: self.axe_x == 10
        if self.axe_x < 0:  self.axe_x == 0
        if self.axe_y > 10: self.axe_y == 0
        if self.axe_y < 0:  self.axe_y == 10

    def tourne_droite(self):
        #change de direction vers la droite
        if self._cardinal == "Sud":     self._cardinal == "Ouest"
        if self._cardinal == "Ouest":   self._cardinal == "Nord"
        if self._cardinal == "Nord":    self._cardinal == "Est"
        if self._cardinal == "Est":     self._cardinal == "Sud"

    def tourne_gauche(self):
        #change de direction vers la gauche
        if self._cardinal == "Sud":     self._cardinal == "Est"
        if self._cardinal == "Est":     self._cardinal == "Nord"
        if self._cardinal == "Nord":    self._cardinal == "Ouest"
        if self._cardinal == "Ouest":   self._cardinal == "Sud"


class Rover(Deplacement):

    def __init__(self):
        self._cardinal = "Nord"
        self.axe_y = 5
        self.axe_x = 5


###########   test   ############
rover = Rover()

rover.position()

rover.tourne_droite()

rover.position()



