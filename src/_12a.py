from file_importer import FileImporter
import json

def get_sum(doc): 
    sm = 0

    if isinstance(doc, dict):
        if 'red' in doc.values():
            return 0
        children = doc.values()
    elif isinstance(doc, list):
        children = doc
    else:
        raise Exception()

    for child in children:
        if isinstance(child, int):
            sm += child

        elif isinstance(child, dict) or isinstance(child, list):
            sm += get_sum(child)

    return sm    

raw = FileImporter.get_input("/../input/12.txt")
doc = json.loads(raw)

print(get_sum(doc))