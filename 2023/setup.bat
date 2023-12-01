@echo off

set /p day=Enter day: 

set current_path=%cd%
set destination_folder=%current_path%\Day%day%
set destination_file=%destination_folder%\day%day%.py
set template_file=%current_path%\template.py
set file_folder=%current_path%\InputFiles\Day%day%
set test_file=%file_folder%\test.txt
set input_file=%file_folder%\input.txt

if not exist %destination_folder% mkdir %destination_folder% & echo Script directory created.

echo import timeit>> %template_file%
echo:>> %template_file%
echo def read_input(file: str):>> %template_file%
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
echo    filename = 'InputFiles\\Day%day%\\test.txt'>> %template_file%
echo    print(timeit.timeit(lambda: print(solve_part1(filename)), number=1))>> %template_file%
echo    print(timeit.timeit(lambda: print(solve_part2(filename)), number=1))>> %template_file%

copy %template_file% %destination_file% /-Y
del %template_file%

if not exist %file_folder% mkdir %file_folder% & echo File directory created.
copy /y nul %test_file%
copy /y nul %input_file%