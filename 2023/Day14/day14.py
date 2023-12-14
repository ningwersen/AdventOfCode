import timeit
import numpy as np

ROTATIONS = {
   'N': 0,
   'E': 1,
   'S': 2,
   'W': 3
}

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def move_rocks(rocks: np.ndarray, direction: str) -> np.ndarray:
   # This function could definitely be rewritten to be generic and work in all directions,
   # but I was lazy and only made it work for moving rocks north for part1. So for all other
   # directions I rotate the array, move rocks north and then rotate back lol
   rocks = np.rot90(rocks, k=ROTATIONS[direction])
   new_rocks = rocks.copy()
   for c in range(rocks.shape[0]):
      column = rocks[:, c]
      next_rock = -1
      for r, value in enumerate(column):
         if value == '.':
            continue
         elif value == '#':
            next_rock = r
            continue

         if next_rock + 1 < r:
            new_rocks[r, c] = '.'
            new_rocks[next_rock + 1, c] = 'O'
            next_rock += 1
         else:
            next_rock = r
   new_rocks = np.rot90(new_rocks, 4 - ROTATIONS[direction])
   return new_rocks

def cycle(rocks: np.ndarray) -> np.ndarray:
   for direction in ['N', 'W', 'S', 'E']:
      rocks = move_rocks(rocks, direction)
   return rocks

def calculate_load(rocks: np.ndarray) -> int:
   return sum((np.sum(row == 'O') * (rocks.shape[0] - i) for i, row in enumerate(rocks)))

def hashify(array: np.ndarray) -> tuple[str]:
   string_array = [''.join(row) for row in array]
   return tuple(string_array)

def solve_part1(input: str) -> int:
   rocks = np.array([list(row) for row in read_input(input)], dtype=np.str_)
   new_rocks = move_rocks(rocks, 'N')
   return calculate_load(new_rocks)

def solve_part2(input: str) -> int:
   rocks = np.array([list(row) for row in read_input(input)], dtype=np.str_)
   SEEN = dict()
   i = 1
   # Find when the cycles start to repeat
   while True:
      rocks = cycle(rocks)
      rock_hash = hashify(rocks)
      if rock_hash in SEEN:
         break
      
      SEEN[rock_hash] = i
      i += 1
   
   repeat = i - SEEN[rock_hash]
   # Cycle until rocks are aligned with the billionth cycle
   for _ in range((1000000000 - i) % repeat):
      rocks = cycle(rocks)
   return calculate_load(rocks)

if __name__ == '__main__':
   filename = 'InputFiles\\Day14\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
