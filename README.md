# A*-Problem

This code visualizes the A* pathfinding algorithm on a 2D grid using **Tkinter** for GUI.  
It supports **8-directional movement** (up, down, left, right, and diagonals) with different movement costs:
- Orthogonal moves (up/down/left/right): **cost = 1**
- Diagonal moves: **cost = 1.5**

Blocked cells (rivers) are represented by `0`, and traversable land is represented by `1`.
Features
- **Interactive input** for grid size, terrain, start, and goal.
- **Real-time path visualization** using Tkinter.
- Diagonal movement supported with slightly higher cost.
- Visual cues:
  - **Blue**: Obstacles (rivers)
  - **White**: Land (walkable)
  - **Green**: Final path
  - **Yellow**: Start point
  - **Red**: Goal point

Time Complexity ≈ O(n × m log(n × m))
Space Complexity ≈ O(n × m)

