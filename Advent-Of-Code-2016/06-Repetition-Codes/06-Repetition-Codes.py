def part_one(rows):
    counters = tuple({} for _ in rows[0])
    for row in rows:
        for j, char in enumerate(row):
            counters[j][char] = counters[j].get(char, 0) + 1

    message = ''.join(max(counter, key=lambda c: counter[c])
                      for counter in counters)

    print('The error-corrected message is: %s.' % message)
    return counters


def part_two(counters):
    message = ''.join(min(counter, key=lambda c: counter[c])
                      for counter in counters)
    print('The original message is: %s.' % message)


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().split('\n')

    counters = part_one(rows)
    part_two(counters)

if __name__ == '__main__':
    main()
