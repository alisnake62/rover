class Rover:

    def easy(self):
        return 1

class Orientation:

    def __init__(self, cardinal):
        self.cardinal = cardinal

    def __eq__(self, otherOrientation):
        return self.cardinal == otherOrientation.cardinal

def main():
    rover = Rover()
    rover.easy()

if __name__ == '__main__':
    main()