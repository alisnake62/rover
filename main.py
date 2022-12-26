from src import *

if __name__ == '__main__':
    mapTest = Map(yMax=Point(value=10), xMax=Point(value=10))
    roverTest = Rover(
        startCardinal   = Cardinal(value="North"),
        startCoordonnee = Coordonnee(y=Point(value=0), x=Point(value=0))
        )
    deplacementTest = Deplacement(map=mapTest, rover=roverTest)

    # print(map._xMax._value)

    roverPosition = deplacementTest._rover._position

    message = RoverMessagePosition(roverPosition=roverPosition)
    print(message)

    deplacementTest.moveUp()
    message = RoverMessagePosition(roverPosition=roverPosition)
    print(message)

    deplacementTest.turnLeft()
    message = RoverMessagePosition(roverPosition=roverPosition)
    print(message)

    deplacementTest.moveUp()
    message = RoverMessagePosition(roverPosition=roverPosition)
    print(message)

    deplacementTest.moveUp()
    message = RoverMessagePosition(roverPosition=roverPosition)
    print(message)
    