import timeit
import math

def read_input(file: str):
   with open(file) as f:
      input = f.read().split('\n\n')

   return input

def count_differences(line1: str, line2: str) -> int:
   return sum(item1 != item2 for item1, item2 in zip(line1, line2))

def get_row_or_column(pattern: list[str], index: int, axis: int) -> str:
    '''
    axis = 0 returns a row, axis = 1 returns a column for a given index
    '''
    if axis == 0:
      return pattern[index]
    elif axis == 1:
      return ''.join([line[index] for line in pattern])
    else:
      raise ValueError('Invalid axis value')

def get_score(pattern: list[str], allowed_differences: int = 0) -> int:
    for shape, weight, axis in zip((len(pattern), len(pattern[0])), (100, 1), (0, 1)):  
      half = math.ceil((shape - 1) / 2)
      for i in range(shape - 1):
        # Weird calculation to determine size of each reflected half
        # For sample pattern 1 doing vertical reflection, I want the sizes to be this:
        # i    = 0, 1, 2, 3, 4, 5, 6, 7 
        # size = 1, 2, 3, 4, 4, 3, 2, 1
        if i < half:
           factor = 1
        else:
           factor = -2 * (i - half)
        size = i + factor

        differences = 0
        for offset in range(size):
            # Starting at the current line of symmetry (in between row/col with index "i"),
            # compare matching lines and count any differences. Part1 symmetry requires no differences
            # while part2 must have 1 difference (the smudge)

            index1 = i - offset
            index2 = i + offset + 1
           
            side1 = get_row_or_column(pattern, index1, axis)
            side2 = get_row_or_column(pattern, index2, axis)

            differences += count_differences(side1, side2)

        if differences == allowed_differences:
            return weight * (i + 1)
    
    return 0

def solve_part1(input: str) -> int:
   patterns = read_input(input)
   return sum(get_score(pattern.splitlines()) for pattern in patterns)

def solve_part2(input: str) -> int:
   patterns = read_input(input)
   return sum(get_score(pattern.splitlines(), allowed_differences=1) for pattern in patterns)

if __name__ == '__main__':
   filename = 'InputFiles\\Day13\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
