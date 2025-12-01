

# UP, LEFT, DOWN, RIGHT
DIRECTIONS : list[list[int]] = [[0, -1], [-1, 0], [1, 0], [0, 1]]

grid : list[list[int]] = [[0 for _ in range(9)] for _ in range(9)]

grid[0][0] = 1
grid[8][8] = 1

line_quantities : list[int] = [6,4,4,3,3,7,1,4,1]
column_quantities : list[int] = [1,6,1,4,3,4,3,4,7]

def backtrack():
    pass

def isMoveValid(grid : list[list[int]], x_next_move : int, y_next_move : int) -> bool :
    """Verify if a move to (x_next_move, y_next_move) is valid.

        Conditions :
        - position must be within grid limits
        - targeted cell is free (value to 0)
        - targeted cell do not touch snake's body other than previous head
        - line and column quantities stay greater than 0 after this move

        Args:
            grid (list[list[int]]): grid showing current state.
            (x_next_move (int), y_next_move (int)) : targeted cell coordinates.

        Returns:
            bool: True if move valid, else False.
        """
    if (x_next_move >= len(grid[0]) or x_next_move < 0 or y_next_move >= len(grid) or y_next_move < 0):
        return False
    if (grid[x_next_move][y_next_move] != 0):
        return False

    neighbourSum = 0
    for x_direction, y_direction in DIRECTIONS:
        if (grid[x_next_move + x_direction][y_next_move + y_direction] != 0):
            neighbourSum += 1
    # 1 neighbour detected means there is only the snake's head around and that it does not touch any other part of the snake besides that
    if (neighbourSum != 1):
        return False

    if (line_quantities[x_next_move] <= 0 or column_quantities[y_next_move] <= 0):
        return False

    return True










if __name__ == "__main__":
    print("This module is not intended to be run directly.")