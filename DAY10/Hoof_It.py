def find_trailheads(map):
    """
    Find all trailheads in the map
    """
    trailheads = []
    for r, row in enumerate(map):
        for c, height in enumerate(row):
            if height == 0:
                trailheads.append((r, c))
    return trailheads


def bfs_trailhead_score(map, start):
    """
    Perform a breadth-first search from a trailhead to find the number of reachable nines
    """
    queue = [start]
    visited = set([start])
    count = 0

    while queue:
        r, c = queue.pop(0)
        current_height = map[r][c]
        neighbors = get_neighbors(r, c, map)

        for nr, nc in neighbors:
            neighbor_height = map[nr][nc]
            if is_valid_step(current_height, neighbor_height, visited, nr, nc):
                visited.add((nr, nc))
                queue.append((nr, nc))
                if neighbor_height == 9:
                    count += 1

    return count


def bfs_trailhead_rating(map, start):
    """
    Perform a breadth-first search from a trailhead to count the number of distinct hiking trails
    """
    queue = [(start, set())]
    trail_count = 0

    while queue:
        (r, c), visited = queue.pop(0)
        current_height = map[r][c]

        if current_height == 9:
            trail_count += 1
            continue

        neighbors = get_neighbors(r, c, map)
        for nr, nc in neighbors:
            neighbor_height = map[nr][nc]
            if is_valid_step(current_height, neighbor_height, visited, nr, nc):
                new_visited = visited | {(nr, nc)}
                queue.append(((nr, nc), new_visited))

    return trail_count


def get_neighbors(r, c, map):
    """
    Get all valid neighboring coordinates for a given cell
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(r + dr, c + dc) for dr, dc in directions if in_bounds(r + dr, c + dc, map)]


def is_valid_step(current_height, neighbor_height, visited, nr, nc):
    """
    Check if the step to a neighboring cell is valid
    """
    return neighbor_height == current_height + 1 and (nr, nc) not in visited


def in_bounds(x, y, grid):
    """
    Check if a position (x, y) is within the grid bounds
    """
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def parse_input(file): 
    """
    Parse the input file into a map representation
    """
    with open(file, 'r') as f:
        return [list(map(int, line)) for line in f.read().strip().split('\n')]


def main():
    map = parse_input("map.csv")
    trailheads = find_trailheads(map)

    scores = sum(bfs_trailhead_score(map, th) for th in trailheads)
    print("Sum of scores for all trailheads:", scores)
    
    ratings = sum(bfs_trailhead_rating(map, th) for th in trailheads)
    print("Sum of ratings for all trailheads:", ratings)

main()
