total = 1
row = 3010 # inp
col = 3019 # inp

while col != 1:
    col -= 1
    row += 1
    total += 1

for i in range(1, row):
    total += i

initial = 20151125
for i in range(1, total):
    initial = (initial * 252533) % 33554393

print(initial)