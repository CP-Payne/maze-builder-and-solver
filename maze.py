from graphics import Line, Window, Point

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