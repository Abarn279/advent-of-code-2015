import itertools
import sys
from enum import Enum
from searches import astar
from collections import deque

class DamageType(Enum):
    PHYSICAL = 0
    MAGIC = 1

class Spell(Enum):
    MAGIC_MISSLE = 53
    DRAIN = 73
    SHIELD = 113
    POISON = 173
    RECHARGE = 229

    def __lt__(self, other):
        return False

class CombatResult:
    def __init__(self, wizardwon, bosshp, wizardmana, wizardhp, spellsunused):
        self.wizardwon = wizardwon
        self.bosshp = bosshp
        self.mana_used = wizardmana
        self.wizardhp = wizardhp
        self.spellsunused = spellsunused

class Item:
    def __init__(self, cost, dmg, armor):
        self.cost = cost
        self.dmg = dmg
        self.armor = armor

class Unit:
    def __init__(self, hp, dmg, armor, mana):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor
        self.mana = mana
        self.mana_used = 0

        self.shield_effect_timer = 0
        self.poison_effect_timer = 0
        self.recharge_effect_timer = 0

    def apply_effects(self):
        ''' run before every player and every boss turn '''
        if self.shield_effect_timer == 0:
            self.armor = 0
        self.shield_effect_timer -= 1
        
        if self.poison_effect_timer > 0:
            self.hp -= 3
        self.poison_effect_timer -= 1
        
        if self.recharge_effect_timer > 0:
            self.mana += 101
        self.recharge_effect_timer -= 1

    def take_dmg(self, amount, d_type: DamageType):
        ''' returns true if kill '''
        if d_type == DamageType.PHYSICAL:
            self.hp = self.hp - max(1, amount - self.armor)
        else: 
            self.hp = self.hp - amount
        return self.hp <= 0

    def attack(self, unit):
        unit.take_dmg(self.dmg, DamageType.PHYSICAL)

    def use_mana(self, amt):
        if amt > self.mana: raise Exception("Can't cast!")
        self.mana -= amt
        self.mana_used += amt

    def cast(self, spell: Spell, unit):
        if spell == Spell.MAGIC_MISSLE:
            self.use_mana(spell.value)
            unit.take_dmg(4, DamageType.MAGIC)
        elif spell == Spell.DRAIN:
            self.use_mana(spell.value)
            unit.take_dmg(2, DamageType.MAGIC)
            self.hp += 2
        elif spell == Spell.SHIELD:
            if self.shield_effect_timer > 0: raise Exception()
            self.use_mana(spell.value)
            self.armor = 7
            self.shield_effect_timer = 6
        elif spell == Spell.POISON:
            if unit.poison_effect_timer > 0: raise Exception()
            self.use_mana(spell.value)
            unit.poison_effect_timer = 6
        elif spell == Spell.RECHARGE:
            if self.recharge_effect_timer > 0: raise Exception()
            self.use_mana(spell.value)
            self.recharge_effect_timer = 5

def simulate_combat(spells):
    wizard = Unit(50, 0, 0, 500)
    boss = Unit(58, 9, 0, 0)
    spell_queue = deque(spells)

    while wizard.hp > 0 and boss.hp > 0:
        # wizard turn
        wizard.apply_effects()
        boss.apply_effects()
        if boss.hp <= 0 or wizard.hp <= 0: break

        if len(spell_queue) > 0:
            try: 
                wizard.cast(spell_queue.popleft(), boss)
            except:
                break

        # boss turn
        wizard.apply_effects()
        boss.apply_effects()
        if boss.hp <= 0 or wizard.hp <= 0: break
        boss.attack(wizard)

    return CombatResult(True if wizard.hp > 0 and boss.hp <= 0 else False, boss.hp, wizard.mana_used, wizard.hp, len(spell_queue))

def is_goal_fn(spells):
    try: 
        c = simulate_combat(spells)
        if c.wizardwon: 
            print(spells)
        return c.wizardwon
    except:
        return False

def heuristic_fn(spells):
    cr = simulate_combat(spells)
    return cr.bosshp * 9

def cost_fn(spells1, spells2):
    return simulate_combat(spells2).mana_used - simulate_combat(spells1).mana_used

def get_neighbors_fn(spells):
    neighbors = []

    cr = simulate_combat(spells)
    
    if not cr.wizardwon and cr.spellsunused > 0: # if we're dying with spells unused then don't keep going down this path
        return neighbors

    for s in [Spell.MAGIC_MISSLE, Spell.DRAIN, Spell.SHIELD, Spell.POISON, Spell.RECHARGE]:
        if s in [Spell.SHIELD, Spell.POISON, Spell.RECHARGE]:
            if len(spells) > 2 and (spells[-1] == s or spells[-2] == s):
                continue

        neighbors.append(spells + (s,))
    
    return neighbors

start = tuple()

# A* nodes are tuples of spells that the player will cast
mana = astar(
    start = start,
    is_goal_fn = is_goal_fn,
    heuristic_fn = heuristic_fn,
    cost_fn = cost_fn,
    get_neighbors_fn = get_neighbors_fn,
    get_key_fn = lambda s: s
)

print(mana)