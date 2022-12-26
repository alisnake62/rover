import unittest

from rover import Point, Map, Coordonnee, Position, Cardinal, Direction, Rover, Deplacement
from test_builder_rover import (
    PointBuilder,
    CoordonneeBuilder,
    CardinalBuilder,
    DirectionBuilder,
    PositionBuilder,
    MapBuilder,
    RoverBuilder,
    DeplacementBuilder
)

from exception import BadPointValueException, BadCardinalValueException, OutSideMapException

class TestInitPoint(unittest.TestCase):

    def test_init_point(self):

        # Arrange

        # Action 
        point = Point(value=1)

        # Assert
        self.assertEqual(point._value, 1)

    def test_init_point_with_negative_value(self):

        # Arrange

        # Action 
        with self.assertRaises(BadPointValueException) as ar:
            Point(value=-1)

        # Assert
        self.assertEqual(str(ar.exception), "The Point Value Must Positive or 0")

    def test_init_point_with_float_value(self):

        # Arrange

        # Action 
        with self.assertRaises(BadPointValueException) as ar:
            Point(value=1.5)

        # Assert
        self.assertEqual(str(ar.exception), "The Point Value Must Be Integer")

class TestInitCoordonnee(unittest.TestCase):

    def test_init_coordonnee(self):

        # Arrange
        y = PointBuilder.build(value=0)
        x = PointBuilder.build(value=1)

        # Action 
        coordonnee = Coordonnee(y=y, x=x)

        # Assert
        self.assertEqual(coordonnee._y, y)
        self.assertEqual(coordonnee._x, x)

class TestInitMap(unittest.TestCase):

    def test_init_map(self):

        # Arrange
        y = PointBuilder.build(value=0)
        x = PointBuilder.build(value=1)

        # Action 
        map = Map(yMax=y, xMax=x)

        # Assert
        self.assertEqual(map._yMax, y)
        self.assertEqual(map._xMax, x)

class TestInitPosition(unittest.TestCase):

    def test_init_position(self):

        # Arrange
        coordonnee = CoordonneeBuilder.build(yPointValue=0, xPointValue=1)

        # Action 
        position = Position(startCoordonnee=coordonnee)

        # Assert
        self.assertEqual(position._coordonnee, coordonnee)

class TestInitCardinal(unittest.TestCase):

    def test_init_cardinal(self):

        # Arrange

        # Action 
        cardinal = Cardinal(value="North")

        # Assert
        self.assertEqual(cardinal._index, 0)

    def test_init_cardinal_with_bad_value(self):

        # Arrange

        # Action 
        with self.assertRaises(BadCardinalValueException) as ar:
            Cardinal(value="Toto")

        # Assert
        self.assertEqual(str(ar.exception), "The Cardfinal Value Must Be One of ('North', 'South', 'East', 'West')")

class TestInitDirection(unittest.TestCase):

    def test_init_direction(self):

        # Arrange
        cardinal = CardinalBuilder.north()

        # Action 
        direction = Direction(startCardinal=cardinal)

        # Assert
        self.assertEqual(direction._cardinal, cardinal)

class TestInitRover(unittest.TestCase):

    def test_init_rover(self):

        # Arrange
        coordonnee  = CoordonneeBuilder.build(yPointValue=0, xPointValue=1)
        cardinal    = CardinalBuilder.north()

        # Action 
        rover = Rover(
            startCardinal   = cardinal,
            startCoordonnee = coordonnee
        )

        # Assert
        expectedPosition    = PositionBuilder.build(yPointValue=0, xPointValue=1)
        expectedDirection   = DirectionBuilder.north()
        self.assertEqual(rover._position    , expectedPosition)
        self.assertEqual(rover._direction   , expectedDirection)

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


class TestRoverTurnLeft(unittest.TestCase):

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

class TestRoverTurnRight(unittest.TestCase):

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

class TestRoverMoveUp(unittest.TestCase):

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

class TestRoverMoveUp(unittest.TestCase):

    def test_move_down_if_direction_north(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_north_1_1()

        # Action 
        deplacement.moveDown()

        # Assert
        expectedRover = RoverBuilder.buildNorth(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_up_if_direction_north_and_out_of_limit(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_north_0_1()

        # Action 
        deplacement.moveDown()

        # Assert
        expectedRover = RoverBuilder.buildNorth(yPointValue=10, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_down_if_direction_east(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_east_0_1()

        # Action 
        deplacement.moveDown()

        # Assert
        expectedRover = RoverBuilder.buildEast(yPointValue=0, xPointValue=0)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_up_if_direction_east_and_out_of_limit(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_east_0_0()

        # Action 
        deplacement.moveDown()

        # Assert
        expectedRover = RoverBuilder.buildEast(yPointValue=0, xPointValue=10)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_down_if_direction_south(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_south_0_1()

        # Action 
        deplacement.moveDown()

        # Assert
        expectedRover = RoverBuilder.buildSouth(yPointValue=1, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_up_if_direction_south_and_out_of_limit(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_south_10_1()

        # Action 
        deplacement.moveDown()

        # Assert
        expectedRover = RoverBuilder.buildSouth(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_down_if_direction_west(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_west_0_0()

        # Action 
        deplacement.moveDown()

        # Assert
        expectedRover = RoverBuilder.buildWest(yPointValue=0, xPointValue=1)
        self.assertEqual(deplacement._rover, expectedRover)

    def test_move_up_if_direction_west_and_out_of_limit(self):

        # Arrange
        deplacement = DeplacementBuilder.map_10_10_rover_west_0_10()

        # Action 
        deplacement.moveDown()

        # Assert
        expectedRover = RoverBuilder.buildWest(yPointValue=0, xPointValue=0)
        self.assertEqual(deplacement._rover, expectedRover)

if __name__ == '__main__':
    unittest.main()