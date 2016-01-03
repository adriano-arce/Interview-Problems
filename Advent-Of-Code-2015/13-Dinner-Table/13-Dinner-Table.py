import re
from itertools import permutations


def max_change(people, happiness):
    largest_change = float('-Inf')

    for perm in permutations(people):
        change = happiness[perm[-1]][perm[0]]
        for i in range(len(perm) - 1):
            change += happiness[perm[i]][perm[i + 1]]
        if change > largest_change:
            largest_change = change

    return largest_change


def main():
    with open('input.txt') as f:
        rows = f.read().split('\n')

    happy_regex = re.compile(r'(\S+) would (gain|lose) (\d+).* (\S+).')
    happiness = {}
    for row in rows:
        match = happy_regex.search(row)
        person, sign, units, other = match.groups()
        change = int(units) if sign == 'gain' else -int(units)
        if person in happiness:
            happiness[person][other] = happiness[person].get(other, 0) + change
        else:
            happiness[person] = {other: change}
        if other in happiness:
            happiness[other][person] = happiness[other].get(person, 0) + change
        else:
            happiness[other] = {person: change}

    people = list(happiness)

    largest_change = max_change(people, happiness)
    print('The largest change in happiness is: %d.' % largest_change)

    me = 'me'
    happiness[me] = {other: 0 for other in people}
    for other in people:
        happiness[other][me] = 0
    people.append(me)

    largest_change = max_change(people, happiness)
    print('With me, the largest change in happiness is: %d.' % largest_change)


if __name__ == '__main__':
    main()
