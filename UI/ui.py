import tkinter as tk

class HomePage:
    def __init__(self, width, height, ctrl_p_ratio) -> None:
        self.width = width
        self.height = height
        # TODO Rename panel to frame
        self._ctrl_panel_width = int(width * ctrl_p_ratio)
        self._maze_panel_width = width - self._ctrl_panel_width
        self.root = self.init_root()
        self.setup_main_frames()
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
        self.control_panel_frame.pack(side="left", fill="y", expand=True)

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