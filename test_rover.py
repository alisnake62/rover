import unittest

from rover import Rover

class TestRover(unittest.TestCase):

    def test_easy(self):
        # Arrange
        rover = Rover()

        # Action
        testEasy = rover.easy()

        # Assert
        self.assertEqual(testEasy, 1)

if __name__ == '__main__':
    unittest.main()
