import unittest

from src import Obstacle
from tests.builders import CoordonneeBuilder

class TestInitObstacle(unittest.TestCase):

    def test_init_coordonnee(self):

        # Arrange
        coordonnee = CoordonneeBuilder.build(yPointValue=1, xPointValue=1)

        # Action 
        obstacle = Obstacle(coordonnee=coordonnee)

        # Assert
        self.assertEqual(obstacle._coordonnee, coordonnee)