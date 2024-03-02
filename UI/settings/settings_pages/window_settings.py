import tkinter as tk
from tkinter import messagebox
from settings.settings import Settings


class WindowSettings(Settings):
    def __init__(self, ctrl_panel, maze_panel, root) -> None:
        super().__init__(ctrl_panel,maze_panel, root)
        self.window_settings_frame = tk.Frame(Settings.settings_container, bg='lightblue')
        self.window_settings_button = tk.Button(Settings.button_container, text="Window Settings", command=lambda: self.show_frame(self.window_settings_frame))
        self.window_settings_button.pack(side='top', fill='x')
        Settings.settings_frames.append(self.window_settings_frame)

        self.add_settings_content()

    def add_settings_content(self):
        # Width widgets (label + entry)
        self.w_width_label = tk.Label(self.window_settings_frame, text='Window Width')
        self.w_width_label.pack(pady=5)
        self.w_width_entry = tk.Entry(self.window_settings_frame)
        self.w_width_entry.pack(pady=5)
        # Heigth widgets (label + entry)
        self.w_height_label = tk.Label(self.window_settings_frame, text='Window Height')
        self.w_height_label.pack(pady=5)
        self.w_height_entry= tk.Entry(self.window_settings_frame)
        self.w_height_entry.pack(pady=5)

        self.save_button = tk.Button(self.window_settings_frame, text="Save Settings", command=lambda: self.change_window_size())
        self.save_button.pack(side="top", fill='x')

    def change_window_size(self):


        width = self.w_width_entry.get()
        if width == "":
            width = Settings.root.winfo_width()
        else:
            try:
                width = int(width)
                if width < 0:
                    width = abs(width)
                    messagebox.showinfo("Info", f"Value converted to +{width}")
                    
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")
                
        height = self.w_height_entry.get()
        if height == "":
            height = Settings.root.winfo_height()
        else:
            try:
                height= int(height)
                if height < 0:
                    height = abs(height)
                    messagebox.showinfo("Info", f"Value converted to +{height}")
                    
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")  


        Settings.root.geometry(f"{width}x{height}")
       
