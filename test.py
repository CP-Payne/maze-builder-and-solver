class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None, stop_event=None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.seed = seed
        if self.seed:
            random.seed(self.seed)
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self.stop_event = stop_event
        self._create_cells()
        self._break_entrance_and_exit()
        #self._break_walls_r(0, 0)
        #self._break_walls_iterative()
        #self.generate_maze()
        #self._reset_cells_visited()
    
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
                

....

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)


....

    def generate_maze(self):
        #self._break_walls_r(0, 0)
        self._break_walls_iterative()
        self._reset_cells_visited()
        self._win.close()
            
....
    def _break_walls_iterative(self):
        stack = [(0, 0)]
        self._cells[0][0].visited = True

        while stack:
            if self.stop_event is not None and self.stop_event.is_set():
                print("Maze generation stopped.")
                return
            row, col = stack.pop()
            self._animate()  # If you want to animate the process
            to_visit = self._get_unvisited_adjacent_cells_i(row, col)

            if to_visit:
                # Push the current cell back onto the stack
                stack.append((row, col))
                # Choose a random adjacent cell to visit next
                next_row, next_col = random.choice(to_visit)
                # Break the wall between the current cell and the chosen adjacent cell
                self._break_cell_wall(row, col, (next_row, next_col))
                # Mark the chosen cell as visited and add it to the stack
                self._cells[next_row][next_col].visited = True
                stack.append((next_row, next_col))
                # Draw the current and adjacent cells to visually update the maze
                self._draw_cell(row, col)
                self._draw_cell(next_row, next_col)

    def _reset_cells_visited(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self._cells[row][col].visited=False

....