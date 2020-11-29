from file_importer import FileImporter
import re

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)

ingredient_strings = '''Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8'''.split('\n')
ing = []

for r in ingredient_strings:
    r = re.match('(\w+): capacity (-?\d), durability (-?\d), flavor (-?\d), texture (-?\d), calories (-?\d)', r)
    ing.append(Ingredient(*r.groups()))

mx = 0
for i1 in range(1, 101):
    for i2 in range(1, 101 - i1):
        for i3 in range(1, 101 - i1 - i2):
            for i4 in range(1, 101 - i1 - i2 - i3):
                if i1 + i2 + i3 + i4 != 100: continue

                cap = max(0, i1 * ing[0].capacity + i2 * ing[1].capacity + i3 * ing[2].capacity + i4 * ing[3].capacity)
                dur = max(0, i1 * ing[0].durability + i2 * ing[1].durability + i3 * ing[2].durability + i4 * ing[3].durability)
                flv = max(0, i1 * ing[0].flavor + i2 * ing[1].flavor + i3 * ing[2].flavor + i4 * ing[3].flavor)
                tex = max(0, i1 * ing[0].texture + i2 * ing[1].texture + i3 * ing[2].texture + i4 * ing[3].texture)

                total = cap * dur * flv * tex
                mx = max(total, mx)

print(mx)
