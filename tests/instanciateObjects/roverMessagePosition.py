import unittest

from src import RoverMessagePosition
from tests.builders import PositionBuilder

class TestInitRoverMessagePosition(unittest.TestCase):

    def test_init_roverMessagePosition(self):

        # Arrange
        position = PositionBuilder.build(yPointValue=1, xPointValue=1)

        # Action 
        roverMessagePosition = RoverMessagePosition(roverPosition=position)

        # Assert
        self.assertEqual(roverMessagePosition._value, "Current position : [1;1] (y;x)")