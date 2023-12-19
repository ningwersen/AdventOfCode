import timeit
import heapq

DIRECTIONS = {
   'E': (0, 1),
   'S': (1, 0),
   'W': (0, -1),
   'N': (-1, 0)
}

OPPOSITES  = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}

def read_input(file: str) :
   with open(file) as f:
      input = f.read().splitlines()

   return input

def is_valid(position: tuple[int, int], graph: list[list[int]]) -> bool:
   bounds = (len(graph), len(graph[0]))
   for value, bound in zip(position, bounds):
      if value < 0 or value >= bound:
         return False
   return True

def valid_directions(current_direction: str, streak: int, part2: bool) -> list[tuple[str, tuple]]:
   directions = []
   for direction in DIRECTIONS:
      if direction == OPPOSITES[current_direction]:
         continue

      if direction == current_direction:
         if part2:
            if streak == 10:
               continue
         else:
            if streak == 3:
               continue
      else:
         if part2 and streak < 4:
            continue
      
      directions.append(direction)
   return directions

def dijsktra(graph: list[list[int]], start: tuple[int, int], end: tuple[int, int], part2: bool = False):
   seen = set()
   nodes = []
   # Heat loss, position, direction, streak
   heapq.heappush(nodes, (0, start, 'E', 0))

   while len(nodes) > 0:
      heat_loss, current, direction, streak = heapq.heappop(nodes)
      if current == end:
         return heat_loss
      
      if (current, direction, streak) in seen:
         continue
      seen.add((current, direction, streak))

      for new_direction in valid_directions(direction, streak, part2):
         delta = DIRECTIONS[new_direction]
         neighbor = (current[0] + delta[0], current[1] + delta[1])
         if not is_valid(neighbor, graph):
            continue

         if new_direction == direction:
            new_streak = streak + 1
         else:
            new_streak = 1
         
         new_heat_loss = heat_loss + graph[neighbor[0]][neighbor[1]]
         heapq.heappush(nodes, (new_heat_loss, neighbor, new_direction, new_streak))

   raise RuntimeError('No valid path found')

def solve_part1(input: str) -> int:
   map = [[int(i) for i in row] for row in read_input(input)]
   goal = (len(map) - 1, len(map[0]) - 1)
   return dijsktra(map, (0, 0), goal)

def solve_part2(input: str) -> int:
   map = [[int(i) for i in row] for row in read_input(input)]
   goal = (len(map) - 1, len(map[0]) - 1)
   return dijsktra(map, (0, 0), goal, part2=True)

if __name__ == '__main__':
   filename = 'InputFiles\\Day17\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
