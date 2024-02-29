import timeit

def read_input(file: str):
   with open(file) as f:
      input = f.read().split('\n\n')

   return input

def get_workflows(text: list[str]) -> dict:
   workflows = dict()
   for line in text:
      open_bracket = line.index('{')
      name = line[:open_bracket]
      rules = line[open_bracket+1:-1]
      workflows[name] = rules.split(',')
   
   return workflows

def get_parts(text: list[str]) -> list[dict]:
   parts = []
   for line in text:
      part = dict()
      for value in line[1:-1].split(','):
         category, rating = value.split('=')
         part[category] = int(rating)
      
      parts.append(part)
   
   return parts

def evaluate_inequality(inequality: str, part: dict) -> bool:
   category = inequality[0]
   operation = inequality[1]
   value = int(inequality[2:])

   if operation == '<':
      return part[category] < value
   elif operation == '>':
      return part[category] > value
   else:
      raise ValueError(f'Invalid operation "{operation}" for inequality: {inequality}')


def part_accepted(part: dict, workflows: dict) -> bool:
   current_workflow = 'in'

   while current_workflow not in ('A', 'R'):
      for test in workflows[current_workflow]:
         if ':' in test:
            inequality, next_workflow = test.split(':')
            if evaluate_inequality(inequality, part) == True:
               current_workflow = next_workflow
               break
         else:
            current_workflow = test

   return current_workflow == 'A'

def get_rating(part: dict) -> int:
   return sum(part.values())

def solve_part1(input: str) -> int:
   workflow_text, parts_text = read_input(input)
   workflows = get_workflows(workflow_text.splitlines())
   parts = get_parts(parts_text.splitlines())

   return sum(get_rating(part) for part in parts if part_accepted(part, workflows))

def solve_part2(input: str) -> int:
   pass

if __name__ == '__main__':
   filename = 'InputFiles\\Day19\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
