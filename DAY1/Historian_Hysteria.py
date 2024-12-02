from collections import Counter

def calculate_distance(left_list, right_list):
    """
    Calculate the total distance between lists
    """
    left_list.sort()
    right_list.sort()
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    return total_distance


def calculate_similarity(left_list, right_list):
    """
    Calculate the similarity score between two lists
    """
    right_counts = Counter(right_list)
    total_similarity = sum(id * right_counts[id] for id in left_list)
    return total_similarity


def read_file(file):
    """
    Read a file with two columns of integers and return two separate lists
    """
    left_list, right_list = [], []
    with open(file, 'r') as f:
        data = [line.split() for line in f]
        left_list = [int(row[0]) for row in data]
        right_list = [int(row[1]) for row in data]
    return left_list, right_list


def main():
    left, right = read_file('./locationID.csv')

    distance = calculate_distance(left, right)
    print("The total distance is", distance)

    similarity = calculate_similarity(left, right)
    print("The total similarity is", similarity)

main()
