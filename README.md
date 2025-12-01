# Snake ARP M1

A logic puzzle solver implementing the Snake (also known as Tunnel) puzzle using backtracking search algorithms.

## Table of Contents
- [About the Puzzle](#about-the-puzzle)
- [Problem Formalization](#problem-formalization)
- [Algorithm](#algorithm)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## About the Puzzle

Snake is a logic puzzle played on a rectangular or square grid where:
- Two cells are marked as start and end points
- The goal is to draw a single continuous line (the "snake") between these marked cells
- The snake never touches itself, not even diagonally
- Numbers outside the grid indicate how many cells must be filled in each corresponding row or column

**Reference:** [Cross+A Puzzles - Snake](https://www.cross-plus-a.com/puzzles.htm#Snake)

## Problem Formalization

### Initial State
- A 9×9 grid with two marked cells representing the head (start) and tail (end) of the snake

### Actions
The snake can move in four directions:
- Left
- Right
- Up
- Down

### Successor Function
A valid successor state must satisfy the following constraints:
- The new position is within the grid boundaries
- The new position is not already part of the snake
- The move does not cause the snake to touch itself (even diagonally)
- The move does not violate numerical constraints (remaining row/column counts ≥ 0)

Each valid action generates a new state with:
- An updated grid
- A new head position

### Goal State
A solution is found when:
- The snake's head reaches the ending cell
- All numerical constraints are satisfied (remaining counts = 0 for all rows and columns)

### Cost Function
The cost is set to 0, as the objective is to find any valid solution path rather than optimize for path length or efficiency.

## Algorithm

This project implements a **Backtracking** algorithm to solve Snake puzzles.

Backtracking is a depth-first search algorithm that:
1. Explores possible paths by making incremental moves
2. Abandons paths that violate constraints (backtracks)
3. Continues until a valid solution is found or all possibilities are exhausted

**Reference:** [Wikipedia - Backtracking](https://en.wikipedia.org/wiki/Backtracking)
