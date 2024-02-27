from graphics import Line, Window, Point
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        for row in range(self.num_rows):
            row_cells = []
            for col in range(self.num_cols):
                cell = Cell(self._win)
                #cell.draw((col*self.cell_size_x)+self.x1, (row*self.cell_size_y)+self.y1,((col+1)*self.cell_size_x)+self.x1, ((row+1)*self.cell_size_y)+self.y1)
                row_cells.append(cell)
            self._cells.append(row_cells)
        for row in range(self.num_cols):
            for col in range(self.num_rows):
                self._draw_cell(row, col)
                

    def _draw_cell(self, col, row):
        x1 = (col*self.cell_size_x)+self.x1
        y1 = (row*self.cell_size_y)+self.y1
        x2 = ((col+1)*self.cell_size_x)+self.x1
        y2 = ((row+1)*self.cell_size_y)+self.y1
        self._cells[col][row].draw(x1, y1, x2, y2)

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

class Cell:
    def __init__(self, window) -> None:
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_bottom_wall:
            start_point = Point(x1, y2)
            end_point = Point(x2,y2)
            bottom_line = Line(start_point, end_point)
            self._win.draw_line(bottom_line)
        if self.has_top_wall:
            start_point = Point(x1, y1)
            end_point = Point(x2, y1)
            top_line= Line(start_point, end_point)
            self._win.draw_line(top_line)
        if self.has_left_wall:
            start_point = Point(x1, y1)
            end_point = Point(x1, y2)
            left_line= Line(start_point, end_point)
            self._win.draw_line(left_line)
        if self.has_right_wall:
            start_point = Point(x2, y1)
            end_point = Point(x2, y2)
            right_line= Line(start_point, end_point)
            self._win.draw_line(right_line)
    
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