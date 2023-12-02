import timeit

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def get_games(text: list[str]) -> list[list[dict]]:
   games = []
   for line in text:
      game = []
      cubes_pulled = line.split(': ')[1]
      for pull in cubes_pulled.split('; '):
         cubes = pull.split(', ')
         game.append({cube.split()[1]: int(cube.split()[0]) for cube in cubes})
      games.append(game)
   
   return games

def validate_game(game: list[dict], cubes: dict) -> bool:
   for pull in game:
      for color in pull:
         if pull[color] > cubes[color]:
            return False
   
   return True

def min_cubes_power(game: list[dict]) -> int:
   min_cubes = {'red': 0, 'blue': 0, 'green': 0}
   for pull in game:
      for color in pull:
         if pull[color] > min_cubes[color]:
            min_cubes[color] = pull[color]
   
   return min_cubes['red'] * min_cubes['blue'] * min_cubes['green']

def solve_part1(input: str) -> int:
   game_text = read_input(input)
   games = get_games(game_text)
   cubes = {'red': 12, 'green': 13, 'blue': 14}
   
   return sum((index + 1 for index, game in enumerate(games) if validate_game(game, cubes)))

def solve_part2(input: str) -> int:
   game_text = read_input(input)
   games = get_games(game_text)

   return sum((min_cubes_power(game) for game in games))

if __name__ == '__main__':
   filename = 'InputFiles\\Day2\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
