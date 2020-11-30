import itertools
import sys

def prod(ary):
    sm = ary[0]
    for i in range(1, len(ary)):
        sm *= ary[i]
    return sm

original = set(map(int, '''1
2
3
7
11
13
17
19
23
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113'''.split('\n')))

start_size = 4
other_min = start_size
weight = sum(original) // 4

qe = set()
mn = sys.maxsize

combinations_group1 = itertools.combinations(original, start_size)

for combo_g1 in combinations_group1:
    if sum(combo_g1) != weight:
        continue

    remaining = original.difference(set(combo_g1))

    for g2_size in range(other_min, len(remaining) - other_min):
        combinations_group2 = itertools.combinations(remaining, g2_size)

        for combo_g2 in combinations_group2:
            if sum(combo_g2) != weight:
                continue

            remaining_after_2 = remaining.difference(set(combo_g2))

            for g3_size in range(other_min, len(remaining_after_2) - other_min):
                combinations_group3 = itertools.combinations(remaining_after_2, g3_size)

                for combo_g3 in combinations_group3:
                    if (sum(combo_g3)) != weight:
                        continue

                    combo_g4 = remaining_after_2.difference(combo_g3)
                    
                    if sum(combo_g1) == sum(combo_g2) == sum(combo_g3) == sum(combo_g4):
                        qe.add(prod(list(combo_g1)))
                        if list(sorted(qe))[0] < mn:
                            mn = list(sorted(qe))[0]
                            print(mn)
