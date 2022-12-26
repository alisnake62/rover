from src import *

if __name__ == '__main__':
    obstacleTest = Obstacle(coordonnee=Coordonnee(y=Point(value=2), x=Point(value=2)))
    obstacleTest2 = Obstacle(coordonnee=Coordonnee(y=Point(value=1), x=Point(value=3)))

    mapTest = Map(yMax=Point(value=10), xMax=Point(value=10), obstacles=[obstacleTest, obstacleTest2])
    roverTest = Rover(
        startCardinal   = Cardinal(value="North"),
        startCoordonnee = Coordonnee(y=Point(value=0), x=Point(value=0))
        )
    deplacementTest = Deplacement(map=mapTest, rover=roverTest)

    print(deplacementTest.moveUp())
    print(deplacementTest.turnRight())
    print(deplacementTest.moveUp())
    print(deplacementTest.moveUp())
    print(deplacementTest.turnLeft())
    print(deplacementTest.moveUp())
    print(deplacementTest.turnRight())
    print(deplacementTest.moveUp())
    print(deplacementTest.moveDown())
    print(deplacementTest.turnRight())
    print(deplacementTest.turnRight())
    print(deplacementTest.moveDown())
    print(deplacementTest.moveDown())

    print("Command List")

    commandList = [
        Command("Up"),
        Command("Left"),
        Command("Left"),
        Command("Up"),
        Command("Up"),
        Command("Up")
    ]

    print(deplacementTest.executeCommandList(commands=commandList))