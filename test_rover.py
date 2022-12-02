import unittest

from rover import Rover, Orientation

class TestRover(unittest.TestCase):

    def test_easy(self):
        # Arrange
        rover = Rover()

        # Action
        testEasy = rover.easy()

        # Assert
        self.assertEqual(testEasy, 1)


    # def test_tourne_droite_1(self):
    #     # Arrange
    #     rover = Rover(orientation=Orientation(cardinal="Sud"))

    #     # Action
    #     # rover.tournedroite()

    #     # Assert
    #     currentOrientation = rover.getOrientation
    #     self.assertEqual(currentOrientation, Orientation("Sud"))
        

if __name__ == '__main__':
    unittest.main()