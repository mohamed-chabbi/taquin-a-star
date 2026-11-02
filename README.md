# Taquin – 8 Puzzle Solver with A*

A Python implementation of the **8-puzzle (Taquin)** using the **A* search algorithm**, with a graphical interface built using Tkinter.

## Features

- Interactive 3×3 puzzle board.
- Manual tile movement with click controls.
- Random solvable board generation.
- A* search algorithm to find an optimal solution.
- Two heuristic functions:
  - **Misplaced Tiles:** Counts tiles that are not in their goal positions.
  - **Manhattan Distance:** Calculates the total horizontal and vertical distance of each tile from its goal position.
- Exploration log displaying the `g`, `h`, and `f` scores of explored states.
- Animated solution playback.

## A* Algorithm

The solver uses the evaluation function:

\[
f(n) = g(n) + h(n)
\]

Where:
- `g(n)`: Actual cost from the initial state to the current state.
- `h(n)`: Estimated cost from the current state to the goal.
- `f(n)`: Estimated total cost of the solution through the current state.

## Project Structure

```text
taquin-a-star/
├── taquin_logic.py   # Puzzle logic, heuristics and A* algorithm
├── taquin_gui.py     # Tkinter graphical interface
└── README.md
```

## Requirements

- Python 3
- Tkinter

## Run the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/taquin-a-star.git
cd taquin-a-star
```

Run the application:

```bash
python taquin_gui.py
```

## How to Use

1. Click **Shuffle** to generate a solvable puzzle.
2. Move tiles manually by clicking an adjacent tile.
3. Click **Solve with A*** to find and visualize the solution.
4. Check the exploration log to follow the algorithm's progress and scores.

## Academic Context

Developed as part of the **Artificial Intelligence Fundamentals** course project at USTHB (Université des Sciences et de la Technologie Houari Boumediene).

**Topic:** State-Space Search – A* Algorithm.
