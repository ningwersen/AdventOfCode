import functools

def read_input(file: str):
   with open(file) as f:
      input = f.read().split('\n\n')

   return input

def correct_order(left, right) -> bool:

   if isinstance(left, type(right)):
      if isinstance(left, int) and isinstance(right, int):
         if left == right:
            # continue checking the next part of the input
            return None
         else:
            # If the left integer is lower than the right integer, the inputs are in the right order
            return left < right

      if isinstance(left, list) and isinstance(right, list):
         left, right = left.copy(), right.copy()
         while len(left) > 0 and len(right) > 0:
            correct = correct_order(left.pop(0), right.pop(0))
            if correct is not None:
               return correct

         if len(left) == len(right):
            # continue checking the next part of the input
            return None
         else:
            # If the right list runs out of items first, the inputs are not in the right order
            return len(right) > len(left)
   else:
      # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, 
      # then retry the comparison
      if isinstance(right, int):
         right = [right]
      elif isinstance(left, int):
         left = [left]
      
      return correct_order(left, right)

def solve_part1(input: str) -> int:
   correct_indices = []
   for i, section in enumerate(read_input(input), start=1):
      left, right = [eval(pair) for pair in section.splitlines()]

      if correct_order(left, right) == 1:
         correct_indices.append(i)
   
   return sum(correct_indices)

def solve_part2(input: str) -> int:
   # Divider packets
   packets = [[[2]], [[6]]]
   for section in read_input(input):
      packets.extend([eval(pair) for pair in section.splitlines()])

   # bubble sort
   length = len(packets)
   for i in range(length):
      for j in range(0, length - i - 1):
         if not correct_order(packets[j], packets[j+1]):
            packets[j], packets[j+1] = packets[j+1], packets[j]
   
   return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

if __name__ == '__main__':
   filename = 'InputFiles\\puzzle13_input.txt'
   print(solve_part1(filename))
   print(solve_part2(filename))
