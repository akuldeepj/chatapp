# from flask import Flask, render_template, request, redirect, url_for, flash,session,jsonify
# import json
# import functions as fn
# import login_reg as lr

# app = Flask(__name__)
# app.secret_key = 'secret-key'

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         phone_num = request.form['phone_num']

#         if lr.register_user(username, password, phone_num):
#             flash('Registration successful!', 'success')
#             return redirect(url_for('login'))
#         else:
#             flash('Username already taken', 'error')

#     return render_template('register.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         phone_num = request.form['phone_num']
#         password = request.form['password']

#         user_id = lr.verify_credentials(phone_num, password)
        
#         if user_id:
#             flash('Login successful!', 'success')

#             # Store user ID in the session
#             session['user_id'] = user_id

#             return redirect(url_for('dashboard'))
#         else:
#             flash('Invalid phone number or password', 'error')

#     return render_template('login.html')

# @app.route('/dashboard', methods=['GET', 'POST'])
# def dashboard():
#     user_id = session.get('user_id')
#     if user_id:
#         with open('info.json', 'r') as f:
#             data = json.load(f)
#         user = next((user for user in data if user['id'] == user_id), None)
#         if user:
#             if request.method == 'POST':
#                 phone_num = request.form['phone_num']

#                 other_user = next((u for u in data if u['phoneNum'] == phone_num), None)
#                 if other_user:
#                     chatroom_exists = fn.verify_id(user['id'], other_user['id'])
#                     if chatroom_exists:
#                         flash('A chatroom with the selected user already exists!', 'error')
#                     else:
#                         chat_id = fn.create_chatroom(user, other_user)
#                         fn.join_chatroom(user, chat_id)
#                         fn.join_chatroom(other_user, chat_id)
#                         flash('Chatroom created successfully!', 'success')

#                     return redirect(url_for('chat', chat_id=chat_id))

#             with open('test.json', 'r') as f:
#                 chatrooms_data = json.load(f)

#             chatrooms = []
#             for chatroom in chatrooms_data:
#                 if user_id in chatroom['members']:
#                     chatrooms.append(chatroom)
                    
#             with open('info.json','r') as f:
#                 user_name = json.load(f)
#             x = chat_id[:3] 
#             y = chat_id[3:]
#             if x == user_id:
#                 temp = y
#             else:
#                 temp = x
#             for usr_id in user_name:
#                 if usr_id['id'] == temp:
#                     username = usr_id['Username']
                 

#             return render_template('dashboard.html', user=user, chatrooms=chatrooms,username=username)

#     flash('Please log in', 'error')
#     return redirect(url_for('login'))


# @app.route('/chat/<chat_id>', methods=['GET', 'POST'])
# def chat(chat_id):
#     user_id = session.get('user_id')
#     if user_id:
#         with open('info.json', 'r') as f:
#             data = json.load(f)
#         user = next((user for user in data if user['id'] == user_id), None)
#         if user:
#             if request.method == 'POST':
#                 message = request.form['message']
#                 fn.send_message(user, chat_id, message)
#                 return 'Message sent' 

#             chat_messages = fn.print_chat(chat_id)
#             return render_template('chat.html', user=user, chat_id=chat_id, messages=chat_messages)

#     flash('Please log in', 'error')
#     return redirect(url_for('login'))


# @app.route('/chat/<chat_id>/messages', methods=['GET'])
# def get_messages(chat_id):
#     chat_messages = fn.print_chat(chat_id)
#     return jsonify(chat_messages)

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import json
import functions as fn
import login_reg as lr

app = Flask(__name__)
app.secret_key = 'secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        phone_num = request.form['phone_num']

        if lr.register_user(username, password, phone_num):
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already taken', 'error')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone_num = request.form['phone_num']
        password = request.form['password']

        user_id = lr.verify_credentials(phone_num, password)

        if user_id:
            flash('Login successful!', 'success')

            # Store user ID in the session
            session['user_id'] = user_id

            return redirect(url_for('dashboard'))
        else:
            flash('Invalid phone number or password', 'error')

    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    user_id = session.get('user_id')
    if user_id:
        with open('info.json', 'r') as f:
            data = json.load(f)
        user = next((user for user in data if user['id'] == user_id), None)
        if user:
            if request.method == 'POST':
                phone_num = request.form['phone_num']

                other_user = next((u for u in data if u['phoneNum'] == phone_num), None)
                if other_user:
                    chatroom_exists = fn.verify_id(user['id'], other_user['id'])
                    if chatroom_exists:
                        flash('A chatroom with the selected user already exists!', 'error')
                        
                    else:
                        chat_id = fn.create_chatroom(user, other_user)
                        fn.join_chatroom(user, chat_id)
                        fn.join_chatroom(other_user, chat_id)
                        flash('Chatroom created successfully!', 'success')
                        return redirect(url_for('chat', chat_id=chat_id))
                else:
                    for a in data:
                        if phone_num not in a['phoneNum']:
                            flash("Phone Number not registered",'error')
                            break

            with open('test.json', 'r') as f:
                chatrooms_data = json.load(f)

            chatrooms = []
            for chatroom in chatrooms_data:
                if user_id in chatroom['members']:
                    chatrooms.append(chatroom)

            with open('info.json', 'r') as f:
                user_names = json.load(f)
            for chatroom in chatrooms:
                x = chatroom['id'][:3]
                y = chatroom['id'][3:]
                if x == user_id:
                    temp = y
                else:
                    temp = x
                for user_name in user_names:
                    if user_name['id'] == temp:
                        chatroom['username'] = user_name['Username']

            return render_template('dashboard.html', user=user, chatrooms=chatrooms)

    flash('Please log in', 'error')
    return redirect(url_for('login'))


@app.route('/chat/<chat_id>', methods=['GET', 'POST'])
def chat(chat_id):
    user_id = session.get('user_id')
    if user_id:
        with open('info.json', 'r') as f:
            data = json.load(f)
        user = next((user for user in data if user['id'] == user_id), None)
        if user:
            if request.method == 'POST':
                message = request.form['message']
                fn.send_message(user, chat_id, message)
                return 'Message sent'

            chat_messages = fn.print_chat(chat_id)
            return render_template('chat.html', user=user, chat_id=chat_id)

    flash('Please log in', 'error')
    return redirect(url_for('login'))


@app.route('/chat/<chat_id>/messages', methods=['GET'])
def get_messages(chat_id):
    chat_messages = fn.print_chat(chat_id)
    return jsonify(chat_messages)

if __name__ == '__main__':
    app.run(debug=True)

