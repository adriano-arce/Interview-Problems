def part_one(rows):
    valid_count = 0
    for row in rows:
        a, b, c = sorted(row)
        if a + b > c:
            valid_count += 1

    print('In part one, there are a total of %d valid triangles.' % valid_count)


def part_two(rows):
    valid_count = 0
    for i in range(0, len(rows), 3):
        for j in range(3):
            a, b, c = sorted((rows[i][j], rows[i+1][j], rows[i+2][j]))
            if a + b > c:
                valid_count += 1

    print('In part two, there are a total of %d valid triangles.' % valid_count)


def main():
    with open('input.txt', 'r') as f:
        raw_rows = f.read().split('\n')

    rows = [list(map(int, raw_row.split())) for raw_row in raw_rows]
    part_one(rows)
    part_two(rows)

if __name__ == '__main__':
    main()
