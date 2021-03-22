import socket
import json
# from Home_work import deck_of_cards as game
# deck = game.Deck()
# dealer = game.Dealer()
# player = game.Player()
# deck.generate()
# deck.shuffle()


def parse_message(message):
    return json.loads(message)


def reaction(data):
    data = data.upper()
    return data


def change_data(data, mess):
    data['user_cmd'] = mess
    return json.dumps(data)


sock = socket.socket()
sock.bind(('', 10052))
sock.listen(1)
print("Start Listen")
conn, addr = sock.accept()
print("====================================Connection=======================================")
conn.send("Hello User! do you wanna play BlackJack(yes/no)".encode("utf-8"))
while True:
    message = conn.recv(1024).decode("utf-8")
    mess_dict = parse_message(message)
    user_cmd = mess_dict.get('user_cmd')

    if not message:
        conn.close()
        break

    if user_cmd == 'no':
        conn.send("See you later!".encode("utf-8"))
        conn.close()

    if user_cmd == 'yes':
        conn.send("lets go!".encode("utf-8"))

    # answer = reaction(user_cmd)
    # server_data = change_data(mess_dict, answer)
    # conn.send(server_data.encode("utf-8"))

conn.close()
