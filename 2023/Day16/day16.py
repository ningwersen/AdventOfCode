import timeit

HEADINGS = {
   'N': (-1, 0),
   'E': (0, 1),
   'S': (1, 0),
   'W': (0, -1)
}

# Describes how direction changes when entering mirror from given direction
MIRRORS = {
   '|': {'N': 'N', 'E': 'NS', 'S': 'S', 'W': 'NS'},
   '-': {'N': 'EW', 'E': 'E', 'S': 'EW', 'W': 'W'},
   '/': {'N': 'E', 'E': 'N', 'S': 'W', 'W': 'S'},
   '\\': {'N': 'W', 'E': 'S', 'S': 'E', 'W': 'N'}
}


def is_valid(position: tuple[int, int], array: list[str]) -> bool:
   bounds = (len(array), len(array[0]))
   for value, bound in zip(position, bounds):
      if value < 0 or value >= bound:
         return False
   return True

def move(position: tuple[int, int], heading: str) -> tuple[int, int]:
   delta = HEADINGS[heading]
   return (position[0] + delta[0], position[1] + delta[1])

def read_input(file: str) :
   with open(file) as f:
      input = f.read().splitlines()

   return input

def trace_beam(cavern: list[str], initial_position: tuple[int, int], initial_heading: str) -> list[tuple]:
   energized = set()
   seen = set()

   first_tile = cavern[initial_position[0]][initial_position[1]]
   if first_tile in MIRRORS:
      beams = [(initial_position, h) for h in MIRRORS[first_tile][initial_heading]]
   else:
      beams = [(initial_position, initial_heading)]

   while len(beams) > 0:
      new_beams = []
      for position, heading in beams:
         if (position, heading) in seen:
            continue

         energized.add(position)
         new_position = move(position, heading)
         if not is_valid(new_position, cavern):
            continue
         
         tile = cavern[new_position[0]][new_position[1]]
         if tile in MIRRORS:
            for new_heading in MIRRORS[tile][heading]:
               new_beams.append((new_position, new_heading))
         else:
            new_beams.append((new_position, heading))
         seen.add((position, heading))
      beams = new_beams

   return energized

def solve_part1(input: str) -> int:
   cavern = read_input(input)
   return len(trace_beam(cavern, (0, 0), 'E'))

def solve_part2(input: str) -> int:
   cavern = read_input(input)
   max_energized = 0
   for r in range(len(cavern)):
      for heading, c in zip(('E', 'W'), (0, len(cavern[0]) - 1)):
         max_energized = max(max_energized, len(trace_beam(cavern, (r, c), heading)))
   
   for c in range(len(cavern[0])):
      for heading, r in zip(('S', 'N'), (0, len(cavern) - 1)):
         max_energized = max(max_energized, len(trace_beam(cavern, (r, c), heading)))
   
   return max_energized

if __name__ == '__main__':
   filename = 'InputFiles\\Day16\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
