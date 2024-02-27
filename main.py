from graphics import Window, Line, Point
from maze import Cell, Maze

def main():
    win = Window(1000, 1000)

    # cell1 = Cell(win)
    # cell1.draw(200, 200, 250, 250)

    # cell2 = Cell(win)
    # cell2.draw(300, 300, 350, 350)

    # cell1.draw_move(cell2, undo=True)
    maze = Maze(50, 50, 1, 11, 50, 50, win)


    win.wait_for_close()

main()