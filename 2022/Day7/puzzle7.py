def read_input(file: str):
   with open(file) as f:
      input = f.read().splitlines()

   return input 

def create_file_structure(commands: list[str]) -> dict:
   # Start in '/' folder
   files = {'/': dict()}
   current_dir = files
   parent_folders = []
   
   for command in commands:
      # We can ignore '$ ls'
      if command.startswith('$ cd'):
         new_dir = command.split()[-1]
         if new_dir == '..':
            parent_folders.pop()
            dir = files
            # Navigate from the top to the last directory
            # Probably a better way to do this
            for f in parent_folders:
               dir = dir[f]
            
            current_dir = dir
         else:
            parent_folders.append(new_dir)
            current_dir = current_dir[new_dir]

      elif command.startswith('$') == False:
         parts = command.split()

         if parts[0] == 'dir':
            # Add directory
            if parts[1] not in current_dir:
               current_dir[parts[1]] = dict()
         else:
            # Add file
            current_dir[parts[1]] = int(parts[0])
   
   return files

def get_folder_sizes(folder: str, structure: dict, folders: dict) -> tuple:
   # Recursive fun :)
   size = 0
   for item in structure:
      if isinstance(structure[item], int):
         size += structure[item]
      elif isinstance(structure[item], dict):
         folders, item_size = get_folder_sizes(item, structure[item], folders)
         # We have to return the size along with the updated dictionary because there may be multiple directories with same name
         size += item_size
   
   # Give unique name
   i = 0
   while folder in folders:
      folder = f'{folder}i'
      i += 1

   folders[folder] = size
   
   return (folders, size)

def solve_part1(input: str) -> int:
   commands = read_input(input)
   files = create_file_structure(commands)

   sizes = get_folder_sizes('/', files['/'], dict())[0]
   return sum((sizes[folder] for folder in sizes if sizes[folder] <= 100000))

def solve_part2(input: str) -> int:
   commands = read_input(input)
   files = create_file_structure(commands)

   sizes = get_folder_sizes('/', files['/'], dict())[0]
   unused_space = 70000000 - sizes['/']
   return min((sizes[folder] for folder in sizes if unused_space + sizes[folder] >= 30000000))

if __name__ == '__main__':
   filename = 'InputFiles\\puzzle7_input.txt'
   print(solve_part1(filename))
   print(solve_part2(filename))
