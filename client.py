import socket
import json


def poleteli(data, mess):
    data['user_cdm'] = mess
    return json.dumps(data)


def parse_responce(response):
    return json.loads(response)


data = {

}

sock = socket.socket()
sock.connect(('localhost', 9014))
print(sock.recv(1024).decode("utf-8"))
while True:
    message = poleteli(data, input())
    sock.send(message.encode('utf-8'))
    responce = sock.recv(1024).decode('utf-8')
    parse = parse_responce(responce)
    server_cmd = parse.get('server_cdm')
    print(server_cmd)
