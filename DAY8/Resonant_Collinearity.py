def create_antinode(grid, antennas):
    """
    Create an antinode from the grid and antennas locations
    Also, create a unique antinode set that includes all unique antinode locations
    """
    antinodes = set()
    unique_antinodes = set()
 
    for positions in antennas.values():
        if len(positions) > 1:
            unique_antinodes.update(positions)

        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx, dy = x2 - x1, y2 - y1

                for nx, ny in [(x1 - dx, y1 - dy), (x2 + dx, y2 + dy)]:
                    if in_bounds(nx, ny, grid): 
                        antinodes.add((nx, ny))
                
                for direction in [(-1, -1), (1, 1)]:
                    add_aligned_antinodes(x1, y1, dx, dy, direction, grid, unique_antinodes)
        
    return antinodes, unique_antinodes


def add_aligned_antinodes(x, y, dx, dy, direction, grid, set):
    """
    Extend antinodes along a specific direction and add them to the antinode set
    """
    nx, ny = x + direction[0] * dx, y + direction[1] * dy
    while in_bounds(nx, ny, grid):
        set.add((nx, ny))
        nx += direction[0] * dx
        ny += direction[1] * dy


def in_bounds(x, y, grid):
    """
    Check if a position (x, y) is within the grid bounds
    """
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def get_antennas_locations(grid):
    """
    Find all unique antenna locations in the grid grouped by frequency
    """
    antennas = {}
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell != ".":
                antennas.setdefault(cell, []).append((x, y))
    return antennas


def parse_input(file):
    """
    Parse the input file into a grid representation
    """
    with open(file, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def main():
    grid = parse_input('map.csv')
    antennas = get_antennas_locations(grid)
    antinodes, unique_antinodes = create_antinode(grid, antennas)
    print(f"Total unique antinode locations: {len(antinodes)}")
    print(f"Total unique antinode locations updated: {len(unique_antinodes)}")

main()
