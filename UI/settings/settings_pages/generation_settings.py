import tkinter as tk
from settings.settings import Settings

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

        self.add_settings_content()

    def add_settings_content(self):
        self.gs_label = tk.Label(self.generation_settings_frame, text='Generation Size:')
        self.gs_label.pack(pady=5, padx=5)
        self.gs_entry = tk.Entry(self.generation_settings_frame)
        self.gs_entry.pack(pady=5, padx=5)

        self.gs_create_maze_button = tk.Button(self.generation_settings_frame, text="Generate Maze", command=self.generate_maze)
        self.gs_create_maze_button.pack(side="top", fill="x")

    def generate_maze(self):
        mazeWin = MazeWindow(Settings.root, Settings.maze_panel)
        maze = Maze(20, 20, 60, 60, 20, 20, mazeWin, seed=None)