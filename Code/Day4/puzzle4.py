def read_input(file: str):
    with open(file) as f:
        input = f.read().splitlines()
    
    return input

def solve_part1(input: str) -> int:
    elf_ranges = read_input(input)
    complete_overlap = 0
    for line in elf_ranges:
        ranges = line.split(',')
        # Add one because stop of range is not inclusive
        range1 = range(int(ranges[0].split('-')[0]), int(ranges[0].split('-')[1]) + 1)
        range2 = range(int(ranges[1].split('-')[0]), int(ranges[1].split('-')[1]) + 1)

        # O(1) solution for overlap
        overlap = range(max(range1[0], range2[0]), min(range1[-1], range2[-1])+1)

        if overlap in [range1, range2]:
            complete_overlap += 1
    
    return complete_overlap

def solve_part2(input: str) -> int:
    elf_ranges = read_input(input)
    any_overlap = 0
    for line in elf_ranges:
        ranges = line.split(',')
        # Add one because stop of range is not inclusive
        range1 = range(int(ranges[0].split('-')[0]), int(ranges[0].split('-')[1]) + 1)
        range2 = range(int(ranges[1].split('-')[0]), int(ranges[1].split('-')[1]) + 1)

        # O(1) solution for overlap, produces empty range for no overlap
        overlap = range(max(range1[0], range2[0]), min(range1[-1], range2[-1])+1)

        if len(overlap) > 0:
            any_overlap += 1
    
    return any_overlap

if __name__ == '__main__':
    filename = 'InputFiles\\puzzle4_input.txt'
    print(solve_part1(filename))
    print(solve_part2(filename))
