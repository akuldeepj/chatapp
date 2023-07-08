from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

def user_id(filename='info.json'):
    with open(filename, 'r') as f:
        a = json.load(f)
        last_id = a[-1]['id']
        new_id = str(int(last_id) + 1).zfill(len(last_id))
        last_id = new_id
    return str(new_id)

def create_chatid(user1, user2):
    if user1[2:] < user2[2:]:
        return user1[2:] + user2[2:]
    else:
        return user2[2:] + user1[2:]

def verify_id(user1, user2, filename='test.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    for i in data:
        if i['id'] == create_chatid(user1, user2):
            return True
    return False

def create_chatroom(user1, user2, filename='test.json'):
    chat_id = create_chatid(user1['id'], user2['id'])
    chatroom = {'id': chat_id, 'members': [user1['id'], user2['id']], 'messages': []}
    with open(filename, 'r') as f:
        data = json.load(f)
    data.append(chatroom)
    with open(filename, 'w') as f:
        json.dump(data, f)
    return chat_id

def join_chatroom(user, chat_id, filename='test.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    for chatroom in data:
        if chatroom['id'] == chat_id:
            chatroom['members'].append(user['id'])
            with open(filename, 'w') as f:
                json.dump(data, f)
            return True
    return False

def print_chat(chat_id, filename='test.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    for chatroom in data:
        if chatroom['id'] == chat_id:
            return chatroom['messages']

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
            return True
    return False

def receive_messages(chat_id, filename='test.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    for chatroom in data:
        if chatroom['id'] == chat_id:
            return chatroom['messages']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_chatroom', methods=['POST'])
def create_chatroom_route():
    user1 = request.form['user1']
    user2 = request.form['user2']
    chat_id = create_chatroom({'id': user1}, {'id': user2})
    return jsonify({'chat_id': chat_id})

@app.route('/send_message', methods=['POST'])
def send_message_route():
    user = request.form['user']
    chat_id = request.form['chat_id']
    message = request.form['message']
    success = send_message({'id': user}, chat_id, message)
    return jsonify({'success': success})

@app.route('/print_chat', methods=['POST'])
def print_chat_route():
    chat_id = request.form['chat_id']
    messages = print_chat(chat_id)
    return jsonify({'messages': messages})

@app.route('/receive_messages', methods=['POST'])
def receive_messages_route():
    chat_id = request.form['chat_id']
    messages = receive_messages(chat_id)
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
