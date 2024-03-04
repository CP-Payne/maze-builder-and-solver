    def _solve_maze(self):
        self.slider.set(1)
        self.generation_settings.solve_maze(self.stop_event)

    def start_solver(self):
        self.generation_settings.maze.speed = 1
        if self.thread is None or not self.thread.is_alive():
            self.stop_event.clear()
            self.thread=Thread(target=self._solve_maze) 
            self.thread.start()
            
    # IN Mazelpy        
    def solve(self, stop_event=None):
        #self._solve_r(0, 0, stop_event, speed)
        self._solve_iterative(stop_event)