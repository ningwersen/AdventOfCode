import timeit

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def get_total_distance(hold_time: int, race_time: int) -> int:
   return hold_time * (race_time - hold_time)

def solve_part1(input: str) -> int:
   time_text, distance_text = read_input(input)
   race_times = [int(t) for t in time_text[5:].split()]
   race_distances = [int(d) for d in distance_text[9:].split()]
   
   total = 1
   for race_time, distance_record in zip(race_times, race_distances):
      total *= sum((int(get_total_distance(time, race_time) > distance_record) for time in range(race_time + 1)))
   
   return total

def solve_part2(input: str) -> int:
   time_text, distance_text = read_input(input)
   race_time = int(''.join(time_text[5:].split()))
   distance_record = int(''.join(distance_text[9:].split()))
   
   return sum((int(get_total_distance(time, race_time) > distance_record) for time in range(race_time + 1)))

if __name__ == '__main__':
   filename = 'InputFiles\\Day6\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
