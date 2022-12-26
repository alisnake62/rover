import unittest

from src import Map
from tests.builders import PointBuilder

class TestInitMap(unittest.TestCase):

    def test_init_map(self):

        # Arrange
        y = PointBuilder.build(value=0)
        x = PointBuilder.build(value=1)

        # Action 
        map = Map(yMax=y, xMax=x)

        # Assert
        self.assertEqual(map._yMax, y)
        self.assertEqual(map._xMax, x)