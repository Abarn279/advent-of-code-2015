from file_importer import FileImporter

# Get input
inp = FileImporter.get_input("/../input/1.txt")
count = 0
index = 0
for char in inp:
    if char == "(":
        count += 1
    if char == ")":
        count -= 1
    if count < 0:
        print(index + 1)
        break
    index += 1