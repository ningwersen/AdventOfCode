import timeit

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def get_card(line: str) -> tuple[set, list]:
      line = line.split(': ')[1]
      winning_numbers, my_numbers = line.split(' | ')
      winning_numbers = set((int(number) for number in winning_numbers.split()))
      my_numbers = [int(number) for number in my_numbers.split()]
      return (winning_numbers, my_numbers)

def get_matches(card: tuple[set, list]) -> list[int]:
   return [number for number in card[1] if number in card[0]]

def score(card: tuple[set, list]) -> int:
   matches = get_matches(card)
   # 1 match is 1 point, doubled for every additional match
   return int(2 ** (len(matches) - 1)) * int(len(matches) > 0)

def solve_part1(input: str) -> int:
   cards = [get_card(line) for line in read_input(input)]
   return sum((score(card) for card in cards))

def solve_part2(input: str) -> int:
   card_reference = [get_card(line) for line in read_input(input)]

   cards = list(range(len(card_reference)))
   cache = dict()
   def dfs(card: int) -> int:
      if card in cache:
         return cache[card]

      number_matches = len(get_matches(card_reference[card]))
      used = 1
      for c in range(card + 1, card + 1 + number_matches):
         used += dfs(c)
      
      cache[card] = used
      return used

   return sum((dfs(card) for card in cards))

if __name__ == '__main__':
   filename = 'InputFiles\\Day4\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
