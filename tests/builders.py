from main import Point, Coordonnee, Cardinal, Position, Direction, Rover, Map, Deplacement, RoverMessagePosition, Obstacle

class PointBuilder:

    def build(value:int) -> Point:
        return Point(value=value)

class CoordonneeBuilder:

    def build(yPointValue:int, xPointValue:int) -> Coordonnee:
        y = PointBuilder.build(value=yPointValue)
        x = PointBuilder.build(value=xPointValue)
        return Coordonnee(y=y, x=x)

class PositionBuilder:

    def build(yPointValue:int, xPointValue:int) -> Position:
        coordonnee = CoordonneeBuilder.build(yPointValue=yPointValue, xPointValue=xPointValue)
        return Position(startCoordonnee=coordonnee)

class ObstacleBuilder:

    def build(yPointValue:int, xPointValue:int) -> Obstacle:
        coordonnee = CoordonneeBuilder.build(yPointValue=yPointValue, xPointValue=xPointValue)
        return Obstacle(coordonnee=coordonnee)

class RoverMessagePositionBuilder:
    def build(yPointValue:int, xPointValue:int) -> RoverMessagePosition:
        position = PositionBuilder.build(yPointValue=yPointValue, xPointValue=xPointValue)
        return RoverMessagePosition(roverPosition=position)

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

    def buildNorth(yPointValue:int, xPointValue:int) -> Rover:
        coordonne   = CoordonneeBuilder.build(yPointValue=yPointValue, xPointValue=xPointValue)
        cardinal    = CardinalBuilder.north()
        return Rover(startCoordonnee=coordonne, startCardinal=cardinal)

    def buildEast(yPointValue:int, xPointValue:int) -> Rover:
        coordonne   = CoordonneeBuilder.build(yPointValue=yPointValue, xPointValue=xPointValue)
        cardinal    = CardinalBuilder.east()
        return Rover(startCoordonnee=coordonne, startCardinal=cardinal)

    def buildSouth(yPointValue:int, xPointValue:int) -> Rover:
        coordonne   = CoordonneeBuilder.build(yPointValue=yPointValue, xPointValue=xPointValue)
        cardinal    = CardinalBuilder.south()
        return Rover(startCoordonnee=coordonne, startCardinal=cardinal)

    def buildWest(yPointValue:int, xPointValue:int) -> Rover:
        coordonne   = CoordonneeBuilder.build(yPointValue=yPointValue, xPointValue=xPointValue)
        cardinal    = CardinalBuilder.west()
        return Rover(startCoordonnee=coordonne, startCardinal=cardinal)

class MapBuilder:

    def map_10_10_without_obstacle() -> Map:
        yMax = PointBuilder.build(value=10)
        xMax = PointBuilder.build(value=10)
        return Map(yMax=yMax, xMax=xMax, obstacles=[])

class DeplacementBuilder:

    def map_10_10_without_obstacle_rover_north_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildNorth(yPointValue=0, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_north_1_1() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildNorth(yPointValue=1, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_north_10_1() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildNorth(yPointValue=10, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_east_0_0() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildEast(yPointValue=0, xPointValue=0)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_east_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildEast(yPointValue=0, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_east_0_10() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildEast(yPointValue=0, xPointValue=10)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_south_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildSouth(yPointValue=0, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_south_1_1() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildSouth(yPointValue=1, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_south_10_1() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildSouth(yPointValue=10, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_west_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildWest(yPointValue=0, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_west_0_0() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildWest(yPointValue=0, xPointValue=0)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_west_0_10() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildWest(yPointValue=0, xPointValue=10)
        return Deplacement(map=map, rover=rover)