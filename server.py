import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1000))
server.listen()

client, addr = server.accept()
done = False

while not done:
    data = client.recv(1024).decode('UTF-8')
    if data == 'quit':
        done = True
    else:
        print(data)
        # client.send(input('message:').encode('UTF-8'))