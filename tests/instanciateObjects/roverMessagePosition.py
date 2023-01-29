import unittest

from src import RoverMessagePosition
from tests.builders import RoverBuilder

class TestInitRoverMessagePosition(unittest.TestCase):

    def test_init_roverMessagePosition(self):

        # Arrange
        rover = RoverBuilder.buildNorth(yPointValue=1, xPointValue=1)

        # Action 
        roverMessagePosition = RoverMessagePosition(rover=rover)

        # Assert
        self.assertEqual(roverMessagePosition._value, "1;1_N")