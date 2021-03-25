from deck_of_cards import Deck, Dealer, Player
import socket
import json

deck = Deck()
dealer = Dealer()
player = Player()


def parse_message(message):
    return json.loads(message)


# def poleteli_obratno_complex(data):
#     return json.dumps(data, default=encode_complex)


def poleteli_obratno(answer, data):
    answer['server_cmd'] = data
    return json.dumps(answer)


# def encode_complex(obj):
#     if isinstance(obj, complex):
#         return obj.real, obj.imag


answer = {

}

sock = socket.socket()
sock.bind(('', 9014))
sock.listen(1)
print("Start Listen")
conn, addr = sock.accept()
print("====================================Connection=======================================")
conn.send("Hello User! do you wanna play BlackJack(yes/no)".encode("utf-8"))
while True:
    message = conn.recv(1024).decode('utf-8')
    parse = parse_message(message)
    user_cdm = parse.get('user_cdm')
    print(user_cdm)
    server_answer = poleteli_obratno(answer, input())
    sock.send(server_answer.encode('utf-8'))
    if not message:
        break

    # if user_cdm == 'no':
    #     data = 'fuck'
    #
    # if user_cdm == 'yes':
    #     deck.shuffle()
    #     player.draw(deck, 2)
    #     data = player.hand

conn.close()
