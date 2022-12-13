import random
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

    def valeur_Y(self):
        print(self.axe_y)

    def valeur_X(self):
        print(self.axe_x)
    
    def valeur_orientation(self):
        print(self.cardinal)

    def position(self):
        print(self.axe_y, self.axe_x, self.cardinal)


class Deplacement(Position):

    def traitement_depassement_limite_teste_avance(position_avant_avance):
        if position_avant_avance > 10: position_avant_avance = 0
        if position_avant_avance < 0:  position_avant_avance = 10

    def traitement_depassement_limite_teste_recule(position_avant_recule):
        if position_avant_recule > 10: position_avant_recule = 0
        if position_avant_recule < 0:  position_avant_recule = 10

    def traitement_des_dépassement_de_limite(self):
        # verification qu'il soit toujours sur la map
        if self.axe_x > 10: self.axe_x = 0
        if self.axe_x < 0:  self.axe_x = 10
        if self.axe_y > 10: self.axe_y = 0
        if self.axe_y < 0:  self.axe_y = 10

    def avance(self):
        #avancement enfonction de la direction
        if self.cardinal == "Sud":     self.axe_y = self.axe_y - 1
        if self.cardinal == "Nord":    self.axe_y = self.axe_y + 1
        if self.cardinal == "Est":     self.axe_x = self.axe_x + 1
        if self.cardinal == "Ouest":   self.axe_x = self.axe_x - 1
        self.traitement_des_dépassement_de_limite()

    def recule(self):
        #recule enfonction de la direction
        if self.cardinal == "Sud":     self.axe_y = self.axe_y + 1
        if self.cardinal == "Nord":    self.axe_y = self.axe_y - 1
        if self.cardinal == "Est":     self.axe_x = self.axe_x - 1
        if self.cardinal == "Ouest":   self.axe_x = self.axe_x + 1
        self.traitement_des_dépassement_de_limite()

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

    # definie une position et une orientation "random" au Rover
    def __init__(self):
        self.cardinal = random.choice(["Nord", "Sud", "Est", "Ouest"])

        self.axe_y = random.randint(0, 10)

        self.axe_x = random.randint(0, 10)
        