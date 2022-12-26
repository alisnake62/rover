from src.objects import Coordonnee, Map

from copy import deepcopy

class Position:

    def __init__(self, startCoordonnee:Coordonnee) -> None:
        self._coordonnee = startCoordonnee

    def __eq__(self, otherposition: object) -> bool:
        return otherposition._coordonnee == self._coordonnee

    def __str__(self) -> str:
        return f"{self._coordonnee}"

    def isInMap(self, map:Map) -> bool:
        return self._coordonnee.isInMap(map=map)

    def moveNorth(self, map:Map) -> None:

        oldCoordonnee = deepcopy(self._coordonnee)
        newCoordonnee = deepcopy(self._coordonnee.north(map=map))
        self._coordonnee = oldCoordonnee
        obstacle = map.isObstacle(coordonnee=newCoordonnee)

        if obstacle: return obstacle

        self._coordonnee = self._coordonnee.north(map=map)

    def moveEast(self, map:Map) -> None:

        oldCoordonnee = deepcopy(self._coordonnee)
        newCoordonnee = deepcopy(self._coordonnee.east(map=map))
        self._coordonnee = oldCoordonnee
        obstacle = map.isObstacle(coordonnee=newCoordonnee)

        if obstacle: return obstacle

        self._coordonnee = self._coordonnee.east(map=map)

    def moveSouth(self, map:Map) -> None:

        oldCoordonnee = deepcopy(self._coordonnee)
        newCoordonnee = deepcopy(self._coordonnee.south(map=map))
        self._coordonnee = oldCoordonnee
        obstacle = map.isObstacle(coordonnee=newCoordonnee)

        if obstacle: return obstacle

        self._coordonnee = self._coordonnee.south(map=map)

    def moveWest(self, map:Map) -> None:

        oldCoordonnee = deepcopy(self._coordonnee)
        newCoordonnee = deepcopy(self._coordonnee.west(map=map))
        self._coordonnee = oldCoordonnee
        obstacle = map.isObstacle(coordonnee=newCoordonnee)

        if obstacle: return obstacle

        self._coordonnee = self._coordonnee.west(map=map)