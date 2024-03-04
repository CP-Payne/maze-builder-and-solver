import tkinter as tk
from settings.settings import Settings
from settings.settings_pages.window_settings import WindowSettings
from settings.settings_pages.generation_settings import GenerationSettings
from settings.settings_pages.solver_settings import SolverSettings
import sys

class HomePage:
    def __init__(self, width, height, ctrl_p_ratio) -> None:
        self.width = width
        self.height = height
        # TODO Rename panel to frame
        self._ctrl_panel_width = int(width * ctrl_p_ratio)
        self._maze_panel_width = width - self._ctrl_panel_width
        self.root = self.init_root()
        self.setup_main_frames()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        #self.settings = Settings(self.control_panel_frame)
        self.win_settings = WindowSettings(self.control_panel_frame, self.maze_display_frame, self.root)
        self.gen_settings = GenerationSettings(self.control_panel_frame, self.maze_display_frame, self.root)
        self.solver_settings = SolverSettings(self.control_panel_frame,self.maze_display_frame, self.root, self.gen_settings)
    
    def on_close(self):
        print("Application is closing")
        self.root.destroy()
        sys.exit()


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
# Create a PanedWindow with two panels
        # self.paned_window = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        # self.paned_window.pack(fill=tk.BOTH, expand=True)

        # # Create control panel frame
        # self.control_panel_frame = tk.Frame(self.paned_window, bg="gray", width=int(self.width * 0.2))
        # self.paned_window.add(self.control_panel_frame, stretch="never")

        # # Create maze panel
        # self.maze_display_frame = tk.Frame(self.paned_window, bg='white')
        # self.paned_window.add(self.maze_display_frame, stretch="always")

        # # This ensures the control panel has an initial width of 20% of the total window width
        # self.paned_window.paneconfig(self.control_panel_frame, minsize=int(self.width * 0.2))

    

if __name__ == "__main__":
    homePage = HomePage(1500, 1200, 0.2)
    homePage.root.mainloop()