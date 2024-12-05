def parse_manual(rules, updates):
    """
    Parse the rules and updates and return the sum of middle page numbers for correct and incorrect updates
    """
    all_rules = [tuple(map(int, rule.split('|'))) for rule in rules]
    graph = build_graph(all_rules)

    correct_sum = 0
    incorrect_sum = 0

    for update in updates:
        pages = list(map(int, update.split(',')))
        if validate_update(all_rules, pages):
            correct_sum += find_middle(pages) 
        else:
            reordered = topological_sort(graph, pages)
            incorrect_sum += find_middle(reordered)
    return correct_sum, incorrect_sum


def validate_update(rules, update):
    """
    Check if a given update satisfies the ordering rules
    """
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def find_middle(update):
    """
    Find the middle page number of a valid update
    """
    return update[len(update) // 2]


def build_graph(rules):
    """
    Build a graph from the given rules
    """
    graph = {}
    for x, y in rules:
        graph.setdefault(x, []).append(y)
    return graph


def build_subgraph(graph, pages):
    """
    Build a subgraph from the given graph and pages
    """
    subgraph = {page: [] for page in pages}
    degrees = {page: 0 for page in pages}

    for page in pages:
        for neighbor in graph.get(page, []):
            if neighbor in pages:
                subgraph[page].append(neighbor)
                degrees[neighbor] += 1
    return subgraph, degrees


def topological_sort(graph, pages):
    """
    Perform topological sort on the given graph and pages
    """
    subgraph, degree = build_subgraph(graph, pages)
    stack = [node for node in pages if degree[node] == 0]
    result = []

    while stack:
        node = stack.pop()
        result.append(node)
        for neighbor in subgraph[node]:
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                stack.append(neighbor)
    return result


def read_file(file):
    """
    Read a file and split it into rules and updates based on a blank line
    """
    with open(file, 'r') as f:
        lines = f.read().splitlines()
    blank = lines.index('')
    return lines[:blank], lines[blank + 1:]


def main():
    rules, updates = read_file('./manual.txt')
    correct_sum, incorrect_sum = parse_manual(rules, updates)

    print("Sum of middle page numbers for correctly ordered updates are", correct_sum)
    print("Sum of middle page numbers for incorrectly ordered updates are", incorrect_sum)

main()
