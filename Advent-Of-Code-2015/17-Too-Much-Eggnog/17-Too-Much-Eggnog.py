from itertools import chain, combinations


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().strip().split('\n')
    target = 150

    containers = [int(row) for row in rows]
    total_count = 0
    min_count = -1
    min_len = len(containers) + 1
    for comb in chain.from_iterable(combinations(containers, k)
                                    for k in range(len(containers) + 1)):
        if sum(comb) == target:
            total_count += 1
            if len(comb) == min_len:
                min_count += 1
            elif len(comb) < min_len:
                min_len = len(comb)
                min_count = 1

    print('There are %d ways to fit all the eggnog.' % total_count)
    print('There are %d ways with min length (%d).' % (min_count, min_len))

if __name__ == '__main__':
    main()
