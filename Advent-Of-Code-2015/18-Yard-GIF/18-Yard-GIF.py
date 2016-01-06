def on_neighbours(grid, x, y):
    m, n = len(grid), len(grid[0])
    count = 0
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
               (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in offsets:
        if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy]:
            count += 1

    return count


def next_grid(old_grid, with_corners=False):
    m, n = len(old_grid), len(old_grid[0])
    grid = [list(row) for row in old_grid]
    corners = ((0, 0), (0, n - 1), (m - 1, 0), (m - 1, n - 1))

    for i in range(m):
        for j in range(n):
            if with_corners and (i, j) in corners:
                grid[i][j] = True
            elif old_grid[i][j]:
                grid[i][j] = on_neighbours(old_grid, i, j) in (2, 3)
            else:
                grid[i][j] = on_neighbours(old_grid, i, j) == 3

    return grid


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().strip().split('\n')

    init_grid = [[c == '#' for c in row] for row in rows]

    grid = [list(row) for row in init_grid]
    for i in range(100):
        grid = next_grid(grid)

    on_count = sum(sum(row) for row in grid)
    print('After 100 steps, there are %d lights on.' % on_count)

    grid = [list(row) for row in init_grid]
    for i in range(100):
        grid = next_grid(grid, True)

    on_count = sum(sum(row) for row in grid)
    print('After 100 steps (with corners), there are %d lights on.' % on_count)


if __name__ == '__main__':
    main()
