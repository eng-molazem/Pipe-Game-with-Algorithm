# Pipe Game

**Pipe Game** is a 2D puzzle game built with Python where the player connects pipe pieces to create a continuous path for water flow.

The goal is to rotate and place pipe tiles correctly so that all pipes are connected and water can move through the entire system.

---

## Gameplay
-Rotate pipe pieces to connect them correctly.
-Build a complete path for water to flow.
-Solve multiple puzzle levels.
-Each level introduces a new pipe layout to solve.
-Skip and solve any level automatically by pressing the N key — the game uses search algorithms to find the solution.


### Game Challenge

- Pipes come in different shapes
- Some pipes may already be fixed
- You must find the correct orientation to complete the path

---

## Features

- Puzzle-based gameplay
- Multiple pipe types:
  - Straight pipes
  - Elbow pipes
  - Tee pipes
  - Cross pipes
- Multiple levels to solve
- Visual pipe connection system
- Simple and clean game interface
- Automatic level solving with the N key using search algorithms.
---

## Project Structure

```
Pipe_Game/
│
├── pipe_game.py      # Main game file
├── Lvl1.txt          # Level 1 data
├── Lvl2.txt          # Level 2 data
├── Lvl3.txt          # Level 3 data
│
└── assets/           # Game images
    ├── straight_empty.png
    ├── straight_full.png
    ├── elbow_empty.png
    ├── elbow_full.png
    ├── tee_empty.png
    ├── tee_full.png
    ├── cross_empty.png
    ├── cross_full.png
    └── stone.png
```

---

## Requirements

- Python 3
- Pygame

### Install the dependency

```bash
pip install pygame
```

---

## Running the Game

```bash
python pipe_game.py
```

---

## Goal

Rotate and place the pipe pieces so that all pipes connect correctly and create a continuous flow path.

Complete each level manually by solving the pipe puzzle, or press N to solve any level automatically using search algorithms.

---

## License

This project is open source and free to use under the MIT License.
ترجمها
