def handle_zero(remaining, memo):
    """
    Handles the case where the stone is zero
    """
    return split_stones(1, remaining - 1, memo)


def handle_even(stone, remaining, memo):
    """
    Handles the case where the stone has an even number of digits
    """
    stone_str = str(stone)
    mid = len(stone_str) // 2
    s1 = int(stone_str[:mid])
    s2 = int(stone_str[mid:])
    return split_stones(s1, remaining - 1, memo) + split_stones(s2, remaining - 1, memo)


def handle_odd(stone, remaining, memo):
    """
    Handles the case where the stone has an odd number of digits
    """
    return split_stones(stone * 2024, remaining - 1, memo)


def split_stones(stone, remaining, memo={}):
    """
    Recursive function to split stones and calculate the resulting count.
    This is the main driver function that uses helper methods based on conditions.
    """
    if remaining == 0:
        return 1

    key = (stone, remaining)
    if key in memo:
        return memo[key]

    result = 0
    if stone == 0:
        result = handle_zero(remaining, memo)
    elif len(str(stone)) % 2 == 0:
        result = handle_even(stone, remaining, memo)
    else:
        result = handle_odd(stone, remaining, memo)

    memo[key] = result
    return result


def read_file(file):
    """
    Read a file with text and return a list 
    """
    with open(file, 'r') as f:
        return [int(stone) for stone in f.read().split()]


def main():
    stones = read_file("stones.txt")

    count_25 = sum(split_stones(stone, 25) for stone in stones)
    print("Number of stones after 25 iterations:", count_25)

    count_75 = sum(split_stones(stone, 75) for stone in stones)
    print("Number of stones after 75 iterations:", count_75)
    
main()
