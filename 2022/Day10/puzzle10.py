def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input 

def solve(input: str) -> int:
   commands = read_input(input)
   cycle = 1
   register = 1
   strength = 0
   line = ''
   for command in commands:
      parts = command.split()
      if parts[0] == 'addx':
         # addx is equivilent to "addx 0" + "addx V"
         add = [0, int(parts[1])]
      elif parts[0] == 'noop':
         # noop is equivilent to "addx 0"
         add = [0]
      
      for v in add:
         index = (cycle % 40) - 1
         if index in range(register - 1, register + 2):
            line += '#'
         else:
            line += '.'

         register += v
         cycle += 1
         if (cycle - 20) % 40 == 0:
            strength += (cycle * register)

         if cycle % 40 == 0:
            print(line)
            line = ''

   return strength

if __name__ == '__main__':
   filename = 'InputFiles\\puzzle10_input.txt'
   print(solve(filename))
