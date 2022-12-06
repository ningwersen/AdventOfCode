import string

# Lazy way to make dictionary
PRIORITY_DICT = {}
for p, l in enumerate(string.ascii_letters, start=1):
    PRIORITY_DICT[l] = p

def read_input(file: str) -> list[tuple[str, str]]:
    with open(file) as f:
        input = f.read().splitlines()
    
    return input

def solve_part1(input: str) -> int:
    packs = read_input(input)
    split_packs = [[p[:int(len(p) / 2)], p[int(len(p) / 2):]] for p in packs]

    shared = []
    for pack in split_packs:
        overlap = set(pack[0]).intersection(set(pack[1]))
        shared.append(list(overlap)[0])
    
    return sum((PRIORITY_DICT[l] for l in shared))


def solve_part2(input: str) -> int:
    packs = read_input(input)
    badges = []
    for i in range(0, len(packs), 3):
        pack1 = set(packs[i])
        pack2 = set(packs[i+1])
        pack3 = set(packs[i+2])

        overlap = pack1.intersection(pack2).intersection(pack3)
        badges.append(list(overlap)[0])
    
    return sum((PRIORITY_DICT[b] for b in badges))


if __name__ == '__main__':
    filename = 'Day3\\puzzle3_input.txt'
    print(solve_part1(filename))
    print(solve_part2(filename))
