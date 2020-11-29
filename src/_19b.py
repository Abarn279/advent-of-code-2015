from collections import deque
from searches import astar

class Replacement:
    def __init__(self, inp, outp):
        self.inp = inp
        self.outp = outp
    def __str__(self):
        return f'{self.inp} => {self.outp}'
    def __repr__(self):
        return self.__str__()

reactions = '''Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg'''

goal = 'e'
initial = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'

reactions = reactions.split('\n')
reactions = list(map(lambda x: Replacement(*x.split(' => ')), reactions))

# needed for heuristic. this is the maximum distances a string can change in one replacement.
max_char_change = max(len(i.outp) - len(i.inp) for i in reactions)

def is_goal_fn(n):
    return len(n) == 1 and n == goal # O(1) for most with length check first

def heuristic_fn(n):
    return len(n)

def cost_fn(a, b): 
    return 1

def get_neighbors_fn(n):
    neighbors = []

    for r in reactions:
        for i in range(len(n)):
            if n[i:i + len(r.outp)] == r.outp:
                new_str = n[:i] + r.inp + n[i+len(r.outp):]
                neighbors.append(new_str)

    return neighbors

steps = astar(
    start = initial,
    is_goal_fn = is_goal_fn,
    heuristic_fn = heuristic_fn,
    cost_fn = cost_fn,
    get_neighbors_fn = get_neighbors_fn,
    get_key_fn = lambda x: x
)

print(steps)
