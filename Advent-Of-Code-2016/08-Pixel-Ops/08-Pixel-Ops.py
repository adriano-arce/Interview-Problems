import re


def rect_op(screen, w, h):
    for x in range(h):
        for y in range(w):
            screen[x][y] = True


def col_op(screen, col, offset):
    for _ in range(offset):
        temp = screen[-1][col]
        for x in range(len(screen) - 1, 0, -1):
            screen[x][col] = screen[x - 1][col]
        screen[0][col] = temp


def row_op(screen, row, offset):
    for _ in range(offset):
        temp = screen[row][-1]
        for y in range(len(screen[0]) - 1, 0, -1):
            screen[row][y] = screen[row][y - 1]
        screen[row][0] = temp


def part_one(instructions, width, height):
    regex_dict = {
        re.compile(r"rect (\d+)x(\d+)"): rect_op,
        re.compile(r"rotate column x=(\d+) by (\d+)"): col_op,
        re.compile(r"rotate row y=(\d+) by (\d+)"): row_op
    }
    screen = [[False] * width for _ in range(height)]
    for instruction in instructions:
        for regex, op in regex_dict.items():
            match = regex.match(instruction)
            if match:
                op(screen, *map(int, match.groups()))
                # print('\n'.join(''.join('#' if r else '.' for r in rows)
                #                 for rows in screen))
                # print()
                break

    total_lit = sum(sum(rows) for rows in screen)
    print('The total number of lit pixels is: %d' % total_lit)

    return screen


def part_two(screen):
    print('The screen is:')
    print('\n'.join(''.join('#' if r else '.' for r in rows)
                    for rows in screen))


def main():
    with open('input.txt', 'r') as f:
        instructions = f.read().split('\n')
    width, height = 50, 6

    screen = part_one(instructions, width, height)
    part_two(screen)

if __name__ == '__main__':
    main()
