from itertools import cycle

def find_obstructions(grid, guard):
    """
    Find all the possible obstructions that can be placed in the grid
    """
    obstructions = []
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == "." and (x, y) != guard:
                grid[x][y] = "#" 
                if check_loop(grid, guard):
                    obstructions.append((x, y))
                grid[x][y] = "." 

    return obstructions


def check_loop(grid, current, obstacle=(-1, -1)):
    """
    Check if the guard will loop back to the same position after placing an obstacle
    """
    directions = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
    cur_dir = next(directions) 
    visited = {(current, cur_dir)}

    while True:
        nx, ny = (current[0] + cur_dir[0], current[1] + cur_dir[1])

        if not in_bounds(nx, ny, grid):
            return False
        elif grid[nx][ny] == "#" or (nx, ny) == obstacle:
            cur_dir = next(directions)
        else:
            current = (nx, ny) 

        if (current, cur_dir) in visited:
            return True

        visited.add((current, cur_dir))



def predict_guard(grid, guard):
    """
    Predict the guard's path in the grid starting from the guard's position
    """
    x, y = guard
    path = set()
    dx, dy = -1, 0

    while True:
        path.add((x, y))
        grid[x][y] = "X"

        nx, ny = x + dx, y + dy
        if not in_bounds(nx, ny, grid):
            break

        if grid[nx][ny] == "#":  
            dx, dy = dy, -dx
        elif grid[nx][ny] in {".", "X"}: 
            x, y = nx, ny

    return path


def find_guard(grid):
    """
    Find the guard's starting position in the grid
    """
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == "^":
                return (x, y)


def in_bounds(x, y, grid):
    """
    Check if a position (x, y) is within the grid bounds
    """
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def read_file(file):
    """
    Read a file with text and return a list of lists of characters
    """
    with open(file, 'r') as f:
        return [list(line) for line in f.read().splitlines()]


def main():
    grid = read_file("map.txt")
    guard = find_guard(grid)
    
    # path = predict_guard(grid, guard)
    # print(f"Number of unique positions visited: {len(path)}")

    obstacles = find_obstructions(grid, guard)
    print(f"Number of obstacles placed: {len(obstacles)}")

main()
