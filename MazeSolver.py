from Board import Maze
import asyncio

''''
Creating Maze solver first python app
Author: ashapira 
version 2
'''
class MazeSolver:

    def __init__(self, maze: Maze, start_point: tuple, end_point: tuple):
        self._maze = maze
        self.traversed_places = dict()
        self._startPoint = start_point
        self._endPoint = end_point

    '''
    Main resolve method 
    @param self:
    '''
    async def ResolveMaze(self):
        await self.NextSteps(self._startPoint, 0)
        print(self.traversed_places[self._endPoint])

    '''
    @:param self
    @:param location: the current location in maze 
    @return: step_number: current step number 
    '''
    async def NextSteps(self, location: tuple, step_number: int):
        if self._maze.getPlaceLocation(location) != 0:
            return
        if location in self.traversed_places and self.traversed_places[location] < step_number:
            return
        self.traversed_places[location] = step_number

        await asyncio.gather(
            self.NextSteps((location[0] + 1, location[1]), step_number + 1),
            self.NextSteps((location[0] - 1, location[1]), step_number + 1),
            self.NextSteps((location[0], location[1] + 1), step_number + 1),
            self.NextSteps((location[0], location[1] - 1), step_number + 1))


async def main():
    mazeSolver = MazeSolver(
        #           0  1  2  3  4  5  6
        maze=Maze([[0, 0, 0, 0, 0, 0, 1],    # 0
                   [0, 1, 1, 1, 1, 0, 1],    # 1
                   [0, 0, 0, 0, 1, 0, 1],    # 2
                   [1, 0, 1, 0, 1, 0, 1],    # 3
                   [0, 0, 0, 0, 0, 0, 0]]),  # 4
        start_point=(0, 4),
        end_point=(6, 4))
    await mazeSolver.ResolveMaze()


if __name__ == '__main__':
    asyncio.run(main())