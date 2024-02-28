from graphics import Line, Window, Point
import time
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None) -> None:
        self.x1 = x1
        self.y1 = y1
        # TODO: Add seed as parameter to init. Update rest of code to reflect
        self.seed = seed
        if self.seed:
            random.seed(self.seed)
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
    
    def _create_cells(self):
        for row in range(self.num_rows):
            row_cells = []
            for col in range(self.num_cols):
                cell = Cell(self._win)
                #cell.draw((col*self.cell_size_x)+self.x1, (row*self.cell_size_y)+self.y1,((col+1)*self.cell_size_x)+self.x1, ((row+1)*self.cell_size_y)+self.y1)
                row_cells.append(cell)
            self._cells.append(row_cells)
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._draw_cell(row, col)
                

    def _draw_cell(self, row, col):
        x1 = (col*self.cell_size_x)+self.x1
        y1 = (row*self.cell_size_y)+self.y1
        x2 = ((col+1)*self.cell_size_x)+self.x1
        y2 = ((row+1)*self.cell_size_y)+self.y1
        self._cells[row][col].draw(x1, y1, x2, y2)

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self.num_rows-1, self.num_cols-1)

    def _get_valid_adjacent_cells_i(self, row, col):
        adjacent_cells = []
        # Checking right and left cells
        if col > 0 and self._cells[row][col-1].visited == False:
            adjacent_cells.append((row, col-1)) 
        if col < self.num_cols-1 and self._cells[row][col+1].visited == False:
            adjacent_cells.append((row, col+1)) 
        # Checking top and bottom cells
        if row < self.num_rows - 1 and self._cells[row+1][col].visited == False:
            adjacent_cells.append((row+1, col)) 
        if row > 0 and self._cells[row-1][col].visited == False:
            adjacent_cells.append((row-1, col))
        return adjacent_cells
    
    def _break_cell_wall(self, row, col, adjacent_cell):
        break_direction = (row-adjacent_cell[0], col-adjacent_cell[1])

        if break_direction[0] == 0:
            # Cells in same row
            # Determine to break left or right
            if break_direction[1] == -1:
                # Break current cell's right wall and adjacent cell's left wall
                self._cells[row][col].has_right_wall = False
                self._cells[adjacent_cell[0]][adjacent_cell[1]].has_left_wall = False
            elif break_direction[1] == 1:
                # Break current cell's left wall and adjacent cell's right wall
                self._cells[row][col].has_left_wall = False
                self._cells[adjacent_cell[0]][adjacent_cell[1]].has_right_wall = False
        elif break_direction[1] == 0:
            # Cells in same column
            # Determine to break top or bottom
            if break_direction[0] == -1:
                # Break current cell's bottom wall and adjacent cell's top wall
                self._cells[row][col].has_bottom_wall = False
                self._cells[adjacent_cell[0]][adjacent_cell[1]].has_top_wall = False
            elif break_direction[0] == 1:
                # Break current cell's top wall and adjacent cell's bottom wall
                self._cells[row][col].has_top_wall = False
                self._cells[adjacent_cell[0]][adjacent_cell[1]].has_bottom_wall = False
            
    # TODO: Recursion limit reached to fast. Use stack to simulate recursion
    def _break_walls_r(self, row, col):
        self._cells[row][col].visited = True
        while True:
            to_visit = self._get_valid_adjacent_cells_i(row, col)
            if len(to_visit) == 0:
                self._draw_cell(row, col) 
                return

            random_direction = random.choice(to_visit)
            self._break_cell_wall(row, col, random_direction)
            self._break_walls_r(random_direction[0], random_direction[1])
            
            
            
            

class Cell:
    def __init__(self, window) -> None:
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.visited = False
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        color = "#d9d9d9"

        if self.has_bottom_wall:
            color="black"
        start_point = Point(x1, y2)
        end_point = Point(x2,y2)
        bottom_line = Line(start_point, end_point)
        self._win.draw_line(bottom_line, color)

        color="#d9d9d9"
        if self.has_top_wall:
            color="black"
        start_point = Point(x1, y1)
        end_point = Point(x2, y1)
        top_line= Line(start_point, end_point)
        self._win.draw_line(top_line, color)

        color="#d9d9d9"
        if self.has_left_wall:
            color="black"
        start_point = Point(x1, y1)
        end_point = Point(x1, y2)
        left_line= Line(start_point, end_point)
        self._win.draw_line(left_line, color)

        color="#d9d9d9"
        if self.has_right_wall:
            color="black"
        start_point = Point(x2, y1)
        end_point = Point(x2, y2)
        right_line= Line(start_point, end_point)
        self._win.draw_line(right_line, color)
    
    def get_midpoint(self):
        return Point(x=(self._x1 + self._x2)/2, y=(self._y1+self._y2)/2)
        
    def draw_move(self, to_cell, undo=False):
        current_point = self.get_midpoint()
        to_point = to_cell.get_midpoint()
        line = Line(current_point, to_point)
        color = "red"
        if undo:
            color = "gray"

        self._win.draw_line(line, color)

    