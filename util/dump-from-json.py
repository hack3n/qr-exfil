import json
import urllib.request

chunk_data = open("../raw.json", "r").read()
chunk_data = json.loads(chunk_data)

base64url_data = ""
for chunk in chunk_data:
    base64url_data += chunk[chunk.index("#") + 1:]

response = urllib.request.urlopen(base64url_data)
with open("output", "wb") as f:
    f.write(response.file.read())