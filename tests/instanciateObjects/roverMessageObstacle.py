import unittest

from src import RoverMessageObstacle
from tests.builders import ObstacleBuilder, RoverBuilder

class TestInitRoverMessageObstacle(unittest.TestCase):

    def test_init_roverMessageObstacle(self):

        # Arrange
        obstacle    = ObstacleBuilder.build(yPointValue=1, xPointValue=1)
        rover       = RoverBuilder.buildNorth(yPointValue=0, xPointValue=0)

        # Action 
        roverMessageObstacle = RoverMessageObstacle(rover=rover, obstacle=obstacle)

        # Assert
        self.assertEqual(roverMessageObstacle._value, "0;0_N_O_1;1")