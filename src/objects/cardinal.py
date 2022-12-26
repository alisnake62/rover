from exception import BadCardinalValueException

class Cardinal:

    _orderedExpectedValue = ["North", "East", "South", "West"]

    def __init__(self, value:str) -> None:
        if value not in self._orderedExpectedValue: raise BadCardinalValueException()
        self._index = self._orderedExpectedValue.index(value)

    def __eq__(self, otherCardinal: object) -> bool:
        return otherCardinal._index == self._index

    def __str__(self) -> str:
        return self._orderedExpectedValue[self._index]

    def left(self):
        self._index -= 1
        if self._index == -1: self._index = 3
        return self

    def right(self):
        self._index += 1
        if self._index == 4: self._index = 0
        return self

    def isNorth(self) -> bool:
        return self._orderedExpectedValue[self._index] == "North"

    def isEast(self) -> bool:
        return self._orderedExpectedValue[self._index] == "East"

    def isSouth(self) -> bool:
        return self._orderedExpectedValue[self._index] == "South"

    def isWest(self) -> bool:
        return self._orderedExpectedValue[self._index] == "West"