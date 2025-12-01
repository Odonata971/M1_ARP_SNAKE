

grid = [[0 for _ in range(9)] for _ in range(9)]

grid[0][0] = 1
grid[8][8] = 1

line_quantities = [6,4,4,3,3,7,1,4,1]
column_quantities = [1,6,1,4,3,4,3,4,7]

def backtrack():
    pass

def isMovementValid(grid, x_next_move : int, y_next_move : int) -> bool :
    if (x_next_move >= len(grid[0]) or x_next_move < 0 or y_next_move >= len(grid) or y_next_move < 0):
        return False
    if (grid[x_next_move][y_next_move] != 0):
        return False
    if ():
        """TODO si somme de tous les cases adjacentes == 1, alors on touche seulement la tete, sinon mouv illégal"""

    return True










if __name__ == "__main__":
    print("This module is not intended to be run directly.")