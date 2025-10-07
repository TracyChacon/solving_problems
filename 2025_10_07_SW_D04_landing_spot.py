# Space Week Day 4: Landing Spot
# In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

# Each spot in the matrix will contain a number from 0-9, inclusive.
# Any 0 represents a potential landing spot.
# Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
# The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
# Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
# Return the indices of the safest landing spot. There will always only be one safest spot.
# For instance, given:

# [
#   [1, 0],
#   [2, 0]
# ]
# Return [0, 1], the indices for the 0 in the first array
def find_landing_spot(matrix: list[list[int]]) -> list[int]:
    DIRECTION_OFFSETS  = [(-1, 0), (1,0), (0, -1), (0, 1)]

    rows_length = len(matrix)
    cols_length = len(matrix[0])
    least_total_danger = float('inf')
    landing_coordinates = []

    for row_idx in range(rows_length):
        for col_idx in range(cols_length):
            if matrix[row_idx][col_idx] == 0:
                current_neighbor_danger = 0
                # Sum all danger values from neigbors of a particular landing spot
                for row_offset, col_offset in DIRECTION_OFFSETS:
                    neighbor_row_idx = row_idx + row_offset
                    neighbor_col_idx = col_idx + col_offset
                    if 0 <= neighbor_row_idx < rows_length and 0 <= neighbor_col_idx < cols_length:
                        current_neighbor_danger += matrix[neighbor_row_idx][neighbor_col_idx]
                # Find least total danger, if lesser danger found, keep coordinates in landing_coordinates variable
                if current_neighbor_danger < least_total_danger:
                    least_total_danger = current_neighbor_danger
                    landing_coordinates = [row_idx, col_idx]
    return landing_coordinates

if __name__ == "__main__":
    # should return [0, 1]
    # print(find_landing_spot([[1, 0], [2,0]]))
    # should return [2, 2]
    print(find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]))
