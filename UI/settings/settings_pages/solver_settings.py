import tkinter as tk
from settings.settings import Settings
from threading import Thread, Event

class SolverSettings(Settings):
    def __init__(self, ctrl_panel,maze_panel, root, generation_settings) -> None:
        super().__init__(ctrl_panel,maze_panel, root)
        self.generation_settings = generation_settings
        self.solver_settings_frame = tk.Frame(Settings.settings_container, highlightbackground="gray", highlightthickness=0.5)
        self.solver_settings_button= tk.Button(Settings.button_container, text="Solver Settings", command=lambda: self.show_frame(self.solver_settings_frame))
        self.solver_settings_button.pack(side='top', fill='x')
        Settings.settings_frames.append(self.solver_settings_frame)
        self.speed = 0
        self.spin_val = 0
        self.add_settings_content()

        self.thread=None
        self.stop_event= Event()
    
    def on_slider_change(self, value):
        if self.generation_settings.maze is not None:
            self.generation_settings.maze.speed =int(value) ###self.spin_val.get()
        print("Slider Value: ", type(value))

    def add_settings_content(self):
        self.ss_label = tk.Label(self.solver_settings_frame, text='Solve Maze', font='Helvetica 12 bold')
        self.ss_label.pack(pady=5, padx=5)

        self.sc_label = tk.Label(self.solver_settings_frame, text='Speed Controller:', anchor="w", font='Helvetica 8 bold')
        self.sc_label.pack(fill="x", pady=(5, 0), padx=(5, 0))

        self.slider = tk.Scale(self.solver_settings_frame, from_=1, to=5, orient='horizontal', command=self.on_slider_change)
        self.slider.pack(side='top', fill="x")

        self.solve_button = tk.Button(self.solver_settings_frame, text="Start",textvariable=self.spin_val, command=self.start_solver)
        self.solve_button.pack(side="top", fill="x")
        
        # self.spinbox = tk.Spinbox(self.solver_settings_frame, from_=1, to=10, command=self.on_slider_change)
        # self.spinbox.pack(side="top")

    def _solve_maze(self):
        self.slider.set(1)
        self.generation_settings.solve_maze(self.stop_event)

    def start_solver(self):
        self.generation_settings.maze.speed = 1
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