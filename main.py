from graphics import Window, Line, Point
from maze import Cell, Maze
import sys

def main():
    win = Window(1000, 1000)

    # Large maze sizes causes program to reach recursion depth to fast. 
    # Not recommended to change the recursion depth though :O
    sys.setrecursionlimit(10000)

    # x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None
    maze = Maze(50, 50, 30, 30, 30, 30, win)

    win.wait_for_close()

main()