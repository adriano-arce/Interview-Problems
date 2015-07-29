import copy


def paint_fill(grid, x, y, new_colour):
    """
    Paint fills position (x, y) in the grid with new_colour.

    This uses an iterative DFS (the frontier is a filtered stack).
    """
    old_colour = grid[x][y]
    frontier = []
    add(x, y, frontier, grid, old_colour)
    while frontier:
        x, y = frontier.pop()
        if grid[x][y] != new_colour:
            grid[x][y] = new_colour
            add(x - 1, y, frontier, grid, old_colour)
            add(x, y - 1, frontier, grid, old_colour)
            add(x + 1, y, frontier, grid, old_colour)
            add(x, y + 1, frontier, grid, old_colour)


def add(x, y, frontier, grid, old_colour):
    """
    Adds the expanded position to the frontier, provided that it's valid.
    """
    m, n = len(grid), len(grid[0])
    if 0 <= x < m and 0 <= y < n and grid[x][y] == old_colour:
        frontier.append((x, y))


def main():
    original_grid = [
        list("xxxxxxxxxxxxxxxxxxxzzxx"),
        list("xxxxooooooooooooooxxxxx"),
        list("xxxzzzooooooooooooooooo"),
        list("xxxxoxxxxxxxxxxzzzxxoxx"),
        list("xxxxoxxxxxxxxxxxxxxxoxx"),
        list("xxxxoxxxxxxxxxxxxxxxoxx"),
        list("xxxooooxxxxxxxxxxxxoooo")
    ]
    test_inputs = [
        (0, 0, "x"),
        (0, 0, "o"),
        (1, 4, "x"),
        (1, 4, "o"),
        (1, 4, "z"),
        (2, 4, "x"),
        (2, 4, "o"),
        (2, 4, "z")
    ]
    for i, test_input in enumerate(test_inputs):
        print("Test Case #{}: {}".format(i + 1, test_input))
        grid = copy.deepcopy(original_grid)
        paint_fill(grid, *test_input)
        print("\n".join("".join(row) for row in grid))

if __name__ == "__main__":
    main()