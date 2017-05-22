import hashlib
import json

with open("tmp.json") as json_file:
   data = json.load(json_file)

json_str = json.dumps(data, separators=(',',':'), sort_keys=True)

print(json_str)
h = hashlib.sha256(json_str.encode("utf-8")).hexdigest()
print(h)


