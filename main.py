from src import *

if __name__ == '__main__':
    map = Map(yMax=Point(value=10), xMax=Point(value=10))
    rover = Rover(
        startCardinal   = Cardinal(value="North"),
        startCoordonnee = Coordonnee(y=Point(value=0), x=Point(value=0))
        )
    deplacement = Deplacement(map=map, rover=rover)

    print(map._xMax._value)