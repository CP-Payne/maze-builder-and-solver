import tkinter as tk
from settings.settings import Settings

class SolverSettings(Settings):
    def __init__(self, ctrl_panel,maze_panel, root) -> None:
        super().__init__(ctrl_panel,maze_panel, root)
        self.solver_settings_frame = tk.Frame(Settings.settings_container, bg='lightcoral')
        self.solver_settings_button= tk.Button(Settings.button_container, text="Solver Settings", command=lambda: self.show_frame(self.solver_settings_frame))
        self.solver_settings_button.pack(side='top', fill='x')
        Settings.settings_frames.append(self.solver_settings_frame)

        self.add_settings_content()

    def add_settings_content(self):
        self.ss_label = tk.Label(self.solver_settings_frame, text='Generation Size:')
        self.ss_label.pack(pady=5, padx=5)
        self.ss_entry = tk.Entry(self.solver_settings_frame)
        self.ss_entry.pack(pady=5, padx=5)