from rover import Point, Coordonnee, Cardinal, Position, Direction, Rover, Map, Deplacement

class PointBuilder:

    def point0() -> Point:
        return Point(value=0)

    def point1() -> Point:
        return Point(value=1)

    def point10() -> Point:
        return Point(value=10)

    def point12() -> Point:
        return Point(value=12)

class CoordonneeBuilder:

    def coordonnee_0_1() -> Coordonnee:
        y = PointBuilder.point0()
        x = PointBuilder.point1()
        return Coordonnee(y=y, x=x)

    def coordonnee_0_12() -> Coordonnee:
        y = PointBuilder.point0()
        x = PointBuilder.point12()
        return Coordonnee(y=y, x=x)

class PositionBuilder:

    def position_0_1() -> Position:
        coordonnee = CoordonneeBuilder.coordonnee_0_1()
        return Position(startCoordonnee=coordonnee)

class CardinalBuilder:

    def north() -> Cardinal:
        return Cardinal(value="North")

    def south() -> Cardinal:
        return Cardinal(value="South")

    def east() -> Cardinal:
        return Cardinal(value="East")

    def west() -> Cardinal:
        return Cardinal(value="West")

class DirectionBuilder:

    def north() -> Direction:
        cardinal = CardinalBuilder.north()
        return Direction(startCardinal=cardinal)

    def south() -> Direction:
        cardinal = CardinalBuilder.south()
        return Direction(startCardinal=cardinal)

    def east() -> Direction:
        cardinal = CardinalBuilder.east()
        return Direction(startCardinal=cardinal)

    def west() -> Direction:
        cardinal = CardinalBuilder.west()
        return Direction(startCardinal=cardinal)

class RoverBuilder:

    def north_0_1() -> Rover:
        coordonne   = CoordonneeBuilder.coordonnee_0_1()
        cardinal    = CardinalBuilder.north()
        return Rover(startCoordonnee=coordonne, startCardinal=cardinal)

    def north_0_12() -> Rover:
        coordonne   = CoordonneeBuilder.coordonnee_0_12()
        cardinal    = CardinalBuilder.north()
        return Rover(startCoordonnee=coordonne, startCardinal=cardinal)

    def east_0_1() -> Rover:
        coordonne   = CoordonneeBuilder.coordonnee_0_1()
        cardinal    = CardinalBuilder.east()
        return Rover(startCoordonnee=coordonne, startCardinal=cardinal)

    def south_0_1() -> Rover:
        coordonne   = CoordonneeBuilder.coordonnee_0_1()
        cardinal    = CardinalBuilder.south()
        return Rover(startCoordonnee=coordonne, startCardinal=cardinal)

    def west_0_1() -> Rover:
        coordonne   = CoordonneeBuilder.coordonnee_0_1()
        cardinal    = CardinalBuilder.west()
        return Rover(startCoordonnee=coordonne, startCardinal=cardinal)

class MapBuilder:

    def map_10_10() -> Map:
        yMax = PointBuilder.point10()
        xMax = PointBuilder.point10()
        return Map(yMax=yMax, xMax=xMax)

class DeplacementBuilder:

    def map_10_10_rover_north_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10()
        rover   = RoverBuilder.north_0_1()
        return Deplacement(map=map, rover=rover)

    def map_10_10_rover_east_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10()
        rover   = RoverBuilder.east_0_1()
        return Deplacement(map=map, rover=rover)

    def map_10_10_rover_south_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10()
        rover   = RoverBuilder.south_0_1()
        return Deplacement(map=map, rover=rover)

    def map_10_10_rover_west_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10()
        rover   = RoverBuilder.west_0_1()
        return Deplacement(map=map, rover=rover)