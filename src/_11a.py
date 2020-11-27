import string
nxtmap = {i: chr(ord(i) + 1) for i in string.ascii_lowercase}
nxtmap['z'] = 'a'
not_allowed = set(['i', 'o', 'l'])

def three_repeating(s):
    return ord(s[1]) - ord(s[0]) == 1 and ord(s[2]) - ord(s[1]) == 1

def is_valid(s):
    global not_allowed

    valid = False
    num_pairs = 0
    last_pair_ind = -1
    for i in range(len(s)):

        # rule 2
        if s[i] in not_allowed:
            valid = False
            break

        # rule 1
        if i <= len(s) - 3 and three_repeating(s[i:i+3]):
            valid = True

        # rule 3
        if i <= len(s) - 2 and s[i] == s[i + 1] and i - last_pair_ind > 1:
            num_pairs += 1
            last_pair_ind = i

    if num_pairs < 2: valid = False
    return valid

def increment(s, ind):
    s = s[:ind] + nxtmap[s[ind]] + s[ind+1:]
    if s[ind] == 'a':
        return increment(s, ind - 1)
    return s

pw = 'hxbxwxba'

while not is_valid(pw):
    pw = increment(pw, len(pw) - 1)

pw = increment(pw, len(pw) - 1)

while not is_valid(pw):
    pw = increment(pw, len(pw) - 1)

print(pw)