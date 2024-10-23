# Motion Planning with A* Search on a Rectangular Grid

This repository implements a motion planning algorithm on a rectangular grid using the **A\* search algorithm**. The grid consists of randomly placed obstacles, and the objective is to find the optimal path from a start position to a goal position using the A* search technique, which combines **heuristics** and **cost functions** to ensure efficient pathfinding.

### How It Works
This motion planning solver navigates a grid from the upper-left corner to the lower-right corner, avoiding obstacles along the way. The A* search algorithm is employed to ensure the most optimal path is found, based on the **Manhattan distance heuristic**.

### Key Features
- **A\* Search Algorithm**:  
  A well-known pathfinding algorithm that uses a combination of a **cost function** (moves from start) and a **heuristic function** (estimated distance to goal) to efficiently search for a path in grid-based environments.
  
- **Manhattan Distance Heuristic**:  
  The algorithm uses the Manhattan distance as the heuristic for estimating the cost to reach the goal from any given position on the grid. This heuristic is suitable for grid-based movement.

- **Obstacle Handling**:  
  Obstacles are randomly placed on the grid with varying probabilities, making the environment dynamic and more challenging depending on the difficulty level.

- **Dynamic Grid Generation**:  
  The grid is generated dynamically at runtime, with different levels of obstacle density for **easy**, **hard**, and **insane** difficulty modes.

### File Overview
- **astar_motion_planning.py**:
  - `State`: The class that represents each grid state, encapsulating the current position, goal, and grid configuration. It also includes the Manhattan distance calculation and A* priority comparison.
  - `create_grid()`: Dynamically creates a grid of `num_rows` x `num_cols`, with randomly placed obstacles based on a given obstacle probability.
  - `main()`: The core function implementing A* search, which attempts to find a path from the start position to the goal, marking the solution path with `*` on the grid.

### Difficulty Modes
- **Easy Mode**: A smaller grid with fewer obstacles (`8 x 16` grid, `20%` obstacle probability).
- **Hard Mode**: A larger grid with more obstacles (`15 x 30` grid, `30%` obstacle probability).
- **Insane Mode**: The most challenging grid configuration with a high obstacle density (`20 x 60` grid, `35%` obstacle probability).

### Example Run
The A* search starts by creating a randomized grid and attempts to find the optimal path, considering both the current move cost and the heuristic to the goal. The path taken is visually displayed on the grid, using `*` to mark the positions along the solution path.

#### Sample Output
```bash
-----Easy trial 1-----
Grid:
1111111111111111
1              1
1   111111     1
1      1       1
1   1     1    1
1   1  111     1
1              1
1111111111111111

Found goal! :)
Solution Path:
************    1
*    111111*    1
*      1   *    1
*   1     1*    1
*   1  111 *    1
************    1
```

### How to Use
1. Clone the repository.
2. Run the script:
   ```bash
   python astar_motion_planning.py
   ```
3. The grid will be randomly generated for each trial, and the A* search will attempt to find the optimal path.

### Future Improvements
- Extend the algorithm to handle **diagonal movements** and **weighted grids**, adding more complexity to the pathfinding challenge.
- Implement **graphical visualization** of the A* search process in real-time.
- Add **user inputs** for custom grid sizes, obstacle densities, and difficulty modes.
