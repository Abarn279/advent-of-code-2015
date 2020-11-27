from file_importer import FileImporter

def hex_to_char(c):
    return chr(int(c, 16))

# Get input
strings = FileImporter.get_input("/../input/8.txt").split('\n')

sm = 0
for s in strings:
    total = len(s)
    s = s[1:-1]
    
    i = 0
    while i < len(s):
        if s[i] != '\\':
            i += 1
            continue
        
        if s[i + 1] == 'x':
            s = s[:i] + hex_to_char(f'0{s[i+1:i+4]}') + s[i+4:]

        else:
            s = s[:i] + s[i+1:]

        i += 1

    filtered = len(s)
    sm += total - filtered

print(sm)