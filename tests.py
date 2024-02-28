import unittest
from graphics import Window
from maze import Maze

class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 800)
        num_cols = 20
        num_rows = 60
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols, 
        )
   
    def test_entrance_and_exit(self):
        win = Window(800, 800)
        num_cols = 20
        num_rows = 20
        m = Maze(0, 0, num_rows, num_cols, 10, 10, win)
         
        self.assertEqual(
            m._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m._cells[-1][-1].has_bottom_wall,
            False,
        )

if __name__== "__main__":
    unittest.main()
