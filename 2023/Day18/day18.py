import timeit

DIRECTIONS = {
   'U': (0, 1),
   'D': (0, -1),
   'L': (-1, 0),
   'R': (1, 0)
}

DIGIT_TO_DIRECTION = {
   0: 'R',
   1: 'D',
   2: 'L',
   3: 'U'
}

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def parse_hexadecimal(hexadecimal: str) -> tuple[str, int]:
   length = int(hexadecimal[:-1].replace('#', '0x'), 16)
   direction = DIGIT_TO_DIRECTION[int(hexadecimal[-1])]
   return (direction, length)

def get_perimeter(instructions: list[tuple[str, int]]):
   trench = {0: {0}}
   position = (0, 0)
   for direction, length in instructions:
      delta = DIRECTIONS[direction]
      for _ in range(length):
         position = (position[0] + delta[0], position[1] + delta[1])
         if position[1] not in trench:
            trench[position[1]] = {position[0]}
            continue
         trench[position[1]].add(position[0])
   
   return trench

def fill_trench(perimeter: dict) -> int:
   filled_points = 0
   # Count the points inside perimeter of each row.
   for row in perimeter:
      if (row + 1) not in perimeter or (row - 1) not in perimeter:
         continue

      # A pair of opposite corners is an intersection into the polygon formed by the perimeter --> ⌝⌞ or ⌟⌜
      # vertical intersections also count --> |
      # If we're inside the polygon, add spaces between current perimeter 'x' value and previous 'x' value
      # If it's a horizontal border, this will be 0 spaces
      pair_start = None
      up_corner = False
      down_corner = False
      inside = False
      for x in sorted(perimeter[row]):
         if pair_start is not None:
            filled_points += x - pair_start - 1
            pair_start = None
         
         if x in perimeter[row + 1]:
            up_corner = not up_corner
         if x in perimeter[row - 1]:
            down_corner = not down_corner
         
         if up_corner and down_corner:
            inside = not inside
            up_corner = False
            down_corner = False
         
         if inside and pair_start is None:
            pair_start = x

   return filled_points

def solve_part1(input: str) -> int:
   text = read_input(input)
   instructions = [(line.split()[0], int(line.split()[1])) for line in text]
   trench_perimeter = get_perimeter(instructions)
   return sum(len(p) for p in trench_perimeter.values()) + fill_trench(trench_perimeter)

def solve_part2(input: str) -> int:
   text = read_input(input)
   instructions = [parse_hexadecimal(line.split()[2][1:-1]) for line in text]
   trench_perimeter = get_perimeter(instructions)
   return sum(len(p) for p in trench_perimeter.values()) + fill_trench(trench_perimeter)

if __name__ == '__main__':
   filename = 'InputFiles\\Day18\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
