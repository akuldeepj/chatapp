import socket
import json
import functions as fn
with open('info.json','r') as f:
    a = json.load(f)
chat_room = fn.create_chatid('ID001','ID002')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

done = False
client.sendall(chat_room.encode('UTF-8'))
while not done:
    client.sendall(input('message:').encode('UTF-8'))
client.close()
