import numpy as np

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def print_cave(cave: np.ndarray):
   rep1 = np.where(cave == 0, '.', cave)
   rep2 = np.where(rep1 == '1', '#', rep1)
   rep3 = np.where(rep2 == '2', 'o', rep2)
   final = np.where(rep3 == '9', '+', rep3)
   print(final)

def generate_rocks(start: tuple[int, int], end: tuple[int, int]):
   if start[0] <= end[0]:
      x_range = range(start[0], end[0] + 1)
   else:
      x_range = range(end[0], start[0] + 1)

   if start[1] <= end[1]:
      y_range = range(start[1], end[1] + 1)
   else:
      y_range = range(end[1], start[1] + 1)

   rocks = []
   for x in x_range:
      for y in y_range:
         rocks.append((x, y))

   return rocks

def is_valid(cave: np.ndarray, location: tuple, expand: bool = False):
   if location[0] < 0 or location[0] >= cave.shape[0]:
      return False
   if location[1] < 0 or location[1] >= cave.shape[1]:
      return False
   
   return True

def expand_cave(cave: np.ndarray, location: tuple) -> np.ndarray:
   if location[1] < 0:
      new_cave = np.zeros((cave.shape[0], cave.shape[1] + 1), dtype=np.int_)
      new_cave[:, 1:] = cave
      # Extend floor
      new_cave[-1, :] = 1

      return new_cave

   elif location[1] >= cave.shape[1]:
      new_cave = np.zeros((cave.shape[0], cave.shape[1] + 1), dtype=np.int_)
      new_cave[:, :-1] = cave
      # Extend floor
      new_cave[-1, :] = 1

      return new_cave

   else:
      return cave

def propagate_sand(cave: np.ndarray, location: tuple, expand: bool = False) -> tuple[np.ndarray, tuple[int, int]]:
   down = cave[location[0]:, location[1]].flatten()
   blockage = np.where((down == 1) | (down == 2))
   if len(blockage[0]) == 0:
      raise ValueError("Infinite propagation")

   blockage_y_index = blockage[0][0] + location[0]

   sand = (blockage_y_index - 1, location[1])
   left = (blockage_y_index, location[1] - 1)
   right = (blockage_y_index, location[1] + 1)

   if expand:
      old_shape = cave.shape
      cave = expand_cave(cave, left)
      # Shift indicies if column was added at beginning
      if old_shape != cave.shape:
         sand = (sand[0], sand[1] + 1)
         left = (left[0], left[1] + 1)
         right = (right[0], right[1] + 1)
      cave = expand_cave(cave, right)

   else:
      if not is_valid(cave, left):
         raise ValueError("Infinite propagation")

      if not is_valid(cave, right):
         raise ValueError("Infinite propagation")

   if cave[left[0], left[1]] not in (1, 2):
      cave, sand = propagate_sand(cave, left, expand)
   elif cave[right[0], right[1]] not in (1, 2):
      cave, sand = propagate_sand(cave, right, expand)
   
   if not is_valid(cave, sand):
      test = 'break'
   return cave, sand

def create_cave(rock_paths: list[list[tuple]], include_floor: bool = False):
   sand = (500, 0)
   rocks = set()
   for path in rock_paths:
      for i in range(len(path) - 1):
         rocks.update(generate_rocks(path[i], path[i+1]))
      
   y_min = 0
   y_max = max((r[1] for r in rocks))
   if include_floor:
      y_max += 2
   x_min = min(min((r[0] for r in rocks)), 500)
   x_max = max(max((r[0] for r in rocks)), 500)

   array = np.zeros((y_max - y_min + 1, x_max - x_min + 1), np.int_)
   rocks = [(r[0] - x_min, r[1]) for r in rocks]
   array[[r[1] for r in rocks], [r[0] for r in rocks]] = 1
   array[sand[1], sand[0] - x_min] = 9

   if include_floor:
      array[y_max, :] = 1
   
   return array
      

def solve_part1(input: str) -> int:
   rock_paths = [[(int(r.split(',')[0]), int(r.split(',')[1])) for r in p] for p in [l.split(' -> ') for l in read_input(input)]]

   # Cave coordinates will be (y, x), origin (0, 0)
   # 0 = air, 1 = rock, 9 = sand source
   cave = create_cave(rock_paths)
   source = np.where(cave == 9)
   source = (source[0][0], source[1][0])

   propagating = True
   while propagating:
      try:
         cave, new_sand = propagate_sand(cave, source)
         cave[new_sand[0], new_sand[1]] = 2
      except ValueError:
         propagating = False
   
   return np.count_nonzero(cave == 2)

def solve_part2(input: str) -> int:
   rock_paths = [[(int(r.split(',')[0]), int(r.split(',')[1])) for r in p] for p in [l.split(' -> ') for l in read_input(input)]]

   # Cave coordinates will be (y, x), origin (0, 0)
   # 0 = air, 1 = rock, 9 = sand source
   cave = create_cave(rock_paths, include_floor=True)

   propagating = True
   while propagating:
      source = np.where(cave == 9)
      source = (source[0][0], source[1][0])

      cave, new_sand = propagate_sand(cave, source, expand=True)
      cave[new_sand[0], new_sand[1]] = 2
      #print_cave(cave)
      if new_sand == source:
         break

   return np.count_nonzero(cave == 2)

if __name__ == '__main__':
   filename = 'InputFiles\\puzzle14_input.txt'
   print(solve_part1(filename))
   print(solve_part2(filename))
