import timeit
from itertools import combinations

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def rotate(array: list) -> list:
   return [[row[i] for row in array] for i in range(len(array[0]))]

def expand(image: list[str]) -> list[str]:
   new_image = []
   for row in image:
      if '#' not in row:
         new_image.append('.' * len(row))
      new_image.append(row)
   return new_image

def find_empty_rows(image: list[str]) -> list[int]:
   return [i for i, s in enumerate(image) if '#' not in s]

def find_galaxies(image: list[str]) -> list[tuple]:
   galaxies = []
   for x, row in enumerate(image):
      for y, item in enumerate(row):
         if item == '#':
            galaxies.append((x, y))
   return galaxies

def distance_between(position1: tuple[int, int], position2: tuple[int, int], empty_rows: list[int], empty_columns: list[int], expansion_factor: int) -> int:
   min_x, max_x = min(position1[0], position2[0]), max(position1[0], position2[0])
   min_y, max_y = min(position1[1], position2[1]), max(position1[1], position2[1])
   distance = 0
   for min_max, empty_values in zip(((min_x, max_x), (min_y, max_y)), (empty_rows, empty_columns)):
      min_value, max_value = min_max
      distance += (max_value - min_value) + ((expansion_factor - 1) * len([i for i in empty_values if min_value <= i <= max_value]))

   return distance

def solve_part1(input: str) -> int:
   image = read_input(input)
   empty_rows = find_empty_rows(image)
   empty_columns = find_empty_rows(rotate(image))

   galaxies = find_galaxies(image)
   return sum((distance_between(galaxy1, galaxy2, empty_rows, empty_columns, 2) for galaxy1, galaxy2 in combinations(galaxies, 2)))

def solve_part2(input: str) -> int:
   image = read_input(input)
   empty_rows = find_empty_rows(image)
   empty_columns = find_empty_rows(rotate(image))

   galaxies = find_galaxies(image)
   return sum((distance_between(galaxy1, galaxy2, empty_rows, empty_columns, 1000000) for galaxy1, galaxy2 in combinations(galaxies, 2)))

if __name__ == '__main__':
   filename = 'InputFiles\\Day11\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
