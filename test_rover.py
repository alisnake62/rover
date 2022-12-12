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
        rover.axe_x = 5
        rover.axe_y = 5
        self.cardinal = "Nord"

        # Action
        rover.avance()
        
        # Assert
        self.assertEqual("6 5 Nord", rover.position())

    def test_recule(self):
        # Arrange
        rover = Rover()
        rover.axe_x = 5
        rover.axe_y = 5
        self.cardinal = "Nord"

        # Action
        rover.avance()
        
        # Assert
        self.assertEqual("4 5 Nord", rover.position())

    def test_limite_map(self):
        # Arrange
        rover = Rover()
        rover.axe_x = 10
        rover.axe_y = 5
        self.cardinal = "Nord"

        # Action
        rover.avance()
        
        # Assert
        self.assertEqual("0 5 Nord", rover.position())

    def test_tourne_gauche(self):
        # Arrange
        rover = Rover()
        rover.axe_x = 5
        rover.axe_y = 5
        self.cardinal = "Nord"

        # Action
        rover.tourne_gauche()
        
        # Assert
        self.assertEqual("5 5 Ouest", rover.position())

    def test_tourne_droite(self):
        # Arrange
        rover = Rover()
        rover.axe_x = 5
        rover.axe_y = 5
        self.cardinal = "Nord"

        # Action
        rover.tourne_droite()
        
        # Assert
        self.assertEqual("5 5 Est", rover.position())
        
    


if __name__ == '__main__':
    unittest.main()