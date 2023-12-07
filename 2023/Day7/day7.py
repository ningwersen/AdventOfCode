import timeit
from collections import Counter

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def read_input(file: str) -> list[str]:
   with open(file) as f:
      input = f.read().splitlines()

   return input

def replace_jokers(hand: str) -> str:
   counter = Counter(hand.replace('J', ''))
   most_common = counter.most_common()
   if not most_common:
      # Card is all jokers
      return 'A' * 5
   
   return hand.replace('J', most_common[0][0])

def strength(hand: str, part2: bool = False) -> tuple[int, list[int]]:
   # For part2, jokers have the lowest hand value
   hand_values = [CARDS.index(card) if not (part2 and card == 'J') else -1 for card in hand]
   if part2 and 'J' in hand:
      hand = replace_jokers(hand)

   counter = Counter(hand)
   
   most_common = counter.most_common()
   if most_common[0][1] == 5:
      return (6, hand_values)
   if most_common[0][1] == 4:
      return (5, hand_values)
   if most_common[0][1] == 3 and most_common[1][1] == 2:
      return (4, hand_values)
   if most_common[0][1] == 3:
      return (3, hand_values)
   if most_common[0][1] == 2 and most_common[1][1] == 2:
      return (2, hand_values)
   if most_common[0][1] == 2:
      return (1, hand_values)
   
   return (0, hand_values)

def solve_part1(input: str) -> int:
   lines = read_input(input)
   hands_and_bets = [(line.split()[0], int(line.split()[1])) for line in lines]
   hands_and_bets.sort(key=lambda h_and_b: strength(h_and_b[0]))
   return sum((index * bet[1] for index, bet in enumerate(hands_and_bets, start=1)))

def solve_part2(input: str) -> int:
   lines = read_input(input)
   hands_and_bets = [(line.split()[0], int(line.split()[1])) for line in lines]
   hands_and_bets.sort(key=lambda h_and_b: strength(h_and_b[0], True))
   return sum((index * bet[1] for index, bet in enumerate(hands_and_bets, start=1)))

if __name__ == '__main__':
   filename = 'InputFiles\\Day7\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
