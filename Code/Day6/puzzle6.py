def read_input(file: str):
    with open(file) as f:
        input = f.read().splitlines()
    
    return input

def solve_part1(input: str) -> int:
    stream = read_input(input)[0]

    for i in range(len(stream) - 3):
        if len(set(stream[i:i+4])) == 4:
            return i+4

def solve_part2(input: str) -> int:
    stream = read_input(input)[0]

    for i in range(len(stream) - 13):
        if len(set(stream[i:i+14])) == 14:
            return i+14

if __name__ == '__main__':
    filename = 'InputFiles\\puzzle6_input.txt'
    print(solve_part1(filename))
    print(solve_part2(filename))