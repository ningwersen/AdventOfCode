import timeit

DIRECTIONS = [
   (0, 1),
   (1, 1),
   (1, 0),
   (1, -1),
   (0, -1),
   (-1, -1),
   (-1, 0),
   (-1, 1)
]

SEEN = set()

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def is_valid(position: tuple[int, int], bounds: tuple[int, int]) -> bool:
   for value, bound in zip(position, bounds):
      if not (0 <= value < bound):
         return False
   
   return True

def get_number(line: str, position: tuple[int, int]) -> int:
   if position in SEEN:
      return None
   
   number = [line[position[0]]]
   # Check both sides of position and add digits to start/end of string
   for x, character in enumerate(line[position[0] + 1:]):
      if not character.isdigit():
         break
      number.append(character)
      SEEN.add((position[0] + x + 1, position[1]))

   for x, character in enumerate(line[:position[0]][::-1]):
      if not character.isdigit():
         break
      SEEN.add((position[0] - x - 1, position[1]))
      number.insert(0, character)
   
   return int(''.join(number))

def find_part_numbers(schematic: list[str]) -> list[int]:
   part_numbers = []
   bounds = (len(schematic[0]), len(schematic))
   for y, line in enumerate(schematic):
      for x, character in enumerate(line):
         if character == '.' or character.isdigit():
            continue

         for direction in DIRECTIONS:
            position = (x + direction[0], y + direction[1])
            if is_valid(position, bounds) and schematic[position[1]][position[0]].isdigit():
               number = get_number(schematic[position[1]], position)
               if number:
                  part_numbers.append(number)
   
   return part_numbers

def find_gear_ratios(schematic: list[str]) -> list[int]:
   gear_ratios = []
   bounds = (len(schematic[0]), len(schematic))
   for y, line in enumerate(schematic):
      for x, character in enumerate(line):
         if character != '*':
            continue
         
         part_numbers = []
         for direction in DIRECTIONS:
            position = (x + direction[0], y + direction[1])
            if is_valid(position, bounds) and schematic[position[1]][position[0]].isdigit():
               number = get_number(schematic[position[1]], position)
               if number:
                  part_numbers.append(number)
         
         if len(part_numbers) == 2:
            gear_ratios.append(part_numbers[0] * part_numbers[1])
   
   return gear_ratios

def solve_part1(input: str) -> int:
   schematic = read_input(input)
   return sum(find_part_numbers(schematic))

def solve_part2(input: str) -> int:
   schematic = read_input(input)
   return sum(find_gear_ratios(schematic))

if __name__ == '__main__':
   filename = 'InputFiles\\Day3\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
