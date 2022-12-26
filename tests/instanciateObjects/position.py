import unittest

from src import Position
from tests.builders import CoordonneeBuilder

class TestInitPosition(unittest.TestCase):

    def test_init_position(self):

        # Arrange
        coordonnee = CoordonneeBuilder.build(yPointValue=0, xPointValue=1)

        # Action 
        position = Position(startCoordonnee=coordonnee)

        # Assert
        self.assertEqual(position._coordonnee, coordonnee)