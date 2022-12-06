def read_input(file: str) -> list[list[str]]:
    with open(file) as f:
        input = f.read().splitlines()
    
    return [line.split() for line in input]

FIRST_MOVE = [
    'A',
    'B',
    'C'
]

LDW = [
    ['Z', 'X', 'Y'],
    ['X', 'Y', 'Z'],
    ['Y', 'Z', 'X']
]

MOVE_POINTS = [
    'X',
    'Y',
    'Z'
]

def play_rps(p1: str, outcome: str):
    points = 0

    p1_index = FIRST_MOVE.index(p1)
    ldw_index = MOVE_POINTS.index(outcome)
    p2 = LDW[p1_index][ldw_index]

    if ldw_index == 2:
        points += 6
    elif ldw_index == 1:
        points += 3

    points += MOVE_POINTS.index(p2) + 1
    return points

if __name__ == '__main__':
    filename = 'InputFiles\\puzzle2_input.txt'

    games = read_input(filename)
    total_score = 0
    for game in games:
        total_score += play_rps(game[0], game[1])
    
    print(f'Total score: {total_score}')
