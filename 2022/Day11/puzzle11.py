from monkeys import Monkey1, Monkey2
from collections import deque
import math

def read_input(file: str):
   with open(file) as f:
      input = f.read().split('\n\n')

   return input

def run(text: list[str], rounds: int, monkey_class) -> int:
   monkeys: list = []
   for block in text:
      lines = block.splitlines()
      items = deque([int(s) for s in lines[1].split('Starting items: ')[1].split(', ')])
      operation = lines[2].split('Operation: new = ')[1]
      test = int(lines[3].split()[-1])
      true = int(lines[4].split()[-1])
      false = int(lines[5].split()[-1])

      monkeys.append(monkey_class(items, operation, test, true, false))
   
   if monkey_class == Monkey2:
      lcm = math.lcm(*[m.test for m in monkeys])
      for m in monkeys:
         m.lcm = lcm

   for _ in range(rounds):
      for monkey in monkeys:
         transfers = monkey.inspect_items()
         for index, item in transfers:
            monkeys[index].items.append(item)

   return math.prod(sorted([m.inspections for m in monkeys], reverse=True)[:2])

def solve_part1(input: str) -> int:
   monkey_text = read_input(input)
   return run(monkey_text, 20, Monkey1)
            
def solve_part2(input: str) -> int:
   monkey_text = read_input(input)
   return run(monkey_text, 10000, Monkey2)

if __name__ == '__main__':
   filename = 'InputFiles\\puzzle11_input.txt'
   print(solve_part1(filename))
   print(solve_part2(filename))
