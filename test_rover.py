import unittest

from rover import Rover

class TestRover(unittest.TestCase):


    # def test_tourne_droite_1(self):
    #     # Arrange
    #     rover = Rover(orientation=Orientation(cardinal="Sud))

    #     # Action
    #     rover.tournedroite()

    #     # Assert
    #     currentOrientation = rover.getOrientation()
    #     self.assertEqual(currentOrientation, Orientation("Ouest"))

    def test_avance(self):
        # Arrange
        rover = Rover()

        # Action et # Assert
        if rover.valeur_orientation == "Nord":
            position_avant_avance = rover.valeur_Y
            position_avant_avance = position_avant_avance + 1
            rover.traitement_de_un_depassement_de_limite_pour_teste_avance(position_avant_avance)
            rover.avance()
            position_apres_avance = rover.valeur_Y

            self.assertEqual(position_avant_avance, position_apres_avance)
            

        if rover.valeur_orientation == "Sud":
            position_avant_avance = rover.valeur_Y
            rover.avance()
            position_avant_avance = position_avant_avance - 1
            position_apres_avance = rover.valeur_Y

            self.assertEqual(position_avant_avance, position_apres_avance)

        if rover.valeur_orientation == "Est":
            position_avant_avance = rover.valeur_X
            rover.avance()
            position_avant_avance = position_avant_avance - 1
            position_apres_avance = rover.valeur_Y

            self.assertEqual(position_avant_avance, position_apres_avance)


        if rover.valeur_orientation == "Ouest":
            position_avant_avance = rover.valeur_X
            position_avant_avance = position_avant_avance + 1
            rover.avance()
            position_apres_avance = rover.valeur_Y

            self.assertEqual(position_avant_avance, position_apres_avance)

    # def test_recule(self):
    #     # Arrange
    #     rover = Rover()
    #     rover.axe_x = 5
    #     rover.axe_y = 5
    #     self.cardinal = "Nord"

    #     # Action
    #     rover.avance()
        
    #     # Assert
    #     self.assertEqual("4 5 Nord", rover.position())

    # def test_limite_map(self):
    #     # Arrange
    #     rover = Rover()
    #     rover.axe_x = 10
    #     rover.axe_y = 5
    #     self.cardinal = "Nord"

    #     # Action
    #     rover.avance()
        
    #     # Assert
    #     self.assertEqual("0 5 Nord", rover.position())

    # def test_tourne_gauche(self):
    #     # Arrange
    #     rover = Rover()
    #     rover.axe_x = 5
    #     rover.axe_y = 5
    #     self.cardinal = "Nord"

    #     # Action
    #     rover.tourne_gauche()
        
    #     # Assert
    #     self.assertEqual("5 5 Ouest", rover.position())

    # def test_tourne_droite(self):
    #     # Arrange
    #     rover = Rover()
    #     rover.axe_x = 5
    #     rover.axe_y = 5
    #     self.cardinal = "Nord"

    #     # Action
    #     rover.tourne_droite()
        
    #     # Assert
    #     self.assertEqual("5 5 Est", rover.position())
        
    

if __name__ == '__main__':
    unittest.main()