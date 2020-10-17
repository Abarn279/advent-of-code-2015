from file_importer import FileImporter

# Get input
inp = FileImporter.get_input("/../input/5.txt").split('\n')

vowels = set(['a', 'e', 'i', 'o', 'u'])
not_strs = set(['ab', 'cd', 'pq', 'xy'])
has_3_vowels = lambda x: sum(1 for i in x if i in vowels) >= 3
has_2_in_row = lambda x: len([x[i] for i in range(len(x) - 1) if x[i] == x[i+1]]) > 0
has_forbidden_strings = lambda x: len([x[i] for i in range(len(x) - 1) if x[i] + x[i+1] in not_strs]) > 0
is_nice = lambda x: has_3_vowels(x) and has_2_in_row(x) and not has_forbidden_strings(x)

print(sum(1 for i in inp if is_nice(i)))