
class SnakeBacktrack:

    def __init__(self, starting_point : tuple[int, int]) -> None:
        # UP, DOWN, LEFT, RIGHT
        self.DIRECTIONS : list[list[int]] = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Initialize a 9x9 grid with all cells set to 0
        self.grid : list[list[int]] = [[0 for _ in range(9)] for _ in range(9)]

        # Starting and ending points of the snake
        self.starting_point : tuple[int, int] = starting_point
        self.ending_point : tuple[int, int] = (len(self.grid[0]) - 1, len(self.grid) - 1)

        # Quantity of cells to fill in each column and row
        self.col_quantities : list[int] = [6, 4, 4, 3, 3, 7, 1, 4, 1]
        self.row_quantities : list[int] = [1, 6, 1, 4, 3, 4, 3, 4, 7]
        self.nodes_count : int = 0
        self.max_depth : int = 1


    def calculate_manhattan_distance_heuristic(self, row, col, target_row, target_col):
        """Calculate heuristic score for a given position."""
        score = 0

        # 1. Constraints (weight 3 because constraints are the most important)
        score += 3 * (self.row_quantities[row] + self.col_quantities[col])

        # 2. Manhattan distance (poids -1)
        manhattan = abs(row - target_row) + abs(col - target_col)
        score -= manhattan

        # 3. Free neighbour degree, used to choose first nodes that have lot of free space to not be trapped (weight 2)
        free_neighbors = self.free_neighbor_count(row, col)
        score += 2 * free_neighbors

        return score


    def backtrack(self, row: int, col: int) -> bool:

        self.nodes_count += 1
        if not self.is_move_valid(row, col):
            return False

        self.row_quantities[row] -= 1
        self.col_quantities[col] -= 1
        self.grid[row][col] = 1

        if self.is_finished(row, col):
            self.output()
            return True

        # Calculate scores for all valid directions
        scored_directions = []
        for dx, dy in self.DIRECTIONS:
            next_row, next_col = row + dx, col + dy
            if not self.is_out_of_grid(next_row, next_col) and self.grid[next_row][next_col] == 0:
                score = self.calculate_manhattan_distance_heuristic(next_row, next_col,
                                                               self.ending_point[0], self.ending_point[1])
                scored_directions.append((score, dx, dy))

        scored_directions.sort(reverse=True, key=lambda x: x[0])

        for _, dx, dy in scored_directions:
            next_x, next_y = row + dx, col + dy
            if self.backtrack(next_x, next_y):
                self.max_depth += 1
                return True

        self.grid[row][col] = 0
        self.row_quantities[row] += 1
        self.col_quantities[col] += 1
        return False



    def is_finished(self, row, col) -> bool:
        """Check if the current state is a finished solution.
        Args:
            row (int): current row of the snake's head.
            col (int): current column of the snake's head.
        Returns:
            bool
        """
        if row != self.ending_point[0] or col != self.ending_point[1]:
            return False

        for row_quantity in self.row_quantities:
            if row_quantity != 0:
                return False
        for col_quantity in self.col_quantities:
            if col_quantity != 0:
                return False

        return True



    def output(self) -> None:
        """Displays grid : '■' for 1 else '•'.

        Returns:
            None
        """
        for row in self.grid:
            print(' '.join('■' if cell == 1 else '•' for cell in row))



    def is_move_valid(self, row_next_move : int, col_next_move : int) -> bool :
        """Verify if a move to (row_next_move, col_next_move) is valid.

        Conditions :
        - position must be within grid limits
        - targeted cell is free (value to 0)
        - targeted cell do not touch snake's body other than previous head
        - line and column quantities stay greater than 0 after this move

        Args:
            row_next_move (int)  targeted cell row.
            col_next_move (int) : targeted cell col.

        Returns:
            bool: True if move valid, else False.
        """
        if self.is_out_of_grid(row_next_move, col_next_move):
            return False

        if self.grid[row_next_move][col_next_move] != 0:
            return False

        if self.row_quantities[row_next_move] <= 0 or self.col_quantities[col_next_move] <= 0:
            return False

        if row_next_move == self.starting_point[0] and col_next_move == self.starting_point[1]:
            return True

        if row_next_move == self.ending_point[0] and col_next_move == self.ending_point[1]:
            return True

        # 1 neighbour detected means there is only the snake's head around and that it does not touch any other part of the snake besides that
        return self.free_neighbor_count(row_next_move, col_next_move) >= 2


    def is_out_of_grid(self, row : int, col : int) -> bool:
        """Check if the given position is out of grid bounds.
        Args:
            row (int): row index to check.
            col (int): column index to check.
        Returns:
            bool: True if out of bounds, else False.
        """
        return row >= len(self.grid[0]) or row < 0 or col >= len(self.grid) or col < 0

    def free_neighbor_count(self, row, col):
        """Count free neighbors of a cell."""
        count = 0
        for dr, dc in self.DIRECTIONS:
            nr, nc = row + dr, col + dc
            if not self.is_out_of_grid(nr, nc) and self.grid[nr][nc] == 0:
                count += 1
        return count


# Main execution
if __name__ == "__main__":
    starting_point: tuple[int, int] = (0, 0)
    snake_backtrack = SnakeBacktrack(starting_point)
    result = snake_backtrack.backtrack(starting_point[0], starting_point[1])

    print(f"Solution found depth: {snake_backtrack.max_depth}")
    print(f"Node count:{snake_backtrack.nodes_count} ")