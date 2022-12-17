class RoverAppException(Exception):

    _message = "roverAppException"

    def __init__(self, message: str = None) -> None:
        if message is None: super().__init__(self._message)
        else: super().__init__(message)

class BadPointValueException(RoverAppException):
    _message = "Bad Point Value"

class BadCardinalValueException(RoverAppException):
    _message = "The Cardfinal Value Must Be One of ('North', 'South', 'East', 'West')"

class OutSideMapException(RoverAppException):
    _message = "The position of the rover is not in the Map"