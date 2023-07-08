from flask import Flask,render_template,request,redirect,url_for,session
import functions as fn

app = Flask(__name__)

user1 = {'id': 'ID001'}
user2 = {'id': 'ID002'}
chat_id = fn.create_chatid(user1['id'], user2['id'])
fn.create_chatroom(user1, user2)
fn.send_message(user1, chat_id, 'Hello, User2!')

@app.route('/',method = ['GET','POST'])
def index():
    if method == 'POST':
        message = request.form['username']
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)