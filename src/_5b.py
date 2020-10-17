from file_importer import FileImporter

# Get input
inp = FileImporter.get_input("/../input/5.txt").split('\n')

def has_twice(x):
    d = {}
    for i in range(len(x) - 1):
        duo = x[i] + x[i+1]
        if duo in d and i - d[duo] > 1:
            return True
        d[duo] = i
    return False 

has_2_in_row = lambda x: len([x[i] for i in range(len(x) - 2) if x[i] == x[i+2]]) > 0
is_nice = lambda x: has_twice(x) and has_2_in_row(x)

print(sum(1 for i in inp if is_nice(i)))