import unittest

from tests.builders import RoverBuilder, DeplacementBuilder

class TestDeplacementMoveUp(unittest.TestCase):

    def test_move_up_if_direction_north(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_north_0_1()

        # Action 
        deplacement.moveUp()

        # Assert
        expectedRover = RoverBuilder.buildNorth(yPointValue=1, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_up_if_direction_north_and_out_of_limit(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_north_10_1()

        # Action 
        deplacement.moveUp()

        # Assert
        expectedRover = RoverBuilder.buildNorth(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_up_if_direction_east(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_east_0_1()

        # Action 
        deplacement.moveUp()

        # Assert
        expectedRover = RoverBuilder.buildEast(yPointValue=0, xPointValue=2)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_up_if_direction_east_and_out_of_limit(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_east_0_10()

        # Action 
        deplacement.moveUp()

        # Assert
        expectedRover = RoverBuilder.buildEast(yPointValue=0, xPointValue=0)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_up_if_direction_south(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_south_1_1()

        # Action 
        deplacement.moveUp()

        # Assert
        expectedRover = RoverBuilder.buildSouth(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_up_if_direction_south_and_out_of_limit(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_south_0_1()

        # Action 
        deplacement.moveUp()

        # Assert
        expectedRover = RoverBuilder.buildSouth(yPointValue=10, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_up_if_direction_west(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_west_0_1()

        # Action 
        deplacement.moveUp()

        # Assert
        expectedRover = RoverBuilder.buildWest(yPointValue=0, xPointValue=0)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_up_if_direction_west_and_out_of_limit(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_west_0_0()

        # Action 
        deplacement.moveUp()

        # Assert
        expectedRover = RoverBuilder.buildWest(yPointValue=0, xPointValue=10)
        self.assertEqual(deplacement._rover, expectedRover)