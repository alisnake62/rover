import unittest

from main import Coordonnee
from tests.builders import PointBuilder

class TestInitCoordonnee(unittest.TestCase):

    def test_init_coordonnee(self):

        # Arrange
        y = PointBuilder.build(value=0)
        x = PointBuilder.build(value=1)

        # Action 
        coordonnee = Coordonnee(y=y, x=x)

        # Assert
        self.assertEqual(coordonnee._y, y)
        self.assertEqual(coordonnee._x, x)