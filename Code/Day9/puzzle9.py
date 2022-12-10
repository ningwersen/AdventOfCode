MOVES = {
   'U': (1, 0),
   'R': (0, 1),
   'D': (-1, 0),
   'L': (0, -1)
}

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def is_neighbor(p1: tuple, p2: tuple):
   for x in range(p1[0] - 1, p1[0] + 2):
      for y in range(p1[1] - 1, p1[1] + 2):
         if (x, y) == p2:
            return True
   
   return False

def move_tail(head: tuple, tail: tuple) -> tuple:
   moves = []
   if head[0] > tail[0]:
      moves.append('U')
   if head[0] < tail[0]:
      moves.append('D')
   if head[1] > tail[1]:
      moves.append('R')
   if head[1] < tail[1]:
      moves.append('L')

   for move in moves:
      tail = tuple(map(lambda x, y: x + y, tail, MOVES[move]))
   
   return tail

def move_snake(commands: list[str], length: int) -> int:
   knots = [(0, 0) for _ in range(length)]

   last_tail_pos = set()
   last_tail_pos.add(knots[-1])
   for command in commands:
      direction, times = command.split()
      for _ in range(int(times)):
         knots[0] = tuple(map(lambda x, y: x + y, knots[0], MOVES[direction]))

         for i in range(len(knots) - 1):
            if not is_neighbor(knots[i], knots[i+1]):
               knots[i+1] = move_tail(knots[i], knots[i+1])
         
         last_tail_pos.add(knots[-1])

   return len(last_tail_pos)

def solve_part1(input: str) -> int:
   commands = read_input(input)
   return move_snake(commands, 2)

def solve_part2(input: str) -> int:
   commands = read_input(input)
   return move_snake(commands, 10)

if __name__ == '__main__':
   filename = 'InputFiles\\puzzle9_input.txt'
   print(solve_part1(filename))
   print(solve_part2(filename))
