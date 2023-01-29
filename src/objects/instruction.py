from .deplacement import Deplacement
from .command import Command

from exception import BadInstructionException

class InstructionChecked:

    _value: bool

    def __init__(self, instructionsCheckedBooleanValue:bool = False) -> None:
        self._value = instructionsCheckedBooleanValue

    def __eq__(self, otherInstructionChecked: object) -> bool:
        return self._value == otherInstructionChecked._value

class Instructions:

    _value:str

    _expectedInsctructions = ["U", "D", "L", "R"]

    def _checkInstruction(self, instruction: str, instructionsChecked:InstructionChecked) -> InstructionChecked:
        if instructionsChecked == InstructionChecked(instructionsCheckedBooleanValue=False): return instructionsChecked
        if instruction not in self._expectedInsctructions:
            return InstructionChecked(instructionsCheckedBooleanValue=False)
        return InstructionChecked(instructionsCheckedBooleanValue=True)


    def _checkValue(self) -> None:

        instructionChecked  = InstructionChecked(instructionsCheckedBooleanValue=True)
        instructionList     = self._value.split('-')
        for instruction in instructionList:
            instructionChecked = self._checkInstruction(instruction=instruction, instructionsChecked=instructionChecked)
        
        if instructionChecked == InstructionChecked(instructionsCheckedBooleanValue=False):
            raise BadInstructionException()


    def __init__(self, value:str) -> None:

        self._value = value
        self._checkValue()

    def createCommandList(self, deplacement:Deplacement)->str:

        commandList = []

        instructionList = self._value.split('-')
        for instruction in instructionList:
            
            if instruction == "U": commandList.append(Command("Up"))
            if instruction == "D": commandList.append(Command("Down"))
            if instruction == "L": commandList.append(Command("Left"))
            if instruction == "R": commandList.append(Command("Right"))

        return deplacement.executeCommandList(commands=commandList)