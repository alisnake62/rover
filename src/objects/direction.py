from src.objects import Cardinal, Map, Position

class Direction:

    def __init__(self, startCardinal:Cardinal) -> None:
        self._cardinal = startCardinal

    def __eq__(self, otherDirection: object) -> bool:
        return otherDirection._cardinal == self._cardinal

    def turnLeft(self) -> None:
        self._cardinal = self._cardinal.left()

    def turnRight(self) -> None:
        self._cardinal = self._cardinal.right()

    def moveUp(self, position: Position, map:Map) -> None:
        if self._cardinal.isNorth() : position.moveNorth(map=map)
        if self._cardinal.isEast()  : position.moveEast(map=map)
        if self._cardinal.isSouth() : position.moveSouth(map=map)
        if self._cardinal.isWest()  : position.moveWest(map=map)

    def moveDown(self, position: Position, map:Map) -> None:
        if self._cardinal.isNorth() : position.moveSouth(map=map)
        if self._cardinal.isEast()  : position.moveWest(map=map)
        if self._cardinal.isSouth() : position.moveNorth(map=map)
        if self._cardinal.isWest()  : position.moveEast(map=map)