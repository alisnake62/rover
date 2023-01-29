from src.objects import Point, Map

class Coordonnee:

    def __init__(self, y:Point, x:Point) -> None:
        self._y = y
        self._x = x

    def __eq__(self, otherCoordonnee) -> bool:
        return otherCoordonnee._y == self._y and otherCoordonnee._x == self._x

    def __str__(self) -> str:
        return f"{self._y};{self._x}"

    def isInMap(self, map: Map) -> bool:
        return map.isGoodYPoint(point=self._y) and map.isGoodXPoint(point=self._x)

    def north(self, map: Map):
        self._y.add1()
        self._y = map.transformYPointIfOutOfMapLimit(self._y)
        return self

    def east(self, map: Map):
        self._x.add1()
        self._x = map.transformYPointIfOutOfMapLimit(self._x)
        return self

    def south(self, map: Map):
        self._y.remove1()
        self._y = map.transformYPointIfOutOfMapLimit(self._y)
        return self

    def west(self, map: Map):
        self._x.remove1()
        self._x = map.transformYPointIfOutOfMapLimit(self._x)
        return self