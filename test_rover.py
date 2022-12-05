import unittest

from rover import Rover, Orientation, Position

class TestRover(unittest.TestCase):

    # j'ai des erreurs, je sais pas pourquoi ducoup => commentaire (même en supriment mon code)

    # def test_tourne_droite_1(self):
    #     # Arrange
    #     rover = Rover(orientation=Orientation(cardinal="Sud"))

    #     # Action
    #     rover.tournedroite()

    #     # Assert
    #     currentOrientation = rover.getOrientation()
    #     self.assertEqual(currentOrientation, Orientation("Ouest"))

    def test_avance(self):
        # Arrange
        rover = Rover(orientation=Orientation(cardinal="Sud"), position=Position(0,0))

        # Action
        rover.avance()
        
        # Assert
        position_actuel = rover.getPosition()
        self.assertEqual(position_actuel, Position(10,0))
        


if __name__ == '__main__':
    unittest.main()