import itertools
import sys

class Item:
    def __init__(self, cost, dmg, armor):
        self.cost = cost
        self.dmg = dmg
        self.armor = armor

class Unit:
    def __init__(self, hp, dmg, armor, items):
        self.hp = hp
        self.items = items
        self.dmg = dmg + sum(i.dmg for i in self.items)
        self.armor = armor + sum(i.armor for i in self.items)

    def take_dmg(self, amount):
        ''' returns true if kill '''
        self.hp = self.hp - max(1, amount - self.armor)
        return self.hp <= 0
        

weapons = [Item(8, 4, 0), Item(10, 5, 0), Item(25, 6, 0), Item(40, 7, 0), Item(74, 8, 0)]
armor = [Item(13, 0, 1), Item(31, 0, 2), Item(53, 0, 3), Item(75, 0, 4), Item(102, 0, 5)]
rings = [Item(25, 1, 0), Item(50, 2, 0), Item(100, 3, 0), Item(20, 0, 1), Item(40, 0, 2), Item(80, 0, 3)]

weapon_combos = itertools.combinations(weapons, 1)
armor_combos = list(itertools.combinations(armor, 0)) + list(itertools.combinations(armor, 1))
ring_combos = list(itertools.combinations(rings, 0)) + list(itertools.combinations(rings, 1)) + list(itertools.combinations(rings, 2))

all_item_combos = list(itertools.product(weapon_combos, armor_combos, ring_combos))
max_gold = -1

for ic in all_item_combos:
    player_items = [item for tup in ic for item in tup]
    cost = sum(item.cost for item in player_items)
    player = Unit(100, 0, 0, player_items)
    boss = Unit(100, 8, 2, [])

    while not (boss.take_dmg(player.dmg) or player.take_dmg(boss.dmg)):
        pass

    if player.hp <= 0:
        max_gold = max(max_gold, cost)

print(max_gold)