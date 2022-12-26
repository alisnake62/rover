import unittest

from src import Deplacement
from tests.builders import MapBuilder, RoverBuilder

from exception import OutSideMapException

class TestInitDeplacement(unittest.TestCase):

    def test_init_deplacement(self):

        # Arrange
        map     = MapBuilder.map_10_10()
        rover   = RoverBuilder.buildNorth(yPointValue=0, xPointValue=1)

        # Action 
        direction = Deplacement(map=map, rover=rover)

        # Assert
        self.assertEqual(direction._map     , map)
        self.assertEqual(direction._rover   , rover)

    def test_init_deplacement_if_rover_not_in_map(self):

        # Arrange
        map     = MapBuilder.map_10_10()
        rover   = RoverBuilder.buildNorth(yPointValue=0, xPointValue=12)

        # Action 
        with self.assertRaises(OutSideMapException) as ar:
            Deplacement(map=map, rover=rover)

        # Assert
        self.assertEqual(str(ar.exception), "The position of the rover is not in the Map")