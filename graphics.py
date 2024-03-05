from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Solve The Maze")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack()
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True

        while self.__running:
            self.redraw()
        
    def close(self):
        self.__running = False

    def draw_line(self, line, color="black"):
        line.draw(canva=self.__canvas, fill_color=color)


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self,start_point, end_point) -> None:
        self.start_point = start_point
        self.end_point = end_point 

    def draw(self, canva, fill_color="black"):
        canva.create_line(self.start_point.x, self.start_point.y, self.end_point.x, self.end_point.y, fill=fill_color, width=2)
        canva.pack()
        
class MazeWindow:
    def __init__(self, root_tk, maze_panel) -> None:
        self.__root = root_tk
        self.maze_panel = maze_panel
        #self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.root = self.__root
        self.__canvas = Canvas(self.maze_panel, width=self.maze_panel.winfo_width(), height=self.maze_panel.winfo_height())
        self.__canvas.pack(fill="both", expand=True)
        self.canvas = self.__canvas
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True

        while self.__running:
            self.redraw()
        
    def close(self):
        self.__running = False

    def draw_line(self, line, color="black"):
        line.draw(canva=self.__canvas, fill_color=color)

    def clear_canvas(self):
        self.__canvas.delete("all")