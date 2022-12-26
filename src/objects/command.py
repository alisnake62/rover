from typing import TYPE_CHECKING
if TYPE_CHECKING: from src.objects import Deplacement, RoverMessage

from exception import BadCommandValueException

class Command:

    _expectedValue = ["Up", "Down", "Left", "Right"]

    def __init__(self, value:str) -> None:
        if value not in self._expectedValue: raise BadCommandValueException()
        self._value = value

    def doDeplacement(self, deplacement: 'Deplacement') -> 'RoverMessage':
        if self._value == "Up"      : return deplacement.moveUp()
        if self._value == "Down"    : return deplacement.moveDown()
        if self._value == "Left"    : return deplacement.turnLeft()
        if self._value == "Right"   : return deplacement.turnRight()