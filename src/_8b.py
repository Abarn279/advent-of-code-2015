from file_importer import FileImporter
import string 

hex_chars = string.digits + 'abcdef' 
def is_hex(c):
    return c[0] in hex_chars and c[1] in hex_chars

def hex_to_char(c):
    return chr(int(c, 16))

# Get input
strings = FileImporter.get_input("/../input/8.txt").split('\n')

sm = 0
for s in strings:
    initial = len(s)
    
    i = 0

    while i < len(s):
        if s[i] not in ['\\', '\"']:
            i += 1
            continue

        s = s[:i] + '\\' + s[i:]
        
        if i + 2 > len(s) - 1:
            i += 2
            continue

        if s[i + 2] == 'x' and is_hex(s[i+3:i+5]):
            i += 5
        else:
            i += 2

    s = f'\"{s}\"'
    print(s)
    encoded = len(s)
    sm += encoded - initial

print(sm)