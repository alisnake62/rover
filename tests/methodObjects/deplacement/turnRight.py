import unittest

from tests.builders import RoverBuilder, DeplacementBuilder

class TestDeplacementTurnRight(unittest.TestCase):

    def test_right_if_direction_north(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_north_0_1()

        # Action 
        deplacement.turnRight()

        # Assert
        expectedRover = RoverBuilder.buildEast(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_right_if_direction_east(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_east_0_1()

        # Action 
        deplacement.turnRight()

        # Assert
        expectedRover = RoverBuilder.buildSouth(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_right_if_direction_south(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_south_0_1()

        # Action 
        deplacement.turnRight()

        # Assert
        expectedRover = RoverBuilder.buildWest(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_right_if_direction_west(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_west_0_1()

        # Action 
        deplacement.turnRight()

        # Assert
        expectedRover = RoverBuilder.buildNorth(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)