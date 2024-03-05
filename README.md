# Maze Builder and Solver

Maze Builder and Solver is an application designed for creating and solving mazes. It enables users to both generate and run an automatic solver to solve mazes via a graphical user interface (GUI).

## Features

- **Maze Generation:** Create mazes with an iterative algorithm. The generation process is visualized, allowing you to watch the maze take shape in real time.

- **Control Panel:** Customize your maze with adjustable settings for size and generation speed.

- **Solving Visualization:** Observe the solver in action as it navigates the maze. Adjustable speeds let you control the visualization of the solving process.

## Screenshots

### Maze in the Process of Being Generated
![Maze Generating](/readme_images/in_process_generating.png)

### Maze Generation Finished
![Generated Maze](/readme_images/generated_maze_1.png)

### Solver in Action
![Solver In Action](/readme_images/in_process_solving.png)

### Solver Finished
![Solver Finished](/readme_images/finished_solving.png)

## How to Use

1. Launch the application with `python UI/ui.py`
1. Begin by generating a maze using the 'Maze Generation Settings' panel, selecting your desired dimensions.
2. After the maze is generated, proceed to the 'Solver Settings' panel to initiate the maze solver.
3. Click 'Start' to commence the solving process. You can watch the solver's progress through the maze and manage the speed using the speed controller.

## Installation
Maze Builder and Solver requires Python and Tkinter, which is included by default in most Python installations. Follow these steps to install and run Maze Builder and Solver:

### Running the Application

1. **Download the Source Code:**  
   Obtain the source code by downloading the ZIP file and extracting it, or by cloning the repository using Git.

2. **Navigate to the Application Directory:**  
   Open your command line interface and navigate to the application directory with the command:
   ```bash
   cd path/to/maze-builder-and-solver
   ```
Replace path/to/maze-builder-and-solver with the actual path to the application's directory.

3. **Run the Application:**  
Start the application by executing the `ui.py` Python script within the UI folder:
```bash
    python UI/ui.py
```
## Technologies

- **Tkinter**: Utilizes the Tkinter library for the GUI.
- **Python Threading**: Implements Python's threading capabilities to ensure the application remains responsive during maze generation and solving.

## Future Enchancements

- Add the ability to save and load generated mazes.
- Implement various solving algorithms and allow the user to choose between them.
- Add support for maze editing and manual path drawing

Note: The application already contains methods to generate and solve the maze recursively, however, this methods are not called or used in the application.