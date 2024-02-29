import tkinter as tk
from settings.settings import Settings
from settings.settings_pages.window_settings import WindowSettings
from settings.settings_pages.generation_settings import GenerationSettings
from settings.settings_pages.solver_settings import SolverSettings

class HomePage:
    def __init__(self, width, height, ctrl_p_ratio) -> None:
        self.width = width
        self.height = height
        # TODO Rename panel to frame
        self._ctrl_panel_width = int(width * ctrl_p_ratio)
        self._maze_panel_width = width - self._ctrl_panel_width
        self.root = self.init_root()
        self.setup_main_frames()
        #self.settings = Settings(self.control_panel_frame)
        self.win_settings = WindowSettings(self.control_panel_frame, self.maze_display_frame, self.root)
        self.gen_settings = GenerationSettings(self.control_panel_frame, self.maze_display_frame, self.root)
        self.solver_settings = SolverSettings(self.control_panel_frame,self.maze_display_frame, self.root)
        # Create two main frames
            # Get correct width and heigth
        # Create settings buttons
        # Choose default setting page display

    def init_root(self):
        root = tk.Tk()
        root.title("Maze Builder and Solver")
        root.geometry(f"{self.width}x{self.height}")
        return root

    def setup_main_frames(self):
        # # # Create control panel frame
        self.control_panel_frame = tk.Frame(self.root, width=self._ctrl_panel_width, bg="gray")
        self.control_panel_frame.pack(side="left", fill="y", expand=False)

        # # # Create maze panel
        self.maze_display_frame = tk.Frame(self.root, width=self._maze_panel_width, bg='white')
        self.maze_display_frame.pack(side='right', fill='both', expand=True)

    
    # def change_frame_color(self):
    #     color = ctrl_color_entry.get()

    #     try:
    #         # Change the frame's background color to the entered value
    #         maze_display_frame.config(bg=color)
    #     except tk.TclError:
    #         print(f"The color '{color}' is not a valid color.")

    # def show_frame(self, frame):
    #     # Hide all frames
    #     for settings_frame in settings_frames:
    #         settings_frame.pack_forget()
    #     # Show the selected frame
    #     frame.pack(fill='both', expand=True)

if __name__ == "__main__":
    homePage = HomePage(400, 400, 0.2)
    homePage.root.mainloop()