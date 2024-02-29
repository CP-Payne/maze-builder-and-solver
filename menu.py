import tkinter as tk
from screeninfo import get_monitors

def change_frame_color():
    color = ctrl_color_entry.get()

    try:
        # Change the frame's background color to the entered value
        maze_display_frame.config(bg=color)
    except tk.TclError:
        print(f"The color '{color}' is not a valid color.")

def show_frame(frame):
    # Hide all frames
    for settings_frame in settings_frames:
        settings_frame.pack_forget()
    # Show the selected frame
    frame.pack(fill='both', expand=True)
    

root = tk.Tk()

root.title("Maze Builder and Solver")

window_width = 1500
window_height = 1000
# for m in get_monitors():
#     if m.is_primary:
#         window_width = m.width
#         window_height = m.height
#         break
root.geometry(f"{window_width}x{window_height}")

# Calculate widths for the main frames
control_panel_width = int(window_width * 0.2)
maze_display_width = window_width - control_panel_width

# # # Create control panel frame
control_panel_frame = tk.Frame(root, width=control_panel_width, bg="gray")
control_panel_frame.pack(side="left", fill="y", expand=True)

# # # Create maze panel
maze_display_frame = tk.Frame(root, width=maze_display_width, bg='white')
maze_display_frame.pack(side='right', fill='both', expand=True)

# TODO HERE HERE HRER HERE
# Create a main frame for the left column
# left_column = tk.Frame(root)
# left_column.pack(side='left', fill='both', expand=True)

# # Create a frame for the buttons on the top row of the left column
button_frame = tk.Frame(control_panel_frame)
button_frame.pack(side='top', fill='x')

# # Create a frame that will contain the settings frames on the bottom row of the left column
settings_container = tk.Frame(control_panel_frame, bg='white')
settings_container.pack(side='top', fill='both', expand=True)

# # Create the main maze display frame on the right column
# maze_display_frame = tk.Frame(root, bg='white')
# maze_display_frame.pack(side='left', fill='both', expand=True)

# Create individual frames for each settings page within the settings container
window_settings_frame = tk.Frame(settings_container, bg='lightblue')
maze_generation_settings_frame = tk.Frame(settings_container, bg='lightgreen')
solver_settings_frame = tk.Frame(settings_container, bg='lightcoral')

# List of settings frames for easier management
settings_frames = [window_settings_frame, maze_generation_settings_frame, solver_settings_frame]

# Create buttons that will show each settings page
window_settings_button = tk.Button(button_frame, text="Window Settings", command=lambda: show_frame(window_settings_frame))
window_settings_button.pack(side='top', fill='x')

maze_generation_settings_button = tk.Button(button_frame, text="Maze Generation Settings", command=lambda: show_frame(maze_generation_settings_frame))
maze_generation_settings_button.pack(side='top', fill='x')

solver_settings_button = tk.Button(button_frame, text="Solver Settings", command=lambda: show_frame(solver_settings_frame))
solver_settings_button.pack(side='top', fill='x')

# Add widgets to each settings page
# Example widgets for window settings
ws_label = tk.Label(window_settings_frame, text='Window Size:')
ws_label.pack(pady=5)
ws_entry = tk.Entry(window_settings_frame)
ws_entry.pack(pady=5)

# # ... Add widgets for maze generation settings ...
# # ... Add widgets for solver settings ...

# # By default, show the window settings frame
show_frame(window_settings_frame)

# # ... Add widgets for maze generation settings ...
# # ... Add widgets for solver settings ...


# # Create control panel frame
# control_panel_frame = tk.Frame(root, width=control_panel_width, bg="gray")
# control_panel_frame.pack(side="left", fill="y")

# #TODO: Add widgets to the control panel

# ctrl_color_entry = tk.Entry(control_panel_frame)
# ctrl_color_entry.pack(pady=10)

# change_color_button = tk.Button(control_panel_frame, text="Change Color", command=change_frame_color)
# change_color_button.pack(pady=5)

# # Create maze panel
# maze_display_frame = tk.Frame(root, width=maze_display_width, bg='white')
# maze_display_frame.pack(side='right', fill='both', expand=True)

# TODO: Add maze frame and widgets here


# lbl = Label(root, text="Are you a Geek?")
# lbl.grid()

# txt= Entry(root, width=10)
# txt.grid(row=0, column=1)

# def clicked():
#     res = f"You wrote {txt.get()}"
#     lbl.configure(text=res)
    
# btn = Button(root, text="Click me", fg="red", command=clicked)

# btn.grid(row=0, column=2)



root.mainloop()