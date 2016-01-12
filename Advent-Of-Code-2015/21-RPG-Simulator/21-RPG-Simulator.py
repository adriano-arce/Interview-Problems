from itertools import product, combinations, chain


def fight(hero, boss):
    hero_hp, hero_dmg, hero_arm = hero
    boss_hp, boss_dmg, boss_arm = boss
    hero_turn = True
    while hero_hp > 0 and boss_hp > 0:
        if hero_turn:
            boss_hp -= max(hero_dmg - boss_arm, 1)
        else:
            hero_hp -= max(boss_dmg - hero_arm, 1)
        hero_turn = not hero_turn
    return hero_hp > 0


def main():
    weapons = [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0),
    ]
    armor_list = [
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5),
    ]
    ring_list = [
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    ]
    boss = (103, 9, 2)
    hero_hp = 100
    inventories = product(
        combinations(weapons, 1),
        chain.from_iterable(combinations(armor_list, k) for k in (0, 1)),
        chain.from_iterable(combinations(ring_list, k) for k in (0, 1, 2))
    )

    min_cost_and_win = float('inf')
    max_cost_and_lose = float('-inf')
    for i, inventory in enumerate(inventories):
        curr = filter(None, inventory)  # Filter out empty tuples.
        curr = chain(*curr)             # Flatten tuple of tuples.
        curr = zip(*curr)               # Group the row vectors by column.
        curr = map(sum, curr)           # Compute each column sum.
        cost, damage, armor = curr      # Reify and unpack.
        hero = (hero_hp, damage, armor)
        if cost < min_cost_and_win and fight(hero, boss):
            min_cost_and_win = cost
        if cost > max_cost_and_lose and not fight(hero, boss):
            max_cost_and_lose = cost

    print('The least gold to win is: %d.' % min_cost_and_win)
    print('The most gold to lose is: %d.' % max_cost_and_lose)


if __name__ == '__main__':
    main()
