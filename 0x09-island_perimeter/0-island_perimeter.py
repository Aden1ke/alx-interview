#!/usr/bin/python3
def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four sides
                # Up
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Down
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter