from src.objects import Cardinal, Map, Position

class Direction:

    def __init__(self, startCardinal:Cardinal) -> None:
        self._cardinal = startCardinal

    def __eq__(self, otherDirection: object) -> bool:
        return otherDirection._cardinal == self._cardinal

    def __str__(self) -> str:
        return f"{self._cardinal}"

    def turnLeft(self) -> None:
        self._cardinal = self._cardinal.left()

    def turnRight(self) -> None:
        self._cardinal = self._cardinal.right()

    def moveUp(self, position: Position, map:Map) -> None:
        if self._cardinal.isNorth() : return position.moveNorth(map=map)
        if self._cardinal.isEast()  : return position.moveEast(map=map)
        if self._cardinal.isSouth() : return position.moveSouth(map=map)
        if self._cardinal.isWest()  : return position.moveWest(map=map)

    def moveDown(self, position: Position, map:Map) -> None:
        if self._cardinal.isNorth() : return position.moveSouth(map=map)
        if self._cardinal.isEast()  : return position.moveWest(map=map)
        if self._cardinal.isSouth() : return position.moveNorth(map=map)
        if self._cardinal.isWest()  : return position.moveEast(map=map)