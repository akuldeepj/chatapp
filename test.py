import json

with open('info.json', 'r') as f:
    data = json.load(f)

for i in data:
    if i['id'] == '001':
        print(i['Username'])