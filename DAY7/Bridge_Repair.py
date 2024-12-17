def evaluate_recursively(numbers, target, value=0, index=0, all_operations=False):
    """
    Evaluate the numbers recursively to see if the target can be reached by adding, multiplying, or concatenating the numbers
    """
    if index == len(numbers):
        return value == target

    if index == 0:
        return evaluate_recursively(numbers, target, numbers[index], index + 1, all_operations)
    
    total = (
        evaluate_recursively(numbers, target, add(value, numbers[index]), index + 1, all_operations)
        or evaluate_recursively(numbers, target, multiply(value, numbers[index]), index + 1, all_operations)
    )

    if all_operations:
        total = total or evaluate_recursively(numbers, target, concatenation(value, numbers[index]), index + 1, all_operations)

    return total


def concatenation(a, b):
    return int(str(a) + str(b))


def multiply(a, b):
    return a * b


def add(a, b): 
    return a + b


def parse_input(file):
    """
    Parse the input file into a list of (target, numbers) tuples
    """
    with open(file, 'r') as f:
        return [
            (int(target), list(map(int, numbers.split())))
            for target, numbers in (line.split(':') for line in f)
        ]


def main():
    equations = parse_input('equations.csv')

    final_calibrations = sum(
        target for target, numbers in equations
        if evaluate_recursively(numbers, target)
    )
    print(f"Total calibration result for add & multiply: {final_calibrations}")

    final_calibrations_all = sum(
        target for target, numbers in equations
        if evaluate_recursively(numbers, target, all_operations=True)
    )
    print(f"Total calibration result for all operations: {final_calibrations_all}")

main()
