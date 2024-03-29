from src import Point, Coordonnee, Cardinal, Position, Direction, Rover, Map, Deplacement, RoverMessagePosition, RoverMessageObstacle, Obstacle, Command

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

    def buildNorth(yPointValue:int, xPointValue:int) -> RoverMessagePosition:
        rover = RoverBuilder.buildNorth(yPointValue=yPointValue, xPointValue=xPointValue)
        return RoverMessagePosition(rover=rover)

    def buildEast(yPointValue:int, xPointValue:int) -> RoverMessagePosition:
        rover = RoverBuilder.buildEast(yPointValue=yPointValue, xPointValue=xPointValue)
        return RoverMessagePosition(rover=rover)

    def buildSouth(yPointValue:int, xPointValue:int) -> RoverMessagePosition:
        rover = RoverBuilder.buildSouth(yPointValue=yPointValue, xPointValue=xPointValue)
        return RoverMessagePosition(rover=rover)

    def buildWest(yPointValue:int, xPointValue:int) -> RoverMessagePosition:
        rover = RoverBuilder.buildWest(yPointValue=yPointValue, xPointValue=xPointValue)
        return RoverMessagePosition(rover=rover)

class RoverMessageObstacleBuilder:
    def build(rover:Rover, yPointValue:int, xPointValue:int) -> RoverMessageObstacle:
        obstacle    = ObstacleBuilder.build(yPointValue=yPointValue, xPointValue=xPointValue)
        return RoverMessageObstacle(rover=rover, obstacle=obstacle)

class CardinalBuilder:

    def north() -> Cardinal:
        return Cardinal(value="North")

    def south() -> Cardinal:
        return Cardinal(value="South")

    def east() -> Cardinal:
        return Cardinal(value="East")

    def west() -> Cardinal:
        return Cardinal(value="West")

class CommandBuilder:

    def up() -> Command:
        return Command(value="Up")

    def down() -> Command:
        return Command(value="Down")

    def left() -> Command:
        return Command(value="Left")

    def right() -> Command:
        return Command(value="Right")

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

    def map_10_10_obstacle_0_0() -> Map:
        yMax = PointBuilder.build(value=10)
        xMax = PointBuilder.build(value=10)
        obstacle    = ObstacleBuilder.build(yPointValue=0, xPointValue=0)
        obstacles   = [obstacle]
        return Map(yMax=yMax, xMax=xMax, obstacles=obstacles)

    def map_10_10_obstacle_0_1() -> Map:
        yMax = PointBuilder.build(value=10)
        xMax = PointBuilder.build(value=10)
        obstacle    = ObstacleBuilder.build(yPointValue=0, xPointValue=1)
        obstacles   = [obstacle]
        return Map(yMax=yMax, xMax=xMax, obstacles=obstacles)

    def map_10_10_obstacle_0_2() -> Map:
        yMax = PointBuilder.build(value=10)
        xMax = PointBuilder.build(value=10)
        obstacle    = ObstacleBuilder.build(yPointValue=0, xPointValue=2)
        obstacles   = [obstacle]
        return Map(yMax=yMax, xMax=xMax, obstacles=obstacles)

    def map_10_10_obstacle_1_1() -> Map:
        yMax = PointBuilder.build(value=10)
        xMax = PointBuilder.build(value=10)
        obstacle    = ObstacleBuilder.build(yPointValue=1, xPointValue=1)
        obstacles   = [obstacle]
        return Map(yMax=yMax, xMax=xMax, obstacles=obstacles)

    def map_10_10_obstacle_2_2() -> Map:
        yMax = PointBuilder.build(value=10)
        xMax = PointBuilder.build(value=10)
        obstacle    = ObstacleBuilder.build(yPointValue=2, xPointValue=2)
        obstacles   = [obstacle]
        return Map(yMax=yMax, xMax=xMax, obstacles=obstacles)

class DeplacementBuilder:

    def map_10_10_without_obstacle_rover_north_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildNorth(yPointValue=0, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_obstacle_1_1_rover_north_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10_obstacle_1_1()
        rover   = RoverBuilder.buildNorth(yPointValue=0, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_obstacle_2_2_rover_north_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10_obstacle_2_2()
        rover   = RoverBuilder.buildNorth(yPointValue=0, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_north_1_1() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildNorth(yPointValue=1, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_obstacle_0_1_rover_north_1_1() -> Deplacement:
        map     = MapBuilder.map_10_10_obstacle_0_1()
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

    def map_10_10_obstacle_0_2_rover_east_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10_obstacle_0_2()
        rover   = RoverBuilder.buildEast(yPointValue=0, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_east_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildEast(yPointValue=0, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_obstacle_0_0_rover_east_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10_obstacle_0_0()
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

    def map_10_10_obstacle_1_1_rover_south_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10_obstacle_1_1()
        rover   = RoverBuilder.buildSouth(yPointValue=0, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_south_1_1() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildSouth(yPointValue=1, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_obstacle_0_1_rover_south_1_1() -> Deplacement:
        map     = MapBuilder.map_10_10_obstacle_0_1()
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

    def map_10_10_obstacle_0_0_rover_west_0_1() -> Deplacement:
        map     = MapBuilder.map_10_10_obstacle_0_0()
        rover   = RoverBuilder.buildWest(yPointValue=0, xPointValue=1)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_west_0_0() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildWest(yPointValue=0, xPointValue=0)
        return Deplacement(map=map, rover=rover)

    def map_10_10_obstacle_0_1_rover_west_0_0() -> Deplacement:
        map     = MapBuilder.map_10_10_obstacle_0_1()
        rover   = RoverBuilder.buildWest(yPointValue=0, xPointValue=0)
        return Deplacement(map=map, rover=rover)

    def map_10_10_without_obstacle_rover_west_0_10() -> Deplacement:
        map     = MapBuilder.map_10_10_without_obstacle()
        rover   = RoverBuilder.buildWest(yPointValue=0, xPointValue=10)
        return Deplacement(map=map, rover=rover)