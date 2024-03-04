import tkinter as tk
from tkinter import messagebox
from settings.settings import Settings
from threading import Thread, Event

import sys

sys.path.append("/home/charles/active_projects/maze-builder-and-solver/")
from graphics import MazeWindow
from maze import Maze

class GenerationSettings(Settings):
    def __init__(self, ctrl_panel,maze_panel,root) -> None:
        super().__init__(ctrl_panel,maze_panel, root)
        self.generation_settings_frame = tk.Frame(Settings.settings_container, bg='lightgreen')
        self.generation_settings_button= tk.Button(Settings.button_container, text="Maze Generation Settings", command=lambda: self.show_frame(self.generation_settings_frame))
        self.generation_settings_button.pack(side='top', fill='x')
        Settings.settings_frames.append(self.generation_settings_frame)
        self.mazeWin = MazeWindow(Settings.root, Settings.maze_panel)
        self.add_settings_content()
        self.thread=None
        self.stop_event= None
        self.maze = None

    def add_settings_content(self):
        self.rows_label = tk.Label(self.generation_settings_frame, text='Rows:')
        self.rows_label.pack(pady=5, padx=5)
        self.rows_entry = tk.Entry(self.generation_settings_frame)
        self.rows_entry.pack(pady=5, padx=5)
        
        self.cols_label = tk.Label(self.generation_settings_frame, text='Cols:')
        self.cols_label.pack(pady=5, padx=5)
        self.cols_entry = tk.Entry(self.generation_settings_frame)
        self.cols_entry.pack(pady=5, padx=5)

        self.cell_size_label = tk.Label(self.generation_settings_frame, text='Cell Size:')
        self.cell_size_label.pack(pady=5, padx=5)
        self.cell_size_entry = tk.Entry(self.generation_settings_frame)
        self.cell_size_entry.pack(pady=5, padx=5)
        self.cell_size_entry.insert(0, "20")

        self.gs_create_maze_button = tk.Button(self.generation_settings_frame, text="Generate Maze", command=self.start_maze_generation)
        self.gs_create_maze_button.pack(side="top", fill="x")
        self.visualise = tk.IntVar()
        self.gs_animate_check = tk.Checkbutton(self.generation_settings_frame, text="Visualise Creation", variable=self.visualise, offvalue=0,onvalue=1)
        self.gs_animate_check.pack(side="top" )
        self.gs_stop_maze_button = tk.Button(self.generation_settings_frame, text="Stop Maze Generation", command=self.stop_maze_generation)
        self.gs_stop_maze_button.pack(side="top", fill="x")


    def _generate_maze(self, stop_event):
        row_num = int(self.rows_entry.get())
        col_num = int(self.cols_entry.get())
        cell_size = int(self.cell_size_entry.get())
    
        x_offset, y_offset = self.calculate_maze_position(row_num, col_num, cell_size)
            
        if x_offset is not None and y_offset is not None:
            self.maze = Maze(x_offset, y_offset, row_num, col_num, cell_size,cell_size, self.mazeWin, seed=None, stop_event=stop_event, should_animate=self.visualise.get())
            self.maze.generate_maze()
            self.gs_create_maze_button.config(state="normal")
            self.gs_stop_maze_button.config(state="disabled")
            # TODO: Remove below only if animate is on and maze generation finished
            if self.visualise.get() == 1:
                self.speed_down_button.destroy()
                self.speed_up_button.destroy()
                self.speed_entry.destroy()
        else:
            self.gs_create_maze_button.config(state="normal")
            self.gs_stop_maze_button.config(state="disabled")
            if self.visualise.get() == 1:
                self.speed_down_button.destroy()
                self.speed_up_button.destroy()
                self.speed_entry.destroy()

    def start_maze_generation(self):
        # Prevent starting multiple threads
        if self.thread and self.thread.is_alive():
            return
        self.stop_event = Event()
        self.mazeWin.clear_canvas()
        self.thread = Thread(target=lambda: self._generate_maze(self.stop_event))
        self.thread.start()
        self.gs_create_maze_button.config(state="disabled")
        self.gs_stop_maze_button.config(state="normal")

        # TODO: Validate if entry is integer
        # TODO: Show current speed
        if self.visualise.get() == 1:
            self.speed_entry = tk.Entry(self.generation_settings_frame)
            self.speed_entry.pack(side="top", fill= "x")
            self.speed_entry.insert(0, "0.01")
            self.speed_up_button = tk.Button(self.generation_settings_frame, text="Speed Up", command= lambda: self.maze.change_speed(speed="faster", by=float(self.speed_entry.get())))
            self.speed_up_button.pack(side="top", fill="x")
            self.speed_down_button = tk.Button(self.generation_settings_frame, text="Speed Down", command= lambda: self.maze.change_speed(speed="slower", by=float(self.speed_entry.get())))
            self.speed_down_button.pack(side="top", fill="x")

    def stop_maze_generation(self):
        if self.maze.stop_event:
            self.maze.stop_event.set()
        self.gs_create_maze_button.config(state="normal")
        self.gs_stop_maze_button.config(state="disabled")
    
    def solve_maze(self, stop_event):
        self.maze.solve(stop_event)

    def calculate_maze_position(self, num_rows, num_cols, cell_size):
        x_offset = (Settings.maze_panel.winfo_width()//2) - ((num_cols * cell_size) // 2)
        y_offset = (Settings.maze_panel.winfo_height()//2) - ((num_rows * cell_size) // 2)
        if x_offset < 0:
            # Check if maze will fit on screen (width)
            messagebox.showerror("Error", "Maze cannot fit into screen. Options: \n- Increase window width\n- Reduce maze columns\n- Reduce cell size")
            x_offset = None
        elif y_offset < 0:
            # Check if maze will fit on screen (height)
            messagebox.showerror("Error", "Maze cannot fit into screen. Options: \n- Increase window height\n- Reduce maze rows\n- Reduce cell size")
            y_offset = None
        else:
            # Maze can fit on screen
            return (x_offset, y_offset)