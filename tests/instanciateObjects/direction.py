import unittest

from main import Direction
from tests.builders import CardinalBuilder

class TestInitDirection(unittest.TestCase):

    def test_init_direction(self):

        # Arrange
        cardinal = CardinalBuilder.north()

        # Action 
        direction = Direction(startCardinal=cardinal)

        # Assert
        self.assertEqual(direction._cardinal, cardinal)