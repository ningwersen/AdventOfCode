def read_input(file: str):
    with open(file) as f:
        input = f.read().splitlines()
    
    return input

def solve_part1(input: str) -> int:
    pass

def solve_part2(input: str) -> int:
    pass

if __name__ == '__main__':
    filename = 'Dayx\\puzzlex_test.txt'
    print(solve_part1(filename))
    print(solve_part2(filename))