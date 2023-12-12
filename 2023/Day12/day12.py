import timeit

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def count_possible_arrangements(spring: str, part2: bool = False) -> int:
   conditions, groupings = spring.split()
   if part2:
      conditions = '?'.join([conditions] * 5)
      groupings = ','.join([groupings] * 5)
   groupings = [int(n) for n in groupings.split(',')]

   cache = {}
   def dfs(index: int, group_index: int, group_length: int) -> int:
      key = (index, group_index, group_length)
      if key in cache:
         return cache[key]
      
      if index == len(conditions):
         if group_index == len(groupings) and group_length == 0:
            # Ending on a '.' with all groups matched
            return 1
         elif group_index == len(groupings) - 1 and groupings[group_index] == group_length:
            # Ending on a '#' that finishes the last group
            return 1
         else:
            return 0
         
      possible = 0
      current_state = conditions[index]
      # Explore both options if there's a '?'
      if current_state == '.' or current_state == '?':
         if group_length > 0 and group_index < len(groupings) and group_length == groupings[group_index]:
            # End of group
            possible += dfs(index + 1, group_index + 1, 0)
         elif group_length == 0:
            possible += dfs(index + 1, group_index, 0)
      if current_state == '#' or current_state == '?':
         possible += dfs(index + 1, group_index, group_length + 1)
      
      cache[key] = possible
      return possible

   return dfs(0, 0, 0)

def solve_part1(input: str) -> int:
   spring_conditions = read_input(input)
   return sum((count_possible_arrangements(row) for row in spring_conditions))

def solve_part2(input: str) -> int:
   spring_conditions = read_input(input)
   return sum((count_possible_arrangements(row, part2=True) for row in spring_conditions))

if __name__ == '__main__':
   filename = 'InputFiles\\Day12\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
