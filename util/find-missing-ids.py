import json

raw = open("../raw.json", "r")
json_obj = json.loads(raw.read())

ids = [int(row[:row.index("#")]) for row in json_obj]
missing = sorted(set(range(ids[0], ids[-1])) - set(ids))

print(missing)