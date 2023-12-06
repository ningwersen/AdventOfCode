import timeit

def read_input(file: str):
   with open(file) as f:
      input = f.read().split('\n\n')

   return input

def get_seed_ranges(values: list[int]) -> list[range]:
   seed_ranges = []
   for index in range(0, len(values), 2):
      seed_ranges.append(range(values[index], values[index] + values[index + 1]))
   
   return seed_ranges

def create_map(text: list[str]) -> list[tuple[range, range]]:
   map = []
   for line in text:
      destination_start, source_start, length = [int(n) for n in line.split()]
      source_range = range(source_start, source_start + length)
      destination_range = range(destination_start, destination_start + length)
      map.append((source_range, destination_range))
   
   return map

def get_final_value(value: int, maps: list[list[tuple[range, range]]]) -> int:
   for mapping in maps:
      for source, destination in mapping:
         if value in source:
            difference = value - source.start
            value = destination.start + difference
            break

   return value

# Another day, another recursive dfs solution
def find_final_ranges(current_range: range, index: int, maps: list[list[tuple[range, range]]]) -> list[range]:
   if index == len(maps):
      return [current_range]
   
   new_ranges = []
   for source, destination in maps[index]:
      overlap = range(max(current_range.start, source.start), min(current_range.stop, source.stop))
      if len(overlap) == 0:
         continue
      offset = overlap.start - source.start
      new_start = destination.start + offset
      new_ranges.extend(find_final_ranges(range(new_start, new_start + len(overlap)), index + 1, maps))

      # Check the parts of the original range not in the overlap if they exist
      if current_range.start < overlap.start:
         new_ranges.extend(find_final_ranges(range(current_range.start, overlap.start), index, maps))
      if overlap.stop < current_range.stop:
         new_ranges.extend(find_final_ranges(range(overlap.stop, current_range.stop), index, maps))
      break
   else:
      # Keep the original range if there weren't any overlaps
      new_ranges.extend(find_final_ranges(current_range, index + 1, maps))

   return new_ranges

def solve_part1(input: str) -> int:
   seed_text, *maps_text = read_input(input)
   seeds = [int(n) for n in seed_text[6:].split()]
   maps = [create_map(text.splitlines()[1:]) for text in maps_text]
   
   return min((get_final_value(seed, maps) for seed in seeds))

def solve_part2(input: str) -> int:
   seed_text, *maps_text = read_input(input)
   seed_values = [int(n) for n in seed_text[6:].split()]
   seed_ranges = get_seed_ranges(seed_values)
   maps = [create_map(text.splitlines()[1:]) for text in maps_text]

   location_ranges: list[range] = []
   for seed_range in seed_ranges:
      location_ranges.extend(find_final_ranges(seed_range, 0, maps))
   
   return min((location_range.start for location_range in location_ranges))

if __name__ == '__main__':
   filename = 'InputFiles\\Day5\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
