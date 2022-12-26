from exception import BadPointValueException

class Point:

    def __init__(self, value:int=0) -> None:

        if not isinstance(value, int)   : raise BadPointValueException(message="The Point Value Must Be Integer")
        if value < 0                    : raise BadPointValueException(message="The Point Value Must Positive or 0")
        self._value = value

    def __eq__(self, otherPoint: object) -> bool:
        return otherPoint._value == self._value

    def __gt__(self, otherPoint:object) -> bool:
        return self._value > otherPoint._value

    def add1(self):
        self._value += 1
        return self

    def remove1(self):
        self._value -= 1
        return self

    def isNegative(self) -> bool:
        return self._value == -1