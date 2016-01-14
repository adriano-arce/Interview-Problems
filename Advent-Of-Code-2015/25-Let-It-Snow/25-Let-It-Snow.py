def generate(prev):
    return (252533 * prev) % 33554393


def next_pair(prev_row, prev_col):
    if prev_row > 1:
        return prev_row - 1, prev_col + 1
    else:
        return prev_col + 1, 1


def main():
    target_row, target_col = 2981, 3075
    max_row, max_col = target_row + target_col - 1, target_row + target_col - 1
    grid = [[-1] * (max_col + 1) for _ in range(max_row + 1)]
    grid[1][1] = 20151125
    prev_row, prev_col = 1, 1
    row, col = 2, 1
    while row <= max_row and col <= max_col:
        grid[row][col] = generate(grid[prev_row][prev_col])
        # print(row, col, grid[row][col])
        prev_row, prev_col = row, col
        row, col = next_pair(row, col)

    print('The number at row %d and col %d is: %d.' %
          (target_row, target_col, grid[target_row][target_col]))

if __name__ == '__main__':
    main()
