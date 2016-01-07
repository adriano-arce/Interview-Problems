def neighbours(base, replacements):
    molecules = set()
    for before, after in replacements:
        for i in range(len(base)):
            if base[i : i + len(before)] == before:
                base_chars = list(base)
                base_chars[i : i + len(before)] = list(after)
                molecules.add(''.join(base_chars))
    return sorted(molecules)  # Makes the running time more consistent.


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().strip().split('\n')

    target = rows[-1]
    replacements = []
    for row in rows[:-2]:
        before, after = row.split(' => ')
        replacements.append((before, after))

    molecules = neighbours(target, replacements)
    print('There are %d possible molecules.' % len(molecules))

    start, target = target, 'e'
    for i in range(len(replacements)):
        before, after = replacements[i]
        replacements[i] = after, before

    frontier = [(start, 0)]
    steps = 0
    while frontier and not steps:
        curr, dist = frontier.pop()
        for neighbour in neighbours(curr, replacements):
            frontier.append((neighbour, dist + 1))
            if neighbour == target:  # Hopefully this path was unique.
                steps = dist + 1

    print('The target can be reached in %d replacements.' % steps)

if __name__ == '__main__':
    main()
