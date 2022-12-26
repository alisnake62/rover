from typing import TYPE_CHECKING
if TYPE_CHECKING: from src.objects import Obstacle

from src.objects import Coordonnee, Map, Position, Cardinal, Direction

class RoverMessage:
    _value = ""

    def __str__(self) -> str:
        return self._value

    def __eq__(self, otherMessage: object) -> bool:
        return otherMessage._value == self._value

class RoverMessagePosition(RoverMessage):
    def __init__(self, roverPosition:Position) -> None:
        self._value = f"Current position : {roverPosition}"

class RoverMessageObstacle(RoverMessage):
    def __init__(self, obstacle:'Obstacle') -> None:
        self._value = f"Unable to move due to the obstacle : {obstacle}"

class Rover:

    def __init__(self, startCoordonnee: Coordonnee, startCardinal:Cardinal) -> None:
        self._position  = Position(startCoordonnee=startCoordonnee)
        self._direction = Direction(startCardinal=startCardinal)

    def __eq__(self, otherRover: object) -> bool:
        return otherRover._position == self._position and otherRover._direction == self._direction

    def isInMap(self, map:Map) -> bool:
        return self._position.isInMap(map=map)

    def turnLeft(self) -> RoverMessagePosition:
        self._direction.turnLeft()
        return RoverMessagePosition(roverPosition=self._position)

    def turnRight(self) -> RoverMessagePosition:
        self._direction.turnRight()
        return RoverMessagePosition(roverPosition=self._position)

    def moveUp(self, map:Map) -> RoverMessagePosition:
        obstacle = self._direction.moveUp(position=self._position, map=map)
        if obstacle: return RoverMessageObstacle(obstacle=obstacle)
        return RoverMessagePosition(roverPosition=self._position)

    def moveDown(self, map:Map) -> RoverMessagePosition:
        obstacle = self._direction.moveDown(position=self._position, map=map)
        if obstacle: return RoverMessageObstacle(obstacle=obstacle)
        return RoverMessagePosition(roverPosition=self._position)