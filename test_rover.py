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

        # Action 
        if rover.valeur_orientation == "Nord":
            position_avant_avance = rover.valeur_Y
            position_avant_avance = position_avant_avance + 1
            rover.traitement_depassement_limite_teste_avance(position_avant_avance)
            rover.avance()
            position_apres_avance = rover.valeur_Y
            # Assert
            self.assertEqual(position_avant_avance, position_apres_avance)
            
        # Action 
        if rover.valeur_orientation == "Sud":
            
            position_avant_avance = rover.valeur_Y
            position_avant_avance = position_avant_avance - 1
            rover.traitement_depassement_limite_teste_avance(position_avant_avance)
            rover.avance()
            position_apres_avance = rover.valeur_Y
            # Assert
            self.assertEqual(position_avant_avance, position_apres_avance)

        # Action 
        if rover.valeur_orientation == "Est":
            position_avant_avance = rover.valeur_X
            position_avant_avance = position_avant_avance + 1
            rover.traitement_depassement_limite_teste_avance(position_avant_avance)
            rover.avance()
            position_apres_avance = rover.valeur_X
            # Assert
            self.assertEqual(position_avant_avance, position_apres_avance)

        # Action 
        if rover.valeur_orientation == "Ouest":
            position_avant_avance = rover.valeur_X
            position_avant_avance = position_avant_avance - 1
            rover.traitement_depassement_limite_teste_avance(position_avant_avance)
            rover.avance()
            position_apres_avance = rover.valeur_X
            # Assert
            self.assertEqual(position_avant_avance, position_apres_avance)

    def test_recule(self):
        # Arrange
        rover = Rover()

        # Action
        if rover.valeur_orientation == "Nord":
            position_avant_recule = rover.valeur_Y
            position_avant_recule = position_avant_recule + 1
            rover.traitement_depassement_limite_teste_recule(position_avant_recule)
            rover.avance()
            position_apres_recule = rover.valeur_Y
            # Assert
            self.assertEqual(position_avant_recule, position_apres_recule)
            
        # Action
        if rover.valeur_orientation == "Sud":
            
            position_avant_recule = rover.valeur_Y
            position_avant_recule = position_avant_recule - 1
            rover.traitement_depassement_limite_teste_recule(position_avant_recule)
            rover.avance()
            position_apres_recule = rover.valeur_Y
            # Assert
            self.assertEqual(position_avant_recule, position_apres_recule)

        # Action
        if rover.valeur_orientation == "Est":
            position_avant_recule = rover.valeur_X
            position_avant_recule = position_avant_recule + 1
            rover.traitement_depassement_limite_teste_recule(position_avant_recule)
            rover.avance()
            position_apres_recule = rover.valeur_X
            # Assert
            self.assertEqual(position_avant_recule, position_apres_recule)

        # Action
        if rover.valeur_orientation == "Ouest":
            position_avant_recule = rover.valeur_X
            position_avant_recule = position_avant_recule - 1
            rover.traitement_depassement_limite_teste_recule(position_avant_recule)
            rover.avance()
            position_apres_recule = rover.valeur_X
            # Assert
            self.assertEqual(position_avant_recule, position_apres_recule)


    def test_tourne_gauche(self):
        # Arrange
        rover = Rover()

        if rover.cardinal == "Nord":
            avant_tourne = "Ouest"
            rover.tourne_gauche()
            apres_tourne = rover.cardinal
            # Assert
            self.assertEqual(avant_tourne, apres_tourne)

        if rover.cardinal == "Sud":
            avant_tourne = "Est"
            rover.tourne_gauche()
            apres_tourne = rover.cardinal
            # Assert
            self.assertEqual(avant_tourne, apres_tourne)

        if rover.cardinal == "Est":
            avant_tourne = "Nord"
            rover.tourne_gauche()
            apres_tourne = rover.cardinal
            # Assert
            self.assertEqual(avant_tourne, apres_tourne)

        if rover.cardinal == "Ouest":
            avant_tourne = "Sud"
            rover.tourne_gauche()
            apres_tourne = rover.cardinal
            # Assert
            self.assertEqual(avant_tourne, apres_tourne)
     
    def test_tourne_droite(self):
        # Arrange
        rover = Rover()

        # Action
        if rover.cardinal == "Nord":
            avant_tourne = "Est"
            rover.tourne_droite()
            apres_tourne = rover.cardinal
            # Assert
            self.assertEqual(avant_tourne, apres_tourne)

        if rover.cardinal == "Sud":
            avant_tourne = "Ouest"
            rover.tourne_droite()
            apres_tourne = rover.cardinal
            # Assert
            self.assertEqual(avant_tourne, apres_tourne)

        if rover.cardinal == "Est":
            avant_tourne = "Sud"
            rover.tourne_droite()
            apres_tourne = rover.cardinal
            # Assert
            self.assertEqual(avant_tourne, apres_tourne)

        if rover.cardinal == "Ouest":
            avant_tourne = "Nord"
            rover.tourne_droite()
            apres_tourne = rover.cardinal
            # Assert
            self.assertEqual(avant_tourne, apres_tourne)

   

if __name__ == '__main__':
    unittest.main()