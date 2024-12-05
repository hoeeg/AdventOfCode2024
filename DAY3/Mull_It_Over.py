import re

pattern_mul = re.compile(r"mul\((\d+),\s*(\d+)\)")
pattern_do = re.compile(r"do\(\)")
pattern_dont = re.compile(r"don't\(\)")

enabled = True

def parse_instructions(memory):
    """
    Parse the instructions in the corrupted memory and return the results
    """
    total_mul = 0
    total_all = 0

    for line in memory:
        total_mul += process_mul_instructions(line)
        total_all += process_all_instructions(line)
    return total_mul, total_all


def process_mul_instructions(line):
    """
    Find and process all 'mul(X, Y)' instructions in a line.
    """
    total = 0
    for match in pattern_mul.finditer(line):
        X, Y = map(int, match.groups())
        total += mul(X, Y)
    return total


def process_all_instructions(line):
    """
    Scan the corrupted memory for valid 'mul(X, Y)' instructions and compute the total result
    Handle the new 'do()' and 'don't()' instructions to enable/disable 'mul' instructions
    """
    global enabled
    total = 0
    
    for i in range(0, len(line)):
        if pattern_dont.match(line[i:i+7]):
            enabled = False
        elif pattern_do.match(line[i:i+4]):
            enabled = True
        elif enabled and pattern_mul.match(line[i:i+12]):
            total += process_mul_instructions(line[i:i+12])
    return total    


def mul(X, Y):
    """
    Multiply two values and return the result.
    """
    return X * Y


def read_file(file):
    """
    Read a file with text and return a list of strings
    """
    with open(file, 'r') as f:
        return f.read().splitlines()


def main():
    memory = read_file('./memory.txt')
    mul, all = parse_instructions(memory)
    print("The total result of the enabled 'mul' instructions is", mul)
    print("The total result of all 'mul' instructions is", all)

main()
