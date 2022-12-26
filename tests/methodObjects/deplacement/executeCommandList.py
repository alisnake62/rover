import unittest

from tests.builders import RoverBuilder, DeplacementBuilder, RoverMessagePositionBuilder, RoverMessageObstacleBuilder, CommandBuilder

class TestExecuteCommandList(unittest.TestCase):

    def test_execute_command_list(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_without_obstacle_rover_north_0_1()

        command1 = CommandBuilder.up()
        command2 = CommandBuilder.right()
        command3 = CommandBuilder.up()
        command4 = CommandBuilder.left()
        command5 = CommandBuilder.down()
        commandList = [command1, command2, command3, command4, command5]

        # Action 
        message = deplacement.executeCommandList(commands=commandList)

        # Assert
        expectedRover   = RoverBuilder.buildNorth(yPointValue=0, xPointValue=2)
        expectedMessage = RoverMessagePositionBuilder.buildNorth(yPointValue=0, xPointValue=2)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)

    def test_execute_command_list_with_obstacle(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_obstacle_2_2_rover_north_0_1()

        command1 = CommandBuilder.up()
        command2 = CommandBuilder.up()
        command3 = CommandBuilder.right()
        command4 = CommandBuilder.up()
        command5 = CommandBuilder.left()
        command6 = CommandBuilder.down()
        commandList = [command1, command2, command3, command4, command5, command6]

        # Action 
        message = deplacement.executeCommandList(commands=commandList)

        # Assert
        expectedRover   = RoverBuilder.buildEast(yPointValue=2, xPointValue=1)
        expectedMessage = RoverMessageObstacleBuilder.build(yPointValue=2, xPointValue=2)
        self.assertEqual(deplacement._rover , expectedRover)
        self.assertEqual(message            , expectedMessage)