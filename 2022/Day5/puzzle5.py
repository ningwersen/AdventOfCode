import math

# Make things easier
class Command():
    def __init__(self, amt: int, start: int, end: int) -> None:
        self.amt = amt
        self.start = start
        self.end = end

def read_input(file: str) -> tuple:
    with open(file) as f:
        input = f.read().split('\n\n')
    
    initial_config = input[0].splitlines()

    # Initalize empty lists
    num_stacks = math.floor((len(initial_config[0]) + 1) / 4)
    stacks: list[list[str]] = [[] for _ in range(num_stacks)]

    for line in initial_config[:-1]:
        # Easier to grab the index of each letter since they are multiples of 4
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                index = math.floor((i - 1) / 4)
                stacks[index].append(line[i])
    
    # Reverse stacks for LIFO operations
    [s.reverse() for s in stacks]
    
    commands = []
    command_text = input[1].splitlines()
    for line in command_text:
        sections = line.split()
        # User 0 based index
        commands.append(Command(int(sections[1]), int(sections[3]) - 1, int(sections[5]) - 1))

    return (stacks, commands)

def solve_part1(input: str) -> str:
    stacks, commands = read_input(input)

    for command in commands:
        for _ in range(command.amt):
            # Slices would be quicker here, but I prefer the logic of pop
            stacks[command.end].append(stacks[command.start].pop())
    
    message = ''
    for stack in stacks:
        message += stack[-1]
    
    return message

def solve_part2(input: str) -> int:
    stacks, commands = read_input(input)

    for command in commands:
        # Slices to preserve order
        stacks[command.end].extend(stacks[command.start][-command.amt:])
        stacks[command.start] = stacks[command.start][:-command.amt]
    
    message = ''
    for stack in stacks:
        message += stack[-1]
    
    return message

if __name__ == '__main__':
    filename = 'InputFiles\\puzzle5_input.txt'
    print(solve_part1(filename))
    print(solve_part2(filename))