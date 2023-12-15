import timeit
import re

def read_input(file: str) -> str:
   with open(file) as f:
      input = f.read()

   return input

def hash_algorithm(string: str) -> int:
   value = 0
   for s in string:
      value += ord(s)
      value *= 17
      value %= 256
   
   return value

def configure_boxes(initialization_sequence: str) -> dict[int, list]:
   boxes: dict[int, list] = dict()
   for label, focal_length in re.findall(r'(\w+)(?:-|(?:=(\d)))', initialization_sequence):
      # Focal length of '' means the operation was a dash (remove)
      box = hash_algorithm(label)
      if box not in boxes:
         if focal_length != '':
            boxes[box] = [[label, int(focal_length)]]
         continue
      
      for item in boxes[box]:
         if item[0] == label:
            break
      else:
         if focal_length != '':
            boxes[box].append([label, int(focal_length)])
         continue

      if focal_length == '':
         boxes[box].remove(item)
      else:
         item[1] = int(focal_length)

   return boxes

def compute_focusing_power(lenses: list, box_factor: int) -> int:
   # Box factor is box number + 1
   return sum((box_factor * (index + 1) * value[1] for index, value in enumerate(lenses)))

def solve_part1(input: str) -> int:
   initialization_sequence = read_input(input).split(',')
   return sum((hash_algorithm(string) for string in initialization_sequence))

def solve_part2(input: str) -> int:
   initialization_sequence = read_input(input)
   boxes = configure_boxes(initialization_sequence)
   return sum((compute_focusing_power(lenses, box_number + 1) for box_number, lenses in boxes.items()))

if __name__ == '__main__':
   filename = 'InputFiles\\Day15\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
