def part_one(rows, dirs):
    grid = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    x, y = 1, 1
    code = []
    for row in rows:
        for instruction in row:
            dx, dy = dirs[instruction]
            x = min(len(grid[0]) - 1, max(0, x + dx))
            y = min(len(grid) - 1, max(0, y + dy))
            # print('CURR:', grid[x][y])
        code.append(grid[x][y])

    print('The part one code is: %s' % ''.join(map(str, code)))


def part_two(rows, dirs):
    grid = (
        (None, None, None, None, None, None, None),
        (None, None, None, '1', None, None, None),
        (None, None, '2', '3', '4', None, None),
        (None, '5', '6', '7', '8', '9', None),
        (None, None, 'A', 'B', 'C', None, None),
        (None, None, None, 'D', None, None, None),
        (None, None, None, None, None, None, None),
    )
    x, y = 3, 1
    code = []
    for row in rows:
        for instruction in row:
            dx, dy = dirs[instruction]
            if grid[x + dx][y + dy]:
                x, y = x + dx, y + dy
        code.append(grid[x][y])

    print('The part two code is: %s' % ''.join(map(str, code)))


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().split('\n')

    dirs = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
    part_one(rows, dirs)
    part_two(rows, dirs)

if __name__ == '__main__':
    main()
