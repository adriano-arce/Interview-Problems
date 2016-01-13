import heapq
from copy import deepcopy


class Spell(object):
    mana_cost = 0

    def try_cast(self, world):
        """Try to cast this spell to modify the state of the world in-place.

        Args:
            world (World):
                The state of the world before casting this spell.

        Returns:
            bool: Whether or not this spell was successfully cast.
        """
        if world.hero_mana < self.mana_cost:
            return False

        world.hero_mana -= self.mana_cost
        return True

    def __repr__(self):
        return type(self).__name__


class MagicMissile(Spell):
    mana_cost = 53

    def try_cast(self, world):
        if not super(MagicMissile, self).try_cast(world):
            return False

        world.boss_hp -= 4
        return True


class Drain(Spell):
    mana_cost = 73

    def try_cast(self, world):
        if not super(Drain, self).try_cast(world):
            return False

        world.boss_hp -= 2
        world.hero_hp += 2
        return True


class Shield(Spell):
    mana_cost = 113

    def try_cast(self, world):
        if world.arm_timer > 0 or not super(Shield, self).try_cast(world):
            return False

        world.arm_timer = 6
        return True


class Poison(Spell):
    mana_cost = 173

    def try_cast(self, world):
        if world.poison_timer > 0 or not super(Poison, self).try_cast(world):
            return False

        world.poison_timer = 6
        return True


class Recharge(Spell):
    mana_cost = 229

    def try_cast(self, world):
        if (world.recharge_timer > 0 or
                not super(Recharge, self).try_cast(world)):
            return False

        world.recharge_timer = 5
        return True


all_spells = (Recharge(), Shield(), Poison(), Drain(), MagicMissile())


class World(object):
    def __init__(self, boss_hp, boss_dmg, hero_hp, hero_mana):
        self.boss_hp = boss_hp
        self.boss_dmg = boss_dmg
        self.hero_hp = hero_hp
        self.hero_mana = hero_mana

        self.hero_arm = 0
        self.arm_timer = 0
        self.poison_timer = 0
        self.recharge_timer = 0
        self.spells_used = []

    def __lt__(self, other):
        return id(self) < id(other)

    def boss_dead(self):
        return self.boss_hp <= 0

    def get_new_worlds(self):
        new_worlds = []
        for spell in all_spells:
            new_world = self.simulate_round(spell)
            if new_world and new_world.hero_hp > 0:
                new_worlds.append(new_world)
        return new_worlds

    def simulate_round(self, spell):
        """Simulate one round (one hero turn and one boss turn).

        Args:
            spell (Spell):
                The spell to be cast by the hero.

        Returns:
            World: The new state of the world after one round.
        """
        new_world = deepcopy(self)

        # ----------------------------------------------------------------------
        # Part Two
        # ----------------------------------------------------------------------
        new_world.hero_hp -= 1
        if new_world.hero_hp <= 0:
            return None

        # Hero's turn.
        new_world.apply_effects()
        if not spell.try_cast(new_world):
            return None
        new_world.spells_used.append(spell)

        # print('> From %s, casting %12s... [%2d, %2d]' %
        #       (self.spells_used[-1] if self.spells_used else 'None',
        #        spell, new_world.hero_hp, new_world.boss_hp))

        # Boss' turn.
        if new_world.boss_dead():
            return new_world

        new_world.apply_effects()
        if new_world.boss_dead():
            return new_world

        new_world.hero_hp -= max(new_world.boss_dmg - new_world.hero_arm, 1)

        return new_world

    def apply_effects(self):
        """Apply any effects."""
        if self.arm_timer > 0:
            self.arm_timer -= 1
            self.hero_arm = 7
        else:
            self.hero_arm = 0

        if self.poison_timer > 0:
            self.boss_hp -= 3
            self.poison_timer -= 1

        if self.recharge_timer > 0:
            self.hero_mana += 101
            self.recharge_timer -= 1


class PriorityQueue(object):
    def __init__(self):
        self._heap = []

    def __bool__(self):
        return bool(self._heap)

    def put(self, item, priority):
        heapq.heappush(self._heap, (priority, item))

    def get(self):
        return heapq.heappop(self._heap)[1]


def heuristic(world, other_world):
    """Returns the estimated mana cost from world to other_world.

    Args:
        world (World):
            The current state of the world.

        other_world (World):
            The next state of the world.

    Returns:
        float: The estimated mana cost from world to other_world.
    """
    score = other_world.hero_hp

    # score += 100 * (other_world.hero_hp - world.hero_hp)
    # score += 1 * (world.boss_hp - other_world.hero_hp)
    # if other_world.recharge_timer > 0:
    #     score += 10
    # if other_world.poison_timer > 0:
    #     score += 20
    # if other_world.arm_timer > 0:
    #     score += 40

    ratio = 1 / max(score, 1)
    return ratio * MagicMissile.mana_cost

    # spell_map = {
    #     'Poison': 100,
    #     'Recharge': 100,
    #     'Shield': 100,
    #     'Drain': 100,
    #     'MagicMissile': 0,
    # }
    # ratio = 1 / max(spell_map[str(other_world.spells_used[-1])], 1)
    # return ratio * MagicMissile.mana_cost


def find_goal_world(world):
    """Find the goal world.

    Args:
        world (World): The initial state of the world.

    Returns:
        World: The goal world, if reachable.
    """
    frontier = PriorityQueue()
    frontier.put(world, 0)
    cost_so_far = {world: 0}
    while frontier:
        world = frontier.get()

        print('[%d]: %s(%2d HP, %d armor, %3d mana) vs. (%2d HP) %s' %
              (cost_so_far[world], ' ' * len(world.spells_used),
               world.hero_hp, world.hero_arm, world.hero_mana, world.boss_hp,
               world.spells_used))

        if world.boss_dead():
            return world, cost_so_far[world]

        for other_world in world.get_new_worlds():
            other_cost = (cost_so_far[world] +
                          other_world.spells_used[-1].mana_cost)
            if other_cost < cost_so_far.get(other_world, float('inf')):
                cost_so_far[other_world] = other_cost
                priority = other_cost + heuristic(world, other_world)
                frontier.put(other_world, priority)

    print('Something went terribly wrong.')
    return world, cost_so_far[world]


def main():
    world = World(71, 10, 50, 500)
    # world = World(13, 8, 10, 250)
    # world = World(14, 8, 10, 250)

    goal_world, total_cost = find_goal_world(world)
    if goal_world:
        print('Mana spent: %d' % total_cost)
        print('Spells used:', goal_world.spells_used)

    # Mana spent: 1824
    # Spells used: [Poison, Recharge, Shield, Poison, Recharge, Shield, Poison,
    #               Recharge, Shield, MagicMissile, Poison, MagicMissile]

    # Mana spent: 1937
    # Spells used: [Shield, Recharge, Poison, Shield, Recharge, Poison, Shield,
    #               Recharge, Poison, Shield, MagicMissile, Poison,
    #               MagicMissile]



if __name__ == '__main__':
    main()
