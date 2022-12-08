import math

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def solve_part1(input: str) -> int:
   trees = read_input(input)

   # Border
   visible = (len(trees) * 2) + ((len(trees[0]) - 2) * 2)

   # Interior trees
   for x in range(1, len(trees) - 1):
      for y in range(1, len(trees[0]) - 1):
         height = int(trees[x][y])
         up = [int(line[y]) for line in trees[:x]]
         down = [int(line[y]) for line in trees[x+1:]]
         right = [int(t) for t in list(trees[x][y+1:])]
         left = [int(t) for t in list(trees[x][:y])]

         for direction in [up, down, left, right]:
            if height > max(direction):
               visible += 1
               break
   
   return visible

def solve_part2(input: str) -> int:
   trees = read_input(input)

   # Trees on edge have at least 1 distance = 0
   # That means their scenic score will also be 0 and we can ignore them
   scenic_scores = []
   for x in range(1, len(trees) - 1):
      for y in range(1, len(trees[0]) - 1):
         height = int(trees[x][y])

         up = [int(line[y]) for line in trees[:x]]
         down = [int(line[y]) for line in trees[x+1:]]
         right = [int(t) for t in list(trees[x][y+1:])]
         left = [int(t) for t in list(trees[x][:y])]

         # Order matters
         # Reverse to start with closest trees
         up.reverse()
         left.reverse()

         view_scores = []
         for direction in [up, right, down, left]:
            direction_score = 0
            for tree in direction:
               direction_score += 1
               if tree >= height:
                  break
            
            view_scores.append(direction_score)
         
         scenic_scores.append(math.prod(view_scores))
   
   return max(scenic_scores)

if __name__ == '__main__':
   filename = 'InputFiles\\puzzle8_input.txt'
   print(solve_part1(filename))
   print(solve_part2(filename))
