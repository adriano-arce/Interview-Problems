import re


def mistranslated(rules):
    rule_regex = re.compile(r'(.+) (\d+),(\d+) through (\d+),(\d+)')
    grid = [[False] * 1000 for _ in range(1000)]
    for rule in rules:
        match = rule_regex.search(rule)
        action, x1, y1, x2, y2 = match.groups()
        for x in range(int(x1), int(x2) + 1):
            for y in range(int(y1), int(y2) + 1):
                if action == 'turn on':
                    grid[x][y] = True
                elif action == 'toggle':
                    grid[x][y] = not grid[x][y]
                else:
                    grid[x][y] = False

    print('There are %d lights that are lit.' % sum(sum(row) for row in grid))


def translated(rules):
    rule_regex = re.compile(r'(.+) (\d+),(\d+) through (\d+),(\d+)')
    grid = [[0] * 1000 for _ in range(1000)]
    for rule in rules:
        match = rule_regex.search(rule)
        action, x1, y1, x2, y2 = match.groups()
        for x in range(int(x1), int(x2) + 1):
            for y in range(int(y1), int(y2) + 1):
                if action == 'turn on':
                    grid[x][y] += 1
                elif action == 'toggle':
                    grid[x][y] += 2
                else:
                    grid[x][y] = max(0, grid[x][y] - 1)

    print('The total brightness is %d.' % sum(sum(row) for row in grid))


def main():
    with open('input.txt', 'r') as f:
        rules = f.read().split('\n')

    mistranslated(rules)
    translated(rules)


if __name__ == '__main__':
    main()
