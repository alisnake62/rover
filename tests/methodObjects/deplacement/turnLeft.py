import unittest

from tests.builders import RoverBuilder, DeplacementBuilder

class TestDeplacementTurnLeft(unittest.TestCase):

    def test_left_if_direction_north(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_north_0_1()

        # Action 
        deplacement.turnLeft()

        # Assert
        expectedRover = RoverBuilder.buildWest(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_left_if_direction_east(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_east_0_1()

        # Action 
        deplacement.turnLeft()

        # Assert
        expectedRover = RoverBuilder.buildNorth(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_left_if_direction_south(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_south_0_1()

        # Action 
        deplacement.turnLeft()

        # Assert
        expectedRover = RoverBuilder.buildEast(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_left_if_direction_west(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_west_0_1()

        # Action 
        deplacement.turnLeft()

        # Assert
        expectedRover = RoverBuilder.buildSouth(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)