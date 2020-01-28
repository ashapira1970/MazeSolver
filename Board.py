class Maze:
    def __init__(self, maze):
        self._maze = maze

    def getPlace(self, x: int, y: int):
        if y >= len(self._maze) or x >= len(self._maze[0]) or x < 0 or y < 0:
            return -1
        return self._maze[y][x]

    def getPlaceLocation(self, location: tuple):
        return self.getPlace(location[0], location[1])
