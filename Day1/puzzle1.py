def read_input(file: str):
    with open(file) as f:
        input = f.read().split('\n\n')
    
    return [line.split('\n') for line in input]

def solve_part1(input: str) -> int:
    food = read_input(input)
    total_cals = [sum([int(i) for i in f]) for f in food]
    return max(total_cals)

def solve_part2(input: str) -> int:
    food = read_input(input)
    total_cals = [sum([int(i) for i in f]) for f in food]
    top_3 = sorted(total_cals, reverse=True)[:3]

    return sum(top_3)

if __name__ == '__main__':
    filename = 'Day1\\puzzle1_input.txt'
    print(solve_part1(filename))
    print(solve_part2(filename))
