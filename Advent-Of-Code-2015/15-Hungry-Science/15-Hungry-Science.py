from itertools import combinations_with_replacement


def find_max(ingredients, with_calories=False):
    max_product = 0
    for comb in combinations_with_replacement(ingredients, 100):
        total = tuple(map(sum, zip(*comb)))

        product = 1
        for prop in total[:-1]:
            if prop <= 0 or (with_calories and total[-1] != 500):
                product = 0
            else:
                product *= prop

        max_product = max(max_product, product)
    return max_product


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().split('\n')

    ingredients = []
    for row in rows:
        _, right = row.split(': ')
        ingredients.append(tuple(int(prop.split()[1])
                                 for prop in right.split(', ')))

    max_product = find_max(ingredients)
    print('Without calories, the max product is: %d.' % max_product)

    max_product = find_max(ingredients, True)
    print('With calories, the max product is: %d.' % max_product)


if __name__ == '__main__':
    main()
