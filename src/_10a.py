def get_rep(s):
    i = 0
    final = ""
    while i < len(s):
        j = 0

        if i == len(s) - 1:
            final += '1' + str(s[i])
            break

        while s[i + j] == s[i]:
            if i + j >= len(s):
                break
            j += 1
        final += str(j) + str(s[i])
        i += j
    return final

inp = '3113322113'

for i in range(50):
    inp = get_rep(inp)

print(len(inp))