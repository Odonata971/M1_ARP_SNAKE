

# UP, DOWN, LEFT, RIGHT
DIRECTIONS : list[list[int]] = [[-1, 0], [1, 0], [0, -1], [0, 1]]

grid : list[list[int]] = [[0 for _ in range(9)] for _ in range(9)]

startingPoint: tuple[int, int] = (0,0)
endingPoint : tuple[int, int] = (len(grid[0])- 1, len(grid)- 1)

col_quantities : list[int] = [6, 4, 4, 3, 3, 7, 1, 4, 1]
row_quantities : list[int] = [1, 6, 1, 4, 3, 4, 3, 4, 7]



def backtrack(grid, row : int, col : int) -> bool:
    if not is_move_valid(grid, row, col):
        return False

    row_quantities[row] -= 1
    col_quantities[col] -= 1
    grid[row][col] = 1

    if is_finished(row, col):
        output(grid)
        return True

    for dx, dy in DIRECTIONS:
        next_x, next_y = row + dx, col + dy
        if backtrack(grid, next_x, next_y):
            return True

    grid[row][col] = 0
    row_quantities[row] += 1
    col_quantities[col] += 1
    return False  # No solution in this branch



def is_finished(row, col) -> bool:
    if row != endingPoint[0] or col != endingPoint[1]:
        return False

    for row_quantity in row_quantities:
        if row_quantity != 0:
            return False
    for col_quantity in col_quantities:
        if col_quantity != 0:
            return False

    return True



def output(grid : list[list[int]]) -> None:
    print('\n'.join(', '.join(str(cell) for cell in row) for row in grid))



def is_move_valid(grid : list[list[int]], row_next_move : int, col_next_move : int) -> bool :
    """Verify if a move to (row_next_move, col_next_move) is valid.

        Conditions :
        - position must be within grid limits
        - targeted cell is free (value to 0)
        - targeted cell do not touch snake's body other than previous head
        - line and column quantities stay greater than 0 after this move

        Args:
            grid (list[list[int]]): grid showing current state.
            row_next_move (int)  targeted cell row.
            col_next_move (int) : targeted cell col.

        Returns:
            bool: True if move valid, else False.
        """
    if is_out_of_grid(row_next_move, col_next_move):
        return False

    if grid[row_next_move][col_next_move] != 0:
        return False

    if row_quantities[row_next_move] <= 0 or col_quantities[col_next_move] <= 0:
        return False

    if row_next_move == startingPoint[0] and col_next_move == startingPoint[1]:
        return True

    if row_next_move == endingPoint[0] and col_next_move == endingPoint[1]:
        return True

    neighbour_sum : int = 0
    for x_direction, y_direction in DIRECTIONS:
        if is_out_of_grid(row_next_move + x_direction, col_next_move + y_direction):
            continue
        if grid[row_next_move + x_direction][col_next_move + y_direction] != 0:
            neighbour_sum += 1
    # 1 neighbour detected means there is only the snake's head around and that it does not touch any other part of the snake besides that
    return neighbour_sum == 1



def is_out_of_grid(row : int, col : int) -> bool:
    return row >= len(grid[0]) or row < 0 or col >= len(grid) or col < 0



if __name__ == "__main__":
    result = backtrack(grid, 0, 0)
    print(f"Solution found: ")