from src import *
from src.earthLink import EarthLink

if __name__ == '__main__':

    # initilisation de la map avec les obstacles ainsi que du Rover
    obstacle    = Obstacle(coordonnee=Coordonnee(y=Point(value=2), x=Point(value=2)))
    obstacle2   = Obstacle(coordonnee=Coordonnee(y=Point(value=1), x=Point(value=3)))
    map = Map(yMax=Point(value=10), xMax=Point(value=10), obstacles=[obstacle, obstacle2])
    roverTest = Rover(
        startCardinal   = Cardinal(value="North"),
        startCoordonnee = Coordonnee(y=Point(value=0), x=Point(value=0))
        )
    deplacementRover = Deplacement(map=map, rover=roverTest)

    # initialisation de la connextion avec la console sur terre (Module EarthLink)
    with EarthLink(deplacement=deplacementRover) as earthLink:

        # attente de connexion de la console
        earthLink.waitClient()

        # instructions provenant de la console
        while True:
            earthLink.listenInstructions()
