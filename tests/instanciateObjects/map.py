import unittest

from src import Map
from tests.builders import PointBuilder, ObstacleBuilder

from exception import OutSideMapException

class TestInitMap(unittest.TestCase):

    def test_init_map(self):

        # Arrange
        y = PointBuilder.build(value=10)
        x = PointBuilder.build(value=10)
        obstacles = [
            ObstacleBuilder.build(yPointValue=1, xPointValue=1)
        ]

        # Action 
        map = Map(yMax=y, xMax=x, obstacles=obstacles)

        # Assert
        self.assertEqual(map._yMax, y)
        self.assertEqual(map._xMax, x)
        self.assertEqual(map._obstacles, obstacles)

    def test_init_map_with_obstacle_not_in_map(self):

        # Arrange
        y = PointBuilder.build(value=10)
        x = PointBuilder.build(value=10)
        obstacles = [
            ObstacleBuilder.build(yPointValue=11, xPointValue=1)
        ]

        # Action 
        with self.assertRaises(OutSideMapException) as ar:
            Map(yMax=y, xMax=x, obstacles=obstacles)

        # Assert
        self.assertEqual(str(ar.exception), "The position of the object is not in the Map")