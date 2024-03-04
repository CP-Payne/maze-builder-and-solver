import tkinter as tk
from settings.settings import Settings
from threading import Thread, Event

class SolverSettings(Settings):
    def __init__(self, ctrl_panel,maze_panel, root, generation_settings) -> None:
        super().__init__(ctrl_panel,maze_panel, root)
        self.generation_settings = generation_settings
        self.solver_settings_frame = tk.Frame(Settings.settings_container, bg='lightcoral')
        self.solver_settings_button= tk.Button(Settings.button_container, text="Solver Settings", command=lambda: self.show_frame(self.solver_settings_frame))
        self.solver_settings_button.pack(side='top', fill='x')
        Settings.settings_frames.append(self.solver_settings_frame)
        self.add_settings_content()

        self.thread=None
        self.stop_event= Event()

    def add_settings_content(self):
        self.ss_label = tk.Label(self.solver_settings_frame, text='Solve Maze')
        self.ss_label.pack(pady=5, padx=5)
        self.solve_button = tk.Button(self.solver_settings_frame, text="Solve", command=self._solve_maze )
        self.solve_button.pack()

    def _solve_maze(self):
        self.generation_settings.solve_maze(self.stop_event)

    def start_solver(self):
        if self.thread is None or not self.thread.is_alive():
            self.stop_event.clear()
            self.thread=Thread(target=self._solve_maze) 
            self.thread.start()

        

        # self.gs_create_maze_button.config(state="disabled")
        # self.gs_stop_maze_button.config(state="normal")

        # TODO: Validate if entry is integer
        # TODO: Show current speed
        # if self.visualise.get() == 1:
        #     self.speed_entry = tk.Entry(self.generation_settings_frame)
        #     self.speed_entry.pack(side="top", fill= "x")
        #     self.speed_entry.insert(0, "0.01")
        #     self.speed_up_button = tk.Button(self.generation_settings_frame, text="Speed Up", command= lambda: self.maze.change_speed(speed="faster", by=float(self.speed_entry.get())))
        #     self.speed_up_button.pack(side="top", fill="x")
        #     self.speed_down_button = tk.Button(self.generation_settings_frame, text="Speed Down", command= lambda: self.maze.change_speed(speed="slower", by=float(self.speed_entry.get())))
        #     self.speed_down_button.pack(side="top", fill="x")