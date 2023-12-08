import timeit
import math

def read_input(file: str):
   with open(file) as f:
      input = f.read().split('\n\n')

   return input

def get_network(text: str) -> dict:
   network = {}
   for line in text.splitlines():
      node, paths = line.split(' = ')
      left_path = paths[1:paths.index(',')]
      right_path = paths[paths.index(',') + 2:-1]
      network[node] = (left_path, right_path)
   
   return network

def traverse_node(branches: tuple[str, str], instructions: str, step: int) -> str:
   instruction = instructions[step % len(instructions)]
   index = 0 if instruction == 'L' else 1
   return branches[index]

def count_steps(start: str, node_goal, network: dict, instructions: str) -> int:
   # Node goal should return a bool that's true when we've reached the end node.
   # This is so I can use the same function for parts 1 and 2 which have different "final node" criteria
   node = start
   steps = 0
   while not node_goal(node):
      node = traverse_node(network[node], instructions, steps)
      steps += 1

   return steps

def solve_part1(input: str) -> int:
   instructions, network_text = read_input(input)
   network = get_network(network_text)
   return count_steps('AAA', lambda n: n == 'ZZZ', network, instructions)

def solve_part2(input: str) -> int:
   instructions, network_text = read_input(input)
   network = get_network(network_text)
   node_goal = lambda n: n[-1] == 'Z'
   start_nodes = [node for node in network if node[-1] == 'A']
   steps = [count_steps(node, node_goal, network, instructions) for node in start_nodes]
   return math.lcm(*steps)

if __name__ == '__main__':
   filename = 'InputFiles\\Day8\\input.txt'
   print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))
   print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))
