# Game of Life

# Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

#     Each cell is either 1 (alive) or 0 (dead).
#     A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
#     Cells on the edges have fewer than eight neighbors.

# Rules for updating each cell:

#     Any live cell with fewer than two live neighbors dies (underpopulation).
#     Any live cell with two or three live neighbors lives on.
#     Any live cell with more than three live neighbors dies (overpopulation).
#     Any dead cell with exactly three live neighbors becomes alive (reproduction).

# For example, given:

# [
#   [0, 1, 0],
#   [0, 1, 1],
#   [1, 1, 0]
# ]

# return:

# [
#   [0, 1, 1],
#   [0, 0, 1],
#   [1, 1, 1]
# ]

# Each cell updates according to the number of live neighbors. For instance, [0][0] stays dead (2 live neighbors), [0][1] stays alive (2 live neighbors), [0][2] dies (3 live neighbors), and so on.

######################################################################
# Initial Solution
######################################################################

def check_inbounds(grid: list[list], i: int, j: int) -> int:
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        return grid[i][j]
    return 0

def life_status(cell: int, total_live_neighbors: int) -> int:
    if cell == 0 and total_live_neighbors == 3:
        return 1
    elif cell == 1 and  2 > total_live_neighbors or total_live_neighbors > 3:
        return 0
    return cell

def game_of_life(grid: list[list]) -> list[list[int]]:
    grid_width = len(grid[0])
    grid_height = len(grid)
    next_state_grid = [row[:] for row in grid]
    
    for i in range(grid_height):
        for j in range(grid_width):
            neighbors  = [
                # north
                check_inbounds(grid, i - 1, j),
                # north_east
                check_inbounds(grid, i - 1, j + 1),
                # east
                check_inbounds(grid, i, j + 1),
                # south_east
                check_inbounds(grid, i + 1, j + 1),
                # south
                check_inbounds(grid, i + 1, j),
                # south_west
                check_inbounds(grid, i + 1, j - 1),
                # west
                check_inbounds(grid, i, j - 1),
                # north_west
                check_inbounds(grid, i - 1, j - 1)
            ]

            cell = grid[i][j]
            total_live_neighbors = sum(neighbors)
            next_state_grid[i][j] = life_status(cell, total_live_neighbors)

    return next_state_grid

######################################################################
# Refactered Solution
######################################################################

# def game_of_life(grid: list[list[int]]) -> list[list[int]]:
#     if not grid: return []
    
#     rows, cols = len(grid), len(grid[0])
#     # Create a blank grid for the next state
#     next_state = [[0 for _ in range(cols)] for _ in range(rows)]
    
#     for r in range(rows):
#         for c in range(cols):
#             # Calculate live neighbors using offsets
#             live_neighbors = 0
#             for dr in [-1, 0, 1]:
#                 for dc in [-1, 0, 1]:
#                     if dr == 0 and dc == 0:
#                         continue
                    
#                     nr, nc = r + dr, c + dc
#                     if 0 <= nr < rows and 0 <= nc < cols:
#                         live_neighbors += grid[nr][nc]
            
#             # Apply Rules
#             if grid[r][c] == 1:
#                 if 2 <= live_neighbors <= 3:
#                     next_state[r][c] = 1
#             else:
#                 if live_neighbors == 3:
#                     next_state[r][c] = 1
                    
#     return next_state


if __name__ == '__main__':
    # Tests

    # Test 1 should return [[0, 1, 1], [0, 0, 1], [1, 1, 1]].
    print(game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]))
    # Test 2 should return [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]].
    print(game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]))
    # Test 3 should return [[0, 0, 0], [0, 1, 0], [0, 0, 0]].
    print(game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    # Test 4 should return [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]].
    print(game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]))