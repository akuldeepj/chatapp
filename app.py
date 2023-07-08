from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import functions as fn

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_chatroom', methods=['POST'])
def create_chatroom_route():
    user1 = request.form['user1']
    user2 = request.form['user2']
    chat_id = fn.create_chatroom({'id': user1}, {'id': user2})
    return jsonify({'chat_id': chat_id})

@app.route('/send_message', methods=['POST'])
def send_message_route():
    user = request.form['user']
    chat_id = request.form['chat_id']
    message = request.form['message']
    success = fn.send_message({'id': user}, chat_id, message)
    return jsonify({'success': success})

@app.route('/print_chat', methods=['POST'])
def print_chat_route():
    chat_id = request.form['chat_id']
    messages = fn.print_chat(chat_id)
    return jsonify({'messages': messages})

@app.route('/receive_messages', methods=['POST'])

def receive_messages_route():
    chat_id = request.form['chat_id']
    messages = fn.receive_messages(chat_id)
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
