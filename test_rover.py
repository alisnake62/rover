import unittest

from rover import Rover, Orientation

class TestRover(unittest.TestCase):

    def test_tourne_droite_1(self):
        # Arrange
        rover = Rover(orientation=Orientation(cardinal="Sud"))

        # Action
        rover.tournedroite()

        # Assert
        currentOrientation = rover.getOrientation()
        self.assertEqual(currentOrientation, Orientation("Ouest"))
        

if __name__ == '__main__':
    unittest.main()