import timeit
import math

# Positive y is "down" 
CONNECTIONS = {
   '|': ((0, 1), (0, -1)),
   '-': ((1, 0), (-1, 0)),
   'L': ((0, -1), (1, 0)),
   'J': ((0, -1), (-1, 0)),
   '7': ((0, 1), (-1, 0)),
   'F': ((0, 1), (1, 0)),
   'S': ((1, 0), (0, 1), (-1, 0), (0, -1))
}

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def get_path(predecessors: dict, start: tuple[int, int], goal: tuple[int, int]) -> list[tuple]:
   current = goal
   path = []
   while current != start:
      path.append(current)
      current = predecessors[current]
   path.append(start)
   path.reverse()
   return path

def can_connect(position1: tuple[int, int], position2: tuple[int, int], tiles: list[str]) -> bool:
   # Check if pipe at position2 allows movement to position1
   tile2 = tiles[position2[1]][position2[0]]
   for direction in CONNECTIONS[tile2]:
      new_position = (position2[0] + direction[0], position2[1] + direction[1])
      if new_position == position1:
         return True
   return False

def get_valid_neighbors(position: tuple[int, int], tiles: list[str]) -> list[tuple]:
   tile = tiles[position[1]][position[0]]
   neighbors = []
   for direction in CONNECTIONS[tile]:
      neighbor = (position[0] + direction[0], position[1] + direction[1])
      neighbor_tile = tiles[neighbor[1]][neighbor[0]]
      if neighbor_tile not in '.S' and can_connect(position, neighbor, tiles):
         neighbors.append(neighbor)
   
   return neighbors

def find_loop(animal: tuple[int, int], tiles: list[str]) -> list[tuple]:
   start, goal = get_valid_neighbors(animal, tiles)
   stack = [start]
   predecessors = {start: None}
   while len(stack) > 0:
      current = stack.pop()
      if current == goal:
         return get_path(predecessors, start, goal)
      
      for neighbor in get_valid_neighbors(current, tiles):
         if neighbor not in predecessors:
            stack.append(neighbor)
            predecessors[neighbor] = current
   
   raise ValueError('No complete loop found')

def solve_part1(input: str) -> int:
   tiles = read_input(input)
   animal = next(((x, y) for y, line in enumerate(tiles) for x, s in enumerate(line) if s == 'S'))
   return math.ceil(len(find_loop(animal, tiles)) / 2)

def solve_part2(input: str) -> int:
   tiles = read_input(input)
   animal = next(((x, y) for y, line in enumerate(tiles) for x, s in enumerate(line) if s == 'S'))
   loop = find_loop(animal, tiles)

if __name__ == '__main__':
   filename = 'InputFiles\\Day10\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
