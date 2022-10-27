import json

with open('inner/links.json') as f:
    links = json.load(f)

output = set([])

for i in links:
    output.add(i.split("/")[3])

print(output)
