from src.objects import Coordonnee, Map, Position, Cardinal, Direction

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

    def moveUp(self, map:Map) -> None:
        self._direction.moveUp(position=self._position, map=map)

    def moveDown(self, map:Map) -> None:
        self._direction.moveDown(position=self._position, map=map)