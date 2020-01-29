import unittest

from Board import Maze


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.maze = Maze([[1,2],
                           [3,4]])

    def test_get_fault_board_index(self):
        self.assertEqual(self.maze.getPlaceLocation((10, 1)), -1)
        self.assertEqual(self.maze.getPlaceLocation((1, 10)), -1)

    def test_get_correct_index(self):
        self.assertEqual(self.maze.getPlaceLocation((0, 0)), 1)
        self.assertEqual(self.maze.getPlaceLocation((0, 1)), 3)
        self.assertEqual(self.maze.getPlaceLocation((1, 1)), 4)
        self.assertEqual(self.maze.getPlaceLocation((1, 0)), 2)



if __name__ == '__main__':
    unittest.main()