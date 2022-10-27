from anytree import RenderTree
from anytree.importer import JsonImporter
import json
from anytree.dotexport import DotExporter, RenderTreeGraph

with open("inner/tree.json", "r") as f:
    jsontree = json.load(f)

importer = JsonImporter()
tree = importer.import_(jsontree)
DotExporter(tree).to_dotfile("inner/tree.dot")