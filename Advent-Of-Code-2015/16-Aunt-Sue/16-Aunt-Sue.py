import re


def is_consistent(key, aunt_facts, ground_truth):
    if key in ('cats', 'trees'):
        return aunt_facts[key] > ground_truth[key]
    if key in ('pomeranians', 'goldfish'):
        return aunt_facts[key] < ground_truth[key]
    return aunt_facts[key] == ground_truth[key]


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().strip().split('\n')
    truth = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    sue_regex = re.compile(r'Sue (\d+): (.+)')
    all_aunt_facts = {}
    for row in rows:
        match = sue_regex.search(row)
        aunt, pairs = match.groups()
        aunt_facts = {}
        for pair in pairs.split(', '):
            key, value = pair.split(': ')
            aunt_facts[key] = int(value)

        all_aunt_facts[aunt] = aunt_facts

    for aunt, aunt_facts in all_aunt_facts.items():
        if all(aunt_facts[key] == truth[key] for key in aunt_facts):
            print('The gift came from aunt %s.' % aunt)

    for aunt, aunt_facts in all_aunt_facts.items():
        if all(is_consistent(key, aunt_facts, truth) for key in aunt_facts):
            print('With ranges, the gift came from aunt %s.' % aunt)


if __name__ == '__main__':
    main()
