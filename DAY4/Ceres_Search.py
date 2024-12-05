DIRECTIONS = [
    (0, 1), 
    (0, -1), 
    (1, 0),  
    (-1, 0), 
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1),
]

def word_search(word, grid):
    """
    Search for a word in a 2D grid and count all occurrences in all directions
    """
    rows = len(grid)
    cols = len(grid[0])
    length = len(word) - 1 
    occurrences = 0

    for x in range(rows):
        for y in range(cols):
            for dx, dy in DIRECTIONS:
                if not (0 <= x + length * dx < rows and 0 <= y + length * dy < cols):
                    continue
                occurrences += count_in_direction(word, grid, x, y, dx, dy)
    return occurrences


def count_in_direction(word, grid, x, y, dx, dy):
    """
    Count occurrences of the word starting from (x, y) in direction (dx, dy)
    """
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if grid[nx][ny] != word[i]:
            return 0
    return 1


def x_mas_search(grid):
    """
    Search for the X-MAS pattern in the grid and count all occurrences
    """
    rows = len(grid)
    cols = len(grid[0])
    total_count = 0

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if grid[x][y] == "A" and check_x_shape(x, y, grid):
                total_count += 1
    return total_count


def check_x_shape(x, y, grid):
    """
    Check if the X-MAS pattern is present in the grid starting from (x, y)
    """
    return (
        (grid[x - 1][y - 1] in "MS" and grid[x + 1][y + 1] in "MS" and grid[x - 1][y - 1] != grid[x + 1][y + 1])
        and (grid[x - 1][y + 1] in "MS" and grid[x + 1][y - 1] in "MS" and grid[x - 1][y + 1] != grid[x + 1][y - 1])
    )
  

def read_file(file):
    """
    Read a file with text and return a list of strings
    """
    with open(file, 'r') as f:
        return f.read().splitlines()


def main():
    text = read_file('./puzzle_input.txt')

    word = "XMAS"
    apperences = word_search(word, text)
    print(f"The word '{word}' appears {apperences} times in the text")

    apperences_x = x_mas_search(text)
    print(f"The X-MAS pattern appears {apperences_x} times in the text")

main()
