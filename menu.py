import tkinter as tk
from screeninfo import get_monitors

def change_frame_color():
    color = ctrl_color_entry.get()

    try:
        # Change the frame's background color to the entered value
        maze_display_frame.config(bg=color)
    except tk.TclError:
        print(f"The color '{color}' is not a valid color.")


    
# for m in get_monitors():
#     if m.is_primary:
#         window_width = m.width
#         window_height = m.height
#         break



# # Create the main maze display frame on the right column
# maze_display_frame = tk.Frame(root, bg='white')
# maze_display_frame.pack(side='left', fill='both', expand=True)

# Create individual frames for each settings page within the settings container

maze_generation_settings_frame = tk.Frame(settings_container, bg='lightgreen')
solver_settings_frame = tk.Frame(settings_container, bg='lightcoral')

# List of settings frames for easier management
settings_frames = [ maze_generation_settings_frame, solver_settings_frame]

# Create buttons that will show each settings page

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