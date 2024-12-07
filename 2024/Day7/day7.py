with open('Day7/input.txt') as f:
    equations = f.readlines()

for operators in [['+', '*'] ,['+', '*', '||']]:
    score = 0
    for equation in equations:
        answer, parts = equation.split(': ')
        values = list(map(int, parts.split()))
        answer = int(answer)

        stack = [(1, values[0])]
        while stack:
            index, total = stack.pop()
            if index == len(values):
                if total == answer:
                    score += answer
                    break
                else:
                    continue

            for operator in operators:
                if operator == '+':
                    new_total = total + values[index]
                elif operator == '*':
                    new_total = total * values[index]
                elif operator == '||':
                    new_total = int(f'{total}{values[index]}')
                stack.append((index + 1, new_total))

    print(score)