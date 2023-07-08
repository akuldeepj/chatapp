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
    
def verify_id(user1,user2,filename='test.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    for i in data:
        if i['id'] == create_chatid(user1,user2):
            return True
        else:
            return False

# if(verify_id('u1','u2')):
#     print_chat("001002")
# else:
#     create_chatid('u1','u2')

# print(user_id())

def create_chatroom(user1, user2, filename='test.json'):
    chat_id = create_chatid(user1['id'], user2['id'])
    chatroom = {'id': chat_id, 'members': [user1['id'], user2['id']], 'messages': []}
    with open(filename, 'r') as f:
        data = json.load(f)
    data.append(chatroom)
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f'Chatroom {chat_id} created successfully.')

def join_chatroom(user, chat_id, filename='test.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    for chatroom in data:
        if chatroom['id'] == chat_id:
            chatroom['members'].append(user['id'])
            with open(filename, 'w') as f:
                json.dump(data, f)
            print(f'User {user["id"]} joined chatroom {chat_id}.')
            return
    print(f'Chatroom {chat_id} not found.')

def print_chat(chat_id, filename='test.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    for chatroom in data:
        if chatroom['id'] == chat_id:
            for message in chatroom['messages']:
                print(f'{message["id"]} : {message["msg"]}')


from datetime import datetime

def send_message(user, chat_id, message, filename='test.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    for chatroom in data:
        if chatroom['id'] == chat_id:
            if 'messages' not in chatroom:
                chatroom['messages'] = []
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            new_message = {'id': user['id'], 'msg': message, 'timestamp': timestamp}
            chatroom['messages'].append(new_message)
            with open(filename, 'w') as f:
                json.dump(data, f)
            print(f'Message sent by {user["id"]} in chatroom {chat_id}.')
            return
    print(f'Chatroom {chat_id} not found.')


def receive_messages(chat_id, filename='test.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    for chatroom in data:
        if chatroom['id'] == chat_id:
            for message in chatroom['messages']:
                print(f'{message["id"]} : {message["msg"]} - {message["timestamp"]}')


user1 = {'id': 'ID001'}
user2 = {'id': 'ID002'}
user3 = {'id': 'ID003'}
user4 = {'id': 'ID004'}

chat_id = create_chatid(user1['id'], user2['id'])
create_chatroom(user1, user2)

send_message(user1, chat_id, 'Hello, User2!')

send_message(user2, chat_id, 'Hi, User1!')
create_chatroom(user3, user4)
send_message(user3,create_chatid(user3['id'], user4['id']), 'Hi, User4!')

send_message(user4,create_chatid(user3['id'], user4['id']), 'Hello, User3!')


receive_messages(chat_id)
receive_messages(create_chatid(user3['id'], user4['id']))