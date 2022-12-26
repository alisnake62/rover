import unittest

from main import Rover
from tests.builders import CoordonneeBuilder, CardinalBuilder, DirectionBuilder, PositionBuilder

class TestInitRover(unittest.TestCase):

    def test_init_rover(self):

        # Arrange
        coordonnee  = CoordonneeBuilder.build(yPointValue=0, xPointValue=1)
        cardinal    = CardinalBuilder.north()

        # Action 
        rover = Rover(
            startCardinal   = cardinal,
            startCoordonnee = coordonnee
        )

        # Assert
        expectedPosition    = PositionBuilder.build(yPointValue=0, xPointValue=1)
        expectedDirection   = DirectionBuilder.north()
        self.assertEqual(rover._position    , expectedPosition)
        self.assertEqual(rover._direction   , expectedDirection)