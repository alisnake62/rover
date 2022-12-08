import unittest

from rover import Rover, Orientation, Position

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
        rover = Rover(orientation=Position())

        # Action
        rover.avance()
        
        # Assert
        position_actuel = rover.getPosition()
        self.assertEqual(position_actuel, Position(10,0))
        


if __name__ == '__main__':
    unittest.main()