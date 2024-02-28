Maze generator:

Currently using recursion to generate the maze. However, if the maze is to big (too many rows x cols) the program throughs a depth recursion error. This is currently bypassed by setting the recursion depth limit a lot higher but is not recommended as it can result in an overflow.

- TODO: Create a new branch that creates the maze using a Stack instead of recursion

If the maze is bigger than the screen then not all cells are printed to the screen. Even if you resize the window.

- Calculate cell size based on window size.

Maze Solver

Using TKinter
