def check_if_safe(levels):
    """
    Check if a report is safe by the following conditions:
    - The levels are either all increasing or all decreasing
    - Any two adjacent levels differ by at least one and at most three
    """ 
    if levels == sorted(levels) or levels == sorted(levels, reverse=True):
            return all(1 <= abs(left - right) <= 3 for left, right in zip(levels, levels[1:]))
    return False


def safe_if_removed(levels):
    """
    Check if removing a single level from an unsafe report makes it safe
    """ 
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if check_if_safe(modified_levels):
            return True
    return False


def read_file(file):
    """
    Read a file with multiple columns and return a list of lists
    """
    with open(file, 'r') as f:
        return [list(map(int, line.split())) for line in f]
        

def main():
    data = read_file('./reports.csv')
    safe_reports = sum(
        check_if_safe(report) or safe_if_removed(report)
        for report in data
    )
    print("The number of safe reports is", safe_reports)

main()
