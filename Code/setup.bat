@echo off

set /p day=Enter day: 

set current_path=%cd%
set destination_folder=%current_path%\Day%day%
set destination_file=%destination_folder%\puzzle%day%.py
set template_file=%current_path%\template.py

if not exist %destination_folder% mkdir %destination_folder% & echo Directory created.

echo def read_input(file: str):> %template_file%
echo    with open(file) as f:>> %template_file%
echo       input = f.read().splitlines()>> %template_file%
echo:>> %template_file%
echo    return input>> %template_file%
echo:>> %template_file%
echo def solve_part1(input: str) -^> int:>> %template_file%
echo    pass>> %template_file%
echo:>> %template_file%
echo def solve_part2(input: str) -^> int:>> %template_file%
echo    pass>> %template_file%
echo:>> %template_file%
echo if __name__ == '__main__':>> %template_file%
echo    filename = 'InputFiles\\puzzle%day%_test.txt'>> %template_file%
echo    print(solve_part1(filename))>> %template_file%
echo    print(solve_part2(filename))>> %template_file%

copy %template_file% %destination_file% /-Y
del %template_file%