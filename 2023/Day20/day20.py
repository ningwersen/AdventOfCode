import timeit

def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input

def parse_modules(input: list[str]) -> tuple[dict, dict, dict]:
    flip_flop_modules = dict()
    conjunction_modules = dict()
    connections = dict()
    for line in input:
      start, end = line.split(' -> ')
      if start == 'broadcaster':
         connections[start] = end.split(', ')
         continue

      module_type = start[0]
      module_name = start[1:]
      connections[module_name] = end.split(', ')

      if module_type == '%':
         flip_flop_modules[module_name] = 0
      elif module_type == '&':
         conjunction_modules[module_name] = dict()
      else:
         raise ValueError(f'Invalid module type {module_type}')
    
    # Set inputs for conjunction modules
    for origin in connections:
       for destination in connections[origin]:
          if destination in conjunction_modules:
             conjunction_modules[destination][origin] = 0
    
    return (connections, flip_flop_modules, conjunction_modules)

def solve_part1(input: str) -> int:
   connections, flip_flop_modules, conjuction_modules = parse_modules(read_input(input))
   low_pulses, high_pulses = 0, 0
   for _ in range(1000):
      pulses = push_button(connections, flip_flop_modules, conjuction_modules)
      low_pulses += pulses[0]
      high_pulses += pulses[1]

   return low_pulses * high_pulses

def push_button(connections: dict[str, list[str]], flip_flop_modules: dict[str, int], conjuction_modules: dict[str, dict[str, int]]) -> list[int]:     
   pulses = [('button', 'broadcaster', 0)]
   pulses_sent = [0, 0]
   while len(pulses) > 0:
      origin, module, pulse = pulses.pop(0)
      pulses_sent[pulse] += 1
      destinations = connections.get(module, [])
      if module == 'broadcaster':
        new_pulse = pulse
      elif module in flip_flop_modules:
         # Ignore high pulse
         if pulse == 1:
            continue

         # Flip module
         new_pulse = flip_flop_modules[module] ^ 1
         flip_flop_modules[module] = new_pulse
      elif module in conjuction_modules:
         conjuction_modules[module][origin] = pulse
         new_pulse = int(any(value == 0 for value in conjuction_modules[module].values()))

      for destination in destinations:
         pulses.append((module, destination, new_pulse))

   return pulses_sent
      
def solve_part2(input: str) -> int:
   pass

if __name__ == '__main__':
   filename = 'InputFiles\\Day20\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
