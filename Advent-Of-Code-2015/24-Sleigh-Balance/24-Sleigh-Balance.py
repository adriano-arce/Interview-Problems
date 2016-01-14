from itertools import combinations, chain


def get_targets(pool, target):
    targets = filter(lambda c: sum(c) == target,
                     chain.from_iterable(combinations(pool, k)
                                         for k in range(len(pool))))
    return sorted(targets, key=len)


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().strip().split('\n')
    weights = {int(row) for row in rows}

    # target = sum(weights) // 3
    target = sum(weights) // 4

    print('Getting targets...')
    targets = get_targets(weights, target)
    print('Found %d targets.' % len(targets))

    # candidates, min_length = set(), float('inf')
    # for i, (first, second) in enumerate(combinations(target_list, 2)):
    #     if first not in candidates and len(set(first) & set(second)) == 0:
    #         print('[%d]: %s' % (i + 1, first))
    #         if len(first) < min_length:
    #             candidates, min_length = {first}, len(first)
    #         elif len(first) == min_length:
    #             candidates.add(first)
    #         else:
    #             break

    candidates, min_length = set(), float('inf')
    for i, first in enumerate(targets):
        if len(first) > min_length:
            break
        if first not in candidates:
            for second, third in combinations(targets[i + 1:], 2):
                if len(set(first) & set(second) & set(third)) == 0:
                    print('[%d]: %s' % (i + 1, first))
                    if len(first) < min_length:
                        candidates, min_length = {first}, len(first)
                    elif len(first) == min_length:
                        candidates.add(first)
                    break

    best_candidate, min_quantum_entanglement = None, float('inf')
    for candidate in candidates:
        product = 1
        for weight in candidate:
            product *= weight
        if product < min_quantum_entanglement:
            best_candidate, min_quantum_entanglement = candidate, product

    print('The best group is %s (QE=%d).' %
          (best_candidate, min_quantum_entanglement))


if __name__ == '__main__':
    main()
