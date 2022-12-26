import unittest

from tests.builders import RoverBuilder, DeplacementBuilder, RoverMessagePositionBuilder, RoverMessageObstacleBuilder

class TestDeplacementMoveDown(unittest.TestCase):

    def test_move_down_if_direction_north(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_without_obstacle_rover_north_1_1()

        # Action 
        message = deplacement.moveDown()

        # Assert
        expectedRover   = RoverBuilder.buildNorth(yPointValue=0, xPointValue=1)
        expectedMessage = RoverMessagePositionBuilder.buildNorth(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)

    def test_move_up_if_direction_north_and_out_of_limit(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_without_obstacle_rover_north_0_1()

        # Action 
        message = deplacement.moveDown()

        # Assert
        expectedRover   = RoverBuilder.buildNorth(yPointValue=10, xPointValue=1)
        expectedMessage = RoverMessagePositionBuilder.buildNorth(yPointValue=10, xPointValue=1)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)


    def test_move_down_if_direction_north_and_obstacle(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_obstacle_0_1_rover_north_1_1()

        # Action 
        message = deplacement.moveDown()

        # Assert
        expectedRover   = RoverBuilder.buildNorth(yPointValue=1, xPointValue=1)
        expectedMessage = RoverMessageObstacleBuilder.build(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)

    def test_move_down_if_direction_east(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_without_obstacle_rover_east_0_1()

        # Action 
        message = deplacement.moveDown()

        # Assert
        expectedRover   = RoverBuilder.buildEast(yPointValue=0, xPointValue=0)
        expectedMessage = RoverMessagePositionBuilder.buildEast(yPointValue=0, xPointValue=0)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)

    def test_move_up_if_direction_east_and_out_of_limit(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_without_obstacle_rover_east_0_0()

        # Action 
        message = deplacement.moveDown()

        # Assert
        expectedRover   = RoverBuilder.buildEast(yPointValue=0, xPointValue=10)
        expectedMessage = RoverMessagePositionBuilder.buildEast(yPointValue=0, xPointValue=10)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)

    def test_move_down_if_direction_east_and_obstacle(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_obstacle_0_0_rover_east_0_1()

        # Action 
        message = deplacement.moveDown()

        # Assert
        expectedRover   = RoverBuilder.buildEast(yPointValue=0, xPointValue=1)
        expectedMessage = RoverMessageObstacleBuilder.build(yPointValue=0, xPointValue=0)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)

    def test_move_down_if_direction_south(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_without_obstacle_rover_south_0_1()

        # Action 
        message = deplacement.moveDown()

        # Assert
        expectedRover   = RoverBuilder.buildSouth(yPointValue=1, xPointValue=1)
        expectedMessage = RoverMessagePositionBuilder.buildSouth(yPointValue=1, xPointValue=1)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)

    def test_move_up_if_direction_south_and_out_of_limit(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_without_obstacle_rover_south_10_1()

        # Action 
        message = deplacement.moveDown()

        # Assert
        expectedRover   = RoverBuilder.buildSouth(yPointValue=0, xPointValue=1)
        expectedMessage = RoverMessagePositionBuilder.buildSouth(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)

    def test_move_down_if_direction_south_and_obstacle(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_obstacle_1_1_rover_south_0_1()

        # Action 
        message = deplacement.moveDown()

        # Assert
        expectedRover   = RoverBuilder.buildSouth(yPointValue=0, xPointValue=1)
        expectedMessage = RoverMessageObstacleBuilder.build(yPointValue=1, xPointValue=1)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)

    def test_move_down_if_direction_west(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_without_obstacle_rover_west_0_0()

        # Action 
        message = deplacement.moveDown()

        # Assert
        expectedRover   = RoverBuilder.buildWest(yPointValue=0, xPointValue=1)
        expectedMessage = RoverMessagePositionBuilder.buildWest(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)

    def test_move_up_if_direction_west_and_out_of_limit(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_without_obstacle_rover_west_0_10()

        # Action 
        message = deplacement.moveDown()

        # Assert
        expectedRover   = RoverBuilder.buildWest(yPointValue=0, xPointValue=0)
        expectedMessage = RoverMessagePositionBuilder.buildWest(yPointValue=0, xPointValue=0)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)

    def test_move_down_if_direction_west_and_obstacle(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_obstacle_0_1_rover_west_0_0()

        # Action 
        message = deplacement.moveDown()

        # Assert
        expectedRover   = RoverBuilder.buildWest(yPointValue=0, xPointValue=0)
        expectedMessage = RoverMessageObstacleBuilder.build(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)