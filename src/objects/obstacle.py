from src.objects import Coordonnee, Map

class Obstacle:

    def __init__(self, coordonnee:Coordonnee) -> None:
        self._coordonnee = coordonnee

    def __eq__(self, otherobstacle: object) -> bool:
        return otherobstacle._coordonnee == self._coordonnee

    def __str__(self) -> str:
        return f"{self._coordonnee}"

    def isInMap(self, map:Map) -> bool:
        return self._coordonnee.isInMap(map=map)

    def here(self, coordonnee: Coordonnee) -> bool:
        return self._coordonnee == coordonnee