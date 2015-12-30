def this_year(directions):
    curr = (0, 0)
    delivered = {curr}
    for direction in directions:
        if direction == '^':
            curr = curr[0], curr[1] + 1
        elif direction == 'v':
            curr = curr[0], curr[1] - 1
        elif direction == '>':
            curr = curr[0] + 1, curr[1]
        elif direction == '<':
            curr = curr[0] - 1, curr[1]
        else:
            print('ERROR: Unrecognized direction %s' % direction)

        delivered.add(curr)

    return delivered

def next_year(directions):
    delivered = this_year(directions[::2])
    delivered.update(this_year(directions[1::2]))

    return delivered

def main():
    with open('input.txt', 'r') as f:
        directions = f.read().strip()

    this_year_count = len(this_year(directions))
    print('This year, %d houses received a present.' % this_year_count)

    next_year_count = len(next_year(directions))
    print('Next year, %d houses will receive a present.' % next_year_count)

if __name__ == '__main__':
    main()