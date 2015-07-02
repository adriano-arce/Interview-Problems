ROW_WIDTH = 80

# In clockwise order: up, right, down, left.
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
STOP, UP, RIGHT, DOWN, LEFT = -1, 0, 1, 2, 3
NUM_DIRS = len(DIRECTIONS)


def main():
    with open("test_snakes.txt") as f:
        snakes = f.read().split("\n" + "-" * ROW_WIDTH + "\n")
    for i, snake in enumerate(snakes):
        print("Test Snake #{}:".format(i + 1))
        print(snake)
        print("Unravelled: {}".format(unravel_snake(snake)))


def unravel_snake(snake):
    canvas = get_canvas(snake)
    pos = 0, 0
    dir_idx = RIGHT if move(pos, RIGHT) in canvas else DOWN
    words = []
    while dir_idx != STOP:
        pos, word = traverse_word(pos, dir_idx, canvas)
        words.append(word)
        dir_idx = next_dir(pos, dir_idx, canvas)
    return " ".join(words)


def get_canvas(snake):
    rows = snake.split("\n")
    canvas = {}
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char != " ":
                canvas[(x, y)] = char
    return canvas


def move(pos, dir_idx):
    x, y = pos
    dx, dy = DIRECTIONS[dir_idx]
    return x + dx, y + dy


def traverse_word(pos, dir_idx, canvas):
    chars = [canvas[pos]]
    next_pos = move(pos, dir_idx)
    while next_pos in canvas:
        pos, next_pos = next_pos, move(next_pos, dir_idx)
        chars.append(canvas[pos])
    return pos, "".join(chars)


def next_dir(pos, dir_idx, canvas):
    for turn in [-1, 1]:
        next_dir_idx = (dir_idx + turn) % NUM_DIRS
        if move(pos, next_dir_idx) in canvas:
            return next_dir_idx
    return STOP

if __name__ == "__main__":
    main()