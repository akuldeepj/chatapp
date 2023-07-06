import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1000))

done = False

while not done:
    client.sendall(input('message:').encode('UTF-8'))
    print(client.recv(1024).decode('UTF-8'))
    # if input('continue? (y/n)') == 'n':
    #     done = True
client.close()
