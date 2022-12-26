from exception import OutSideMapException
from src.objects import Rover, Map, RoverMessagePosition

class Deplacement:

    def __init__(self, map:Map, rover:Rover) -> None:

        if not rover.isInMap(map=map): raise OutSideMapException()
        self._map   = map
        self._rover = rover

    def turnLeft(self) -> RoverMessagePosition:
        return self._rover.turnLeft()

    def turnRight(self) -> RoverMessagePosition:
        return self._rover.turnRight()

    def moveUp(self) -> RoverMessagePosition:
        return self._rover.moveUp(map=self._map)

    def moveDown(self) -> RoverMessagePosition:
        return self._rover.moveDown(map=self._map)