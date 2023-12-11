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

def can_connect(position1: tuple[int, int], position2: tuple[int, int], tiles: list[str]) -> bool:
   # Check if pipe at position2 allows movement to position1
   tile2 = tiles[position2[1]][position2[0]]
   for direction in CONNECTIONS[tile2]:
      new_position = (position2[0] + direction[0], position2[1] + direction[1])
      if new_position == position1:
         return True
   return False

def determine_tile(animal: tuple[int, int], tiles: list[str]) -> str:
   neighbors = get_valid_neighbors(animal, tiles)
   neighbor_directions = sorted([(n[0] - animal[0], n[1] - animal[1]) for n in neighbors])
   for tile, possible_directions in CONNECTIONS.items():
      if sorted(possible_directions) == neighbor_directions:
         return tile

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
   # Doesn't matter which neighbor we start with since it's a loop
   current = get_valid_neighbors(animal, tiles)[0]
   previous = animal
   path = [animal]
   while current != animal:
      tile = tiles[current[1]][current[0]]
      for direction in CONNECTIONS[tile]:
         new_position = (current[0] + direction[0], current[1] + direction[1])
         # Only two ways to go, forward and back
         if new_position != previous:
            path.append(current)
            previous = current
            current = new_position
            break
   return path

def point_in_loop(point: tuple[int, int], loop: list[tuple], tiles: list[str]) -> bool:
   # Ray cast in one direction and count intersections with loop.
   # Odd number of intersection indiates point is in loop, even is outside
   # Credit to william feng for this idea
   loop_row = sorted([p for p in loop if p[1] == point[1] and p[0] < point[0]])
   # Vertical pipes are always intersections. Horizontal pipes will connect to make one intersection so just
   # count pairs of pipes that move in opposite vertical directions
   matches = {'L': '7', '7': 'L', 'F': 'J', 'J': 'F'}
   open_match = None
   intersections = 0
   for item in loop_row:
      tile = tiles[item[1]][item[0]]
      if tile == '|':
         intersections += 1
      elif tile in matches:
         if open_match is None:
            open_match = tile
         else:
            if tile == matches[open_match]:
               intersections += 1
            open_match = None

   return intersections % 2 == 1

def solve_part1(input: str) -> int:
   tiles = read_input(input)
   animal = next(((x, y) for y, line in enumerate(tiles) for x, s in enumerate(line) if s == 'S'))
   return math.ceil(len(find_loop(animal, tiles)) / 2)

def solve_part2(input: str) -> int:
   tiles = read_input(input)
   animal = next(((x, y) for y, line in enumerate(tiles) for x, s in enumerate(line) if s == 'S'))
   loop = find_loop(animal, tiles)
   # Replace animal with actual tile for counting points inside loop
   tiles[animal[1]] = tiles[animal[1]].replace('S', determine_tile(animal, tiles))
   enclosed_in_loop = 0
   for y in range(len(tiles)):
      for x in range(len(tiles[0])):
         if (x, y) not in loop:
            enclosed_in_loop += point_in_loop((x, y), loop, tiles)
   return enclosed_in_loop

if __name__ == '__main__':
   filename = 'InputFiles\\Day10\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
