from typing import List, TYPE_CHECKING
if TYPE_CHECKING: from src.objects import Obstacle, Coordonnee

from src.objects import Point

from exception import OutSideMapException

class Map:

    def __init__(self, yMax:Point, xMax:Point, obstacles:List['Obstacle']) -> None:

        self._yMax      = yMax
        self._xMax      = xMax

        for obstacle in obstacles:
            if not obstacle.isInMap(self): raise OutSideMapException()
        self._obstacles = obstacles

    def isGoodYPoint(self, point:Point) -> bool:
        if point > self._yMax: return False
        return True

    def isGoodXPoint(self, point:Point) -> bool:
        if point > self._xMax: return False
        return True

    def isObstacle(self, coordonnee:'Coordonnee') -> 'Obstacle':
        for obstacle in self._obstacles:
            if obstacle.here(coordonnee): return obstacle

    def transformYPointIfOutOfMapLimit(self, point: Point) -> Point:
        if point.isNegative(): return self._yMax
        if point > self._yMax: return Point(value=0)
        return point

    def transformXPointIfOutOfMapLimit(self, point: Point) -> Point:
        if point.isNegative(): return self._xMax
        if point > self._xMax: return Point(value=0)
        return point