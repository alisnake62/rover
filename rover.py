from exception import BadPointValueException, BadCardinalValueException, OutSideMapException

class Point:

    def __init__(self, value:int=0) -> None:

        if not isinstance(value, int)   : raise BadPointValueException(message="The Point Value Must Be Integer")
        if value < 0                    : raise BadPointValueException(message="The Point Value Must Positive or 0")
        self._value = value

    def __eq__(self, otherPoint: object) -> bool:
        return otherPoint._value == self._value

    def __gt__(self, otherPoint:object) -> bool:
        return self._value > otherPoint._value

class Map:

    def __init__(self, yMax:Point, xMax:Point) -> None:
        self._yMax = yMax
        self._xMax = xMax

    def isGoodYPoint(self, point:Point) -> bool:
        if point > self._yMax: return False
        return True

    def isGoodXPoint(self, point:Point) -> bool:
        if point > self._xMax: return False
        return True

class Coordonnee:

    def __init__(self, y:Point, x:Point) -> None:
        self._y = y
        self._x = x

    def __eq__(self, otherCoordonnee: object) -> bool:
        return otherCoordonnee._y == self._y and otherCoordonnee._x == self._x

    def isInMap(self, map: Map) -> bool:
        return map.isGoodYPoint(point=self._y) and map.isGoodXPoint(point=self._x)

class Position:

    def __init__(self, startCoordonnee:Coordonnee) -> None:
        self._coordonnee = startCoordonnee

    def __eq__(self, otherposition: object) -> bool:
        return otherposition._coordonnee == self._coordonnee

    def isInMap(self, map:Map) -> bool:
        return self._coordonnee.isInMap(map=map)

class Cardinal:

    _orderedExpectedValue = ["North", "East", "South", "West"]

    def __init__(self, value:str) -> None:
        if value not in self._orderedExpectedValue: raise BadCardinalValueException()
        self._index = self._orderedExpectedValue.index(value)

    def __eq__(self, otherCardinal: object) -> bool:
        return otherCardinal._index == self._index

    def left(self):
        self._index -= 1
        if self._index == -1: self._index = 3
        return self

    def right(self):
        self._index += 1
        if self._index == 4: self._index = 0
        return self


class Direction:

    def __init__(self, startCardinal:Cardinal) -> None:
        self._cardinal = startCardinal

    def __eq__(self, otherDirection: object) -> bool:
        return otherDirection._cardinal == self._cardinal

    def turnLeft(self) -> None:
        self._cardinal = self._cardinal.left()

    def turnRight(self) -> None:
        self._cardinal = self._cardinal.right()

class Rover:

    def __init__(self, startCoordonnee: Coordonnee, startCardinal:Cardinal) -> None:
        self._position  = Position(startCoordonnee=startCoordonnee)
        self._direction = Direction(startCardinal=startCardinal)

    def __eq__(self, otherRover: object) -> bool:
        return otherRover._position == self._position and otherRover._direction == self._direction

    def isInMap(self, map:Map) -> bool:
        return self._position.isInMap(map=map)

    def turnLeft(self) -> None:
        self._direction.turnLeft()

    def turnRight(self) -> None:
        self._direction.turnRight()

class Deplacement:

    def __init__(self, map:Map, rover:Rover) -> None:

        if not rover.isInMap(map=map): raise OutSideMapException()
        self._map   = map
        self._rover = rover

    def turnLeft(self) -> None:
        self._rover.turnLeft()

    def turnRight(self) -> None:
        self._rover.turnRight()
