import socket
import json


def change_data(data, mess):
    data['user_cmd'] = mess
    #data['conn_count'] += 1
    return json.dumps(data)


sock = socket.socket()

sock.connect(('localhost', 10052))

data = {
    #'conn_count': 0
}
print(sock.recv(1024).decode("utf-8"))
while True:
    message = change_data(data, input())
    sock.send(message.encode("utf-8"))
    response = sock.recv(1024).decode("utf-8")
    if response:
        print(response)




sock.close()
