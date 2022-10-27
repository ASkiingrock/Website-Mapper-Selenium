from anytree import AnyNode
from anytree.exporter import JsonExporter
import json

link = 'YOUR WEBSITE'
if link[-1] != "/"
    link += "/
root = AnyNode(name=link)
exporter = JsonExporter(sort_keys=True)
exporttree = exporter.export(root)
with open("start-tree.json", "w") as f:
    json.dump(exporttree, f)
with open("links.json", "w") as f:
    json.dump([link], f)
