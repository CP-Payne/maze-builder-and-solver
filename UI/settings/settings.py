import tkinter as tk

class Settings:
    ctrl_panel = None
    maze_panel = None
    button_container = None
    settings_container = None
    root = None
    settings_frames = []
    def __init__(self, ctrl_panel,maze_panel, root) -> None:
        if Settings.ctrl_panel is None:
            Settings.ctrl_panel = ctrl_panel
        if Settings.maze_panel is None:
            Settings.maze_panel = maze_panel

        if Settings.root is None:
            Settings.root = root
        self.init_containers()

    def init_containers(self):
        if Settings.button_container is None:
            Settings.button_container= tk.Frame(Settings.ctrl_panel)
            Settings.button_container.pack(side='top', fill='x')

        if Settings.settings_container is None:
            # Create a frame that will contain the settings frames on the bottom row of the left column
            Settings.settings_container = tk.Frame(Settings.ctrl_panel, bg='white')
            Settings.settings_container.pack(side='top', fill='both', expand=True)

    def show_frame(self, frame):
        # Hide all frames
        for settings_frame in Settings.settings_frames:
            settings_frame.pack_forget()
        # Show the selected frame
        frame.pack(fill='both', expand=True)