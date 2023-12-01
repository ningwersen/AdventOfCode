import timeit

DIGIT_MAP = {
   'one': '1',
   'two': '2',
   'three': '3',
   'four': '4',
   'five': '5',
   'six': '6',
   'seven': '7',
   'eight': '8',
   'nine': '9'
}

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def get_numbers(string: str) -> int:
   digits = [c for c in string if c.isnumeric()]
   return int(digits[0] + digits[-1])

def get_numbers2(string: str) -> int:
   digits = []
   for index, character in enumerate(string):
      if character.isnumeric():
         digits.append(character)
         continue

      # Check if number is spelled out
      number_string = character
      buffer = 1
      while (index + buffer < len(string)) and any((number_string in digit for digit in DIGIT_MAP)):
         number_string += string[index + buffer]
         if number_string in DIGIT_MAP:
            digits.append(DIGIT_MAP[number_string])
            break
         buffer += 1
   
   return int(digits[0] + digits[-1])

def solve_part1(input: str) -> int:
   return sum((get_numbers(line) for line in read_input(input)))

def solve_part2(input: str) -> int:
   return sum((get_numbers2(line) for line in read_input(input)))

if __name__ == '__main__':
   filename = 'InputFiles\\Day1\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
