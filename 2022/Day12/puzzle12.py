import collections
import string

# Up, right, down, left
DIRECTIONS = (
   0+1j,
   1+0j,
   0-1j,
   -1+0j
)

# Map letters to values
ELEVATION = {'S': 0, 'E': 27}
for e, l in enumerate(string.ascii_lowercase, start=1):
   ELEVATION[l] = e

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def get_path(predecessors: dict, start: complex, end: complex) -> list[complex]:
   current = end
   path = []
   while current != start:
      path.append(current)
      current = predecessors[current]
   path.append(start)
   path.reverse()
   return path

def valid(grid: list[str], position: complex, elevation: int) -> bool:
   if 0 <= position.real < len(grid) and 0 <= position.imag < len(grid[0]):
      if ELEVATION[grid[int(position.real)][int(position.imag)]] - elevation <= 1:
         return True
   
   return False

# TODO: Replace with A* solution
def bfs(grid: list[str], start: complex, goal: complex) -> list[complex]:
   deque = collections.deque()
   deque.append(start)
   predecessors = {start: None}

   while len(deque) > 0:
      current = deque.popleft()
      elevation = ELEVATION[grid[int(current.real)][int(current.imag)]]
      if current == goal:
         return get_path(predecessors, start, goal)
      
      for direction in DIRECTIONS:
         neighbor = current + direction
         if valid(grid, neighbor, elevation) and neighbor not in predecessors:
            deque.append(neighbor)
            predecessors[neighbor] = current
   
   return None

def solve_part1(input: str) -> int:
   map = read_input(input)
   for i, row in enumerate(map):
      for j, s in enumerate(row):
         if s == 'S':
            start = complex(i, j)
         elif s == 'E':
            end = complex(i, j)

   # Minus 1 bc len includes start
   return len(bfs(map, start, end)) - 1

def solve_part2(input: str) -> int:
   map = read_input(input)
   starts = []
   for i, row in enumerate(map):
      for j, s in enumerate(row):
         if s in ('S', 'a'):
            starts.append(complex(i, j))
         elif s == 'E':
            end = complex(i, j)

   lengths = []
   for start in starts:
      path = bfs(map, start, end)
      if path is not None:
         # Minus 1 bc len includes start
         lengths.append(len(path) - 1)

   return min(lengths)

if __name__ == '__main__':
   filename = 'InputFiles\\puzzle12_input.txt'
   print(solve_part1(filename))
   print(solve_part2(filename))
