import json

def user_id(filename='info.json'):
    with open(filename,'r') as f:
        a = json.load(f)
        last_id = a[-1]['id']
        new_id = str(int(last_id) + 1).zfill(len(last_id))
    # print(new_id)
        last_id = new_id
    return str(new_id)

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
            for j in i['msg']:
                print(i['msg'][j]['id'] + ' : ' + i['msg'][j]['msg'])

def verify_id(user1,user2,filename='test.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    for i in data:
        if i['id'] == create_chatid(user1,user2):
            return True
        else:
            return False

if(verify_id('u1','u2')):
    print_chat("001002")
else:
    create_chatid('u1','u2')

print(user_id())