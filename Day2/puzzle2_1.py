def read_input(file: str) -> list[list[str]]:
    with open(file) as f:
        input = f.read().splitlines()
    
    return [line.split() for line in input]

FIRST_MOVE = [
    'A',
    'B',
    'C'
]

WDL = [
    ['Y', 'X', 'Z'],
    ['Z', 'Y', 'X'],
    ['X', 'Z', 'Y']
]

MOVE_POINTS = [
    'X',
    'Y',
    'Z'
]

def play_rps(p1: str, p2: str):
    p1_index = FIRST_MOVE.index(p1)
    p2_index = WDL[p1_index].index(p2)

    points = 0
    if p2_index == 0:
        points += 6
    elif p2_index == 1:
        points += 3

    points += MOVE_POINTS.index(p2) + 1
    return points

if __name__ == '__main__':
    filename = 'Day2\\puzzle2_input.txt'

    games = read_input(filename)
    total_score = 0
    for game in games:
        total_score += play_rps(game[0], game[1])
    
    print(f'Total score: {total_score}')
