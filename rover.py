# class Cardinal():

#     Sud = "Sud"
#     Ouest = "Ouest"
#     Est = "Est"
#     Nord = "Nord"

#     def __init__(self, value):
#         self._value = value

#     def __eq__(self, otherCardinal):
#         return self._value == otherCardinal._value

# class Orientation():

#     def __init__(self, cardinal:Cardinal):
#         self._cardinal = cardinal

#     #besoin d'explication pour cette methode
#     def __eq__(self, otherOrientation):
#         return self._cardinal == otherOrientation._cardinal

#     def tourne_droite(self):
#         if self._cardinal == Cardinal("Nord"): return Cardinal("Est")
        

class Position():
    
    def __init__(self, point_y, point_x, cardinal):
        self.cardinal = cardinal
        self.axe_y = point_y
        self.axe_x = point_x

    def position(self):
        print(self.axe_y, self.axe_x, self.cardinal)

class Deplacement(Position):

    def avance(self):
        #avancement enfonction de la direction
        if self.cardinal == "Sud":     self.axe_y += -1
        if self.cardinal == "Nord":    self.axe_y += 1
        if self.cardinal == "Est":     self.axe_x += 1
        if self.cardinal == "Ouest":   self.axe_x += -1

        #verification qu'il soit toujours sur la map
        if self.axe_x > 10: self.axe_x = 10
        if self.axe_x < 0:  self.axe_x = 0
        if self.axe_y > 10: self.axe_y = 0
        if self.axe_y < 0:  self.axe_y = 10

    def recule(self):
        #recule enfonction de la direction
        if self.cardinal == "Sud":     self.axe_y += 1
        if self.cardinal == "Nord":    self.axe_y += -1
        if self.cardinal == "Est":     self.axe_x += -1
        if self.cardinal == "Ouest":   self.axe_x += 1

        #verification qu'il soit toujours sur la map
        if self.axe_x > 10: self.axe_x = 10
        if self.axe_x < 0:  self.axe_x = 0
        if self.axe_y > 10: self.axe_y = 0
        if self.axe_y < 0:  self.axe_y = 10

    def tourne_droite(self):
        test=1  
        #change de direction vers la droite
        if self.cardinal == "Sud" and test == 1:     
            self.cardinal = "Ouest" 
            test = 2
        if self.cardinal == "Ouest" and test == 1:   
            self.cardinal = "Nord"
            test = 2
        if self.cardinal == "Nord" and test == 1:    
            self.cardinal = "Est"
            test = 2
        if self.cardinal == "Est" and test == 1:     
            self.cardinal = "Sud"
            test = 2

    def tourne_gauche(self):
        test=1  
        #change de direction vers la gauche
        if self.cardinal == "Sud" and test == 1: 
            self.cardinal = "Est" 
            test = 2
        if self.cardinal == "Est" and test == 1:     
            self.cardinal = "Nord"
            test = 2
        if self.cardinal == "Nord" and test == 1:    
            self.cardinal = "Ouest"
            test = 2
        if self.cardinal == "Ouest" and test == 1:   
            self.cardinal = "Sud"
            test = 2


class Rover(Deplacement):

    def __init__(self):

        #direction entre ( Nord | Sud | Est | Ouest )
        self.cardinal = "Nord"

        #axe Y n'import qu'elle chiffre 
        self.axe_y = 5

        #axe X n'import qu'elle chiffre 
        self.axe_x = 5


###########   test   ############
# rover = Rover()
# print("Y|X|Direction")
# rover.position()
# rover.avance()
# rover.position()

