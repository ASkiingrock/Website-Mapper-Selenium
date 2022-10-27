from anytree import RenderTree
from anytree.importer import JsonImporter
import json

with open("inner/tree.json", "r") as f:
    jsontree = json.load(f)

importer = JsonImporter()
tree = importer.import_(jsontree)

with open("inner/tree.txt", "w", encoding="utf-8") as f:
    f.write(str(RenderTree(tree)))