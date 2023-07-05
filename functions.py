import json

def create_chatid(user1, user2):
    if user1[2:] < user2[2:]:
        return user1[2:] + user2[2:]
    else:
        return user2[2:] + user1[2:]
    
def print_chat(id,filename = 'test.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    for i in data:
        if i['id'] == id:
            for j in i['messages']:
                print(j['sender'] + ' : ' + j['message'])

def verify_id(user1,user2,filename='test.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    for i in data:
        if i['id'] == create_chatid(user1,user2):
            return True
        else:
            return False

if(verify_id('u1','u2')):
    print_chat(create_chatid('u1','u2'))
else:
    create_chatid('u1','u2')
