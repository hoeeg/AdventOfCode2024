DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
current_plot = 0 

def in_bounds(x, y, grid):
    """
    Check if a position (x, y) is within the grid bounds
    """
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def fences(garden, partitions, start):
    """
    Calculate area and perimeter of a region starting from `start`
    """
    global current_plot
    if partitions[start[0]][start[1]]:
        return 0, 0

    current_plot += 1
    current_type = garden[start[0]][start[1]]
    queue = [start]
    area, perimeter = 0, 0

    while queue:
        r, c = queue.pop(0)
        if partitions[r][c]:
            continue

        partitions[r][c] = current_plot
        area += 1
        perimeter += 4 

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc, garden) and garden[nr][nc] == current_type:
                perimeter -= 1 
                queue.append((nr, nc))

    return area, perimeter


def count_external_sides(partitions, part):
    """
    Count external sides of a region identified by `part`
    """
    sum_sides = 0

    for d in [-1, 1]:
        for i in range(len(partitions)):
            horizontal = vertical = False
            for j in range(len(partitions[0])):
                if (not in_bounds(i + d, j, partitions) or partitions[i + d][j] != part) and partitions[i][j] == part:
                    horizontal = True
                elif horizontal:
                    sum_sides += 1
                    horizontal = False

                if (not in_bounds(j, i + d, partitions) or partitions[j][i + d] != part) and partitions[j][i] == part:
                    vertical = True
                elif vertical:
                    sum_sides += 1
                    vertical = False

            sum_sides += horizontal + vertical

    return sum_sides


def find_regions(garden):
    """
    Identify regions, calculate areas, perimeters, and fencing prices
    """
    visited = set()
    regions, partitions = [], [[0] * len(garden[0]) for _ in range(len(garden))]

    for x, plot in enumerate(garden):
        for y, plant in enumerate(plot):
            if (x, y) not in visited:
                area, perimeter = fences(garden, partitions, (x, y))
                sides = count_external_sides(partitions, partitions[x][y])
                regions.append({"plant_type": plant, "area": area, "perimeter": perimeter, "sides": sides})
                
    return regions


def calculate_fencing_price(regions, name):
    """
    Calculate fencing price from region areas and perimeters or sides
    """
    return sum(region["area"] * region[name] for region in regions)


def parse_input(file):
    """
    Parse the input file into a grid representation
    """
    with open(file, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]


def main():
    garden = parse_input("map.csv")
    regions = find_regions(garden)

    price_perimeter = calculate_fencing_price(regions, "perimeter")
    price_sides = calculate_fencing_price(regions, "sides")

    print("Total fencing price using perimeter:", price_perimeter)
    print("Total fencing price using sides:", price_sides)

main()
