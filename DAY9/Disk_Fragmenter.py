def parse_disk_map(disk):
    """
    Parse the disk map into a list of blocks with file IDs and free spaces
    """
    blocks = []
    file_id = 0
    is_file = True

    for size in map(int, disk):
        if is_file:
            blocks.extend([file_id] * size)
            file_id += 1
        else:
            blocks.extend(["."] * size)
        is_file = not is_file
        
    return blocks


def find_free_spans(blocks):
    """
    Find spans of contiguous free spaces in the disk
    """
    spans = []
    start = None

    for i, block in enumerate(blocks):
        if block == ".":
            if start is None:
                start = i
        elif start is not None:
            spans.append((start, i - 1))
            start = None

    if start is not None:
        spans.append((start, len(blocks) - 1))

    return spans


def compact_disk(blocks):
    """
    Move file blocks to the leftmost free space until all files are compacted
    """
    for i in range(len(blocks) - 1, -1, -1):
        if blocks[i] == ".":
            continue
        for j in range(i):
            if blocks[j] == ".":
                blocks[j], blocks[i] = blocks[i], "."
                break
    return blocks


def compact_whole_disk(blocks):
    """
    Compact the disk by moving whole files to the leftmost suitable span of free space
    """
    file_ids = sorted(set(block for block in blocks if block != "."), reverse=True)

    for file_id in file_ids:
        file_indices = [i for i, block in enumerate(blocks) if block == file_id]
        if not file_indices:
            continue

        file_size = len(file_indices)
        spans = find_free_spans(blocks)
        
        for span_start, span_end in spans:
            span_size = span_end - span_start + 1
            if span_size >= file_size and span_start <= file_indices[0]:
                for i in range(file_size):
                    blocks[span_start + i] = file_id
                for i in range(file_indices[0], file_indices[-1] + 1):
                    blocks[i] = "."
                break

    return blocks


def calculate_checksum(blocks):
    """
    Calculate the checksum based on the final disk layout
    """
    return sum(position * block for position, block in enumerate(blocks) if block != ".")


def read_file(file):
    """
    Read a file
    """
    with open(file, 'r') as f:
        return f.read().strip()

    
def main():
    disk_map = read_file("disk_map.csv")

    blocks = parse_disk_map(disk_map)
    compacted_blocks = compact_disk(blocks)
    checksum = calculate_checksum(compacted_blocks)
    print("Filesystem checksum for individual blocks:", checksum)

    blocks = parse_disk_map(disk_map)
    compacted_whole = compact_whole_disk(blocks)
    checksum_whole = calculate_checksum(compacted_whole)
    print("Filesystem checksum for whole files:", checksum_whole)

main()
