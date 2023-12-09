import timeit
from itertools import pairwise
from functools import reduce

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def find_next_value(sequence: list[int], part2: bool = False) -> int:
   sequences = [sequence]
   while not all((s == 0 for s in sequence)):
      sequence = [pair[1] - pair[0] for pair in pairwise(sequence)]
      sequences.append(sequence)

   if part2:
      # Pairwise subtraction from the last sequence to the first
      return reduce(lambda s1, s2: s2 - s1, [s[0] for s in reversed(sequences)])

   return sum((s[-1] for s in sequences))

def solve_part1(input: str) -> int:
   histories = [[int(h) for h in history.split()] for history in read_input(input)]
   return sum((find_next_value(history) for history in histories))

def solve_part2(input: str) -> int:
   histories = [[int(h) for h in history.split()] for history in read_input(input)]
   return sum((find_next_value(history, part2=True) for history in histories))

if __name__ == '__main__':
   filename = 'InputFiles\\Day9\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
