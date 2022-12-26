import unittest

from src import RoverMessageObstacle
from tests.builders import ObstacleBuilder

class TestInitRoverMessageObstacle(unittest.TestCase):

    def test_init_roverMessageObstacle(self):

        # Arrange
        obstacle = ObstacleBuilder.build(yPointValue=1, xPointValue=1)

        # Action 
        roverMessageObstacle = RoverMessageObstacle(obstacle=obstacle)

        # Assert
        self.assertEqual(roverMessageObstacle._value, "Unable to move due to the obstacle : [1;1] (y;x)")