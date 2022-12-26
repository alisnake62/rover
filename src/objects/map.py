from src.objects import Point

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

    def transformYPointIfOutOfMapLimit(self, point: Point) -> Point:
        if point.isNegative(): return self._yMax
        if point > self._yMax: return Point(value=0)
        return point

    def transformXPointIfOutOfMapLimit(self, point: Point) -> Point:
        if point.isNegative(): return self._xMax
        if point > self._xMax: return Point(value=0)
        return point