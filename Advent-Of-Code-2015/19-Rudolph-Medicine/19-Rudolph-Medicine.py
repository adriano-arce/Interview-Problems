from collections import deque


def neighbours(base, replacements):
    molecules = set()
    for before, after in replacements:
        for i in range(len(base)):
            if base[i : i + len(before)] == before:
                base_chars = list(base)
                base_chars[i : i + len(before)] = list(after)
                molecules.add(''.join(base_chars))
    return molecules


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

    # --------------------------------------------------------------------------
    # This uses a brute force BFS, but took too long.
    # --------------------------------------------------------------------------
    # start = 'e'
    # frontier = deque([(start, 0)])
    # found_target = False
    # i = 0
    # while frontier and not found_target:
    #     curr, dist = frontier.popleft()
    #     for neighbour in neighbours(curr, replacements):
    #         if i % 10000 == 0:
    #             print(i, neighbour, dist + 1)
    #         frontier.append((neighbour, dist + 1))
    #         if neighbour == target:
    #             found_target = True
    #         i += 1

    # --------------------------------------------------------------------------
    # This uses a brute force DFS in reverse, and happens to work quickly.
    # --------------------------------------------------------------------------
    start, target = target, 'e'
    for i in range(len(replacements)):
        before, after = replacements[i]
        replacements[i] = after, before

    frontier = deque([(start, 0)])
    steps = 0
    i = 0
    while frontier and not steps:
        curr, dist = frontier.pop()
        for neighbour in neighbours(curr, replacements):
            frontier.append((neighbour, dist + 1))
            if neighbour == target:  # Hopefully this is the fastest.
                steps = dist + 1
            i += 1

    print('The target can be reached in %d replacements.' % steps)

if __name__ == '__main__':
    main()
