import timeit
import math


def read_input(file: str):
    with open(file) as f:
        input = f.read().split('\n\n')

    return input


def get_workflows(text: list[str]) -> dict:
    workflows = dict()
    for line in text:
        open_bracket = line.index('{')
        name = line[:open_bracket]
        rules = line[open_bracket+1:-1]
        workflows[name] = rules.split(',')

    return workflows


def get_parts(text: list[str]) -> list[dict]:
    parts = []
    for line in text:
        part = dict()
        for value in line[1:-1].split(','):
            category, rating = value.split('=')
            part[category] = int(rating)

        parts.append(part)

    return parts


def evaluate_inequality(inequality: str, part: dict) -> bool:
    category = inequality[0]
    operation = inequality[1]
    value = int(inequality[2:])

    if operation == '<':
        return part[category] < value
    elif operation == '>':
        return part[category] > value
    else:
        raise ValueError(
            f'Invalid operation "{operation}" for inequality: {inequality}')


def part_accepted(part: dict, workflows: dict) -> bool:
    current_workflow = 'in'

    while current_workflow not in ('A', 'R'):
        for test in workflows[current_workflow]:
            if ':' in test:
                inequality, next_workflow = test.split(':')
                if evaluate_inequality(inequality, part) == True:
                    current_workflow = next_workflow
                    break
            else:
                current_workflow = test

    return current_workflow == 'A'


def get_rating(part: dict) -> int:
    return sum(part.values())


def get_valid_ranges(rule: str) -> range:
    operation = rule[1]
    value = int(rule[2:])

    if operation == '<':
        valid_ranges = range(1, value)
    elif operation == '>':
        valid_ranges = range(value + 1, 4001)
    else:
        raise ValueError(f'Invalid operation "{operation}" for rule: {rule}')

    return valid_ranges


def get_overlap(range1: range, range2: range) -> range:
    return range(max(range1.start, range2.start), min(range1.stop, range2.stop))


def inverse(rule: str) -> str:
    operation = rule[1]
    value = int(rule[2:])
    if operation == '<':
        new_rule = rule[0] + '>' + str(value - 1)
    elif operation == '>':
        new_rule = rule[0] + '<' + str(value + 1)

    return new_rule


def count_valid_combinations(workflows: dict[str, list[str]]) -> int:
    def dfs(current: str, ratings: dict, trace: tuple[str]) -> int:
        if current == 'A':
            return math.prod(len(r) for r in ratings.values())
        if current == 'R':
            return 0

        combos = 0
        for path in workflows[current]:
            if ':' in path:
                rule, next_workflow = path.split(':')
                valid_ranges = get_valid_ranges(rule)
                opposite_ranges = get_valid_ranges(inverse(rule))
                new_ratings = ratings.copy()
                new_ratings[rule[0]] = get_overlap(new_ratings[rule[0]], valid_ranges)

                # Apply opposite range filter to ratings for next iteration
                ratings[rule[0]] = get_overlap(ratings[rule[0]], opposite_ranges)

                combos += dfs(next_workflow, new_ratings, (*trace, current))
            else:
                combos += dfs(path, ratings.copy(), (*trace, current))

        return combos

    starting_ratings = {
        'x': range(1, 4001),
        'm': range(1, 4001),
        'a': range(1, 4001),
        's': range(1, 4001)
    }

    return dfs('in', starting_ratings, ())


def solve_part1(input: str) -> int:
    workflow_text, parts_text = read_input(input)
    workflows = get_workflows(workflow_text.splitlines())
    parts = get_parts(parts_text.splitlines())

    return sum(get_rating(part) for part in parts if part_accepted(part, workflows))


def solve_part2(input: str) -> int:
    workflow_text = read_input(input)[0]
    workflows = get_workflows(workflow_text.splitlines())

    return count_valid_combinations(workflows)


if __name__ == '__main__':
    filename = 'InputFiles\\Day19\\input.txt'
    print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
    print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
