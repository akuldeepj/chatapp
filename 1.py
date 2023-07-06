import json
x = '123'
with open('info.json','r') as f:
    a = json.load(f)
for i in a:
    print(i['phoneNum'])
    print(i)