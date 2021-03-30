import random
import json
import time


class Card:
    def __init__(self, suit, val, points):
        """
            инициализация масти и значения карты
        """
        self.suit = suit
        self.value = val
        self.points = points

    def __repr__(self):
        return f'{self.show()}'

    def show(self):
        """
        показать карту
        """
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return f"{val} of {self.suit}"
        # return f"{self.value}"


class Deck:
    def __init__(self):
        """
        self.cards - пустой список для хранения колоды
        self.generate() - заполнение колоды картами
        """
        self.cards = []
        self.generate()
        self.shuffle()

    def show(self):
        """
        отображение колоды карт
        """
        for card in self.cards:
            return f'{card.show()}'

    def generate(self):
        """
        генерация 52х карт 4х мастей
        """
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(1, 13):
                if val == 'Ace':
                    points = 1
                if val == 'Jack':
                    points = 11
                if val == 'Queen':
                    points = 12
                if val == 'King':
                    points = 13
                else:
                    points = int(val)
                self.cards.append(Card(suit, val, points))

    def shuffle(self):
        """
        перемешать колоду
        """
        return random.shuffle(self.cards)

    def deal(self):
        """
        достать верхнюю карту
        """
        return self.cards.pop()


class Player:
    """
    инициализация руки игрока
    """

    def __init__(self):
        self.hand = []
        self.bet = 0
        self.sum_p = 0
        self.money = 100

    def sum_points(self):
        self.sum_p = sum([card.points for card in self.hand])

    def change_bet(self):
        """
        ставим ставочки
        """
        max_bet = 50
        min_bet = 0
        while True:
            val = int(input('Make your bet: '))
            if min_bet < val < max_bet:
                self.bet = val
                self.money -= self.bet
            print(f'Player give {self.bet}')
            break

    def draw(self, deck, num):
        """
        взятие n карт из колоды до тех пор, пока они там есть
        """
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
            self.sum_points()
        return True

    def showHand(self):
        """
        отображение руки игрока
        """
        for card in self.hand:
            print(f'{card.show()} ', end='')
        print(f'\nTotal points: {self.sum_p}')

    def discard(self):
        """
        сброс карты из руки
        """
        return self.hand.pop()

    def ask_card(self):
        if self.sum_p == 21:
            return False
        choice = input('Want more card(yes/no)')
        if choice == 'yes':
            return True
        else:
            return False


# class Dealer(Player):
#     """
#     инициализация карт диллера
#     """
#
#     def __init__(self):
#         self.hand = []
#         self.max_points = 17
#
#     def sum_points(self):
#         self.sum_p = sum([card.points for card in self.hand])
#
#     def draw(self, deck, num=2):
#         """
#         взятие n карт из колоды до тех пор, пока они там есть
#         """
#         for _ in range(num):
#             card = deck.deal()
#             if card:
#                 self.hand.append(card)
#             else:
#                 return False
#         return True
#
#     def ask_card(self):
#         print('Dealer thinking...')
#         if self.sum_p < self.max_points:
#             return True
#         else:
#             return False
#
#     def change_bet(self):
#         max_bet = 50
#         min_bet = 0
#         self.bet = random.randint(min_bet, max_bet)


class Bot(Player):
    """
    исскуственный интеллект
    """
    def __init__(self):
        self.hand = []
        self.bet = 0
        # self.max_points = random.randint(17, 20)
        self.max_points = 17
        self.money = 100

    def change_bet(self):
        max_bet = 50
        min_bet = 0
        self.bet = random.randint(min_bet, max_bet)
        self.money -= self.bet
        print('Bot preparing to make a bet...')
        time.sleep(1)
        print(f'Bot give {self.bet}')

    def showHand(self):
        """
        отображение руки бота
        """
        for card in self.hand:
            print(f'{card.show()} ', end='')
        print(f'\nTotal points: {self.sum_p}')

    def ask_card(self):
        print('Bot thinking...')
        if self.sum_p < self.max_points:
            return True
        else:
            return False


class Game:
    def __init__(self):
        """
        игра содержит в себе информацию об игроках за столом, колоде для игры и ставках
        """
        self.players = []
        # self.dealer = Dealer()
        self.a_p_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 50, 0

    def starting(self):
        """
        предложение поиграться
        """
        choice = input("Hello User! do you wanna play BlackJack(yes/no)")
        if choice == 'yes':
            return True
        if choice == 'no':
            return False

    def gen_table(self):
        """
        садимся за столик
        """
        while True:
            p_count = int(input('Enter count of players: '))
            if p_count <= 4:
                break
        self.a_p_count = p_count + 1
        pos = 1
        for i in range(p_count):
            b = Bot()
            # print(f'{b} is created')
            self.players.append(b)
            pos += 1
        self.players.append(Player())
        print(f'Your position is {pos}')

    def bet(self):
        """
        ставки для ботов рандомятся, для игрока указывается
        """
        for player in self.players:
            player.change_bet()

    def check(self, player):
        if player.sum_p >= 21:
            return True
        else:
            return False

    def remove_player(self, player):
        player.showHand()
        if isinstance(player, Player):
            print('You are loser!')
        elif isinstance(player, Bot):
            print(player, 'are fall!')
        self.players.remove(player)

    def check_wins(self):
        for player in self.players:
            player.money += player.bet * 2
        if isinstance(player, Bot):
            print('Bot wins!')
        if isinstance(player, Player):
            print('You are win!')

    def ask_card(self):
        for player in self.players:
            while player.ask_card():
                time.sleep(3)
                player.draw(deck, 1)
                print('============================================================')
                player.showHand()
                print('============================================================')
                stop = self.check(player)
                if stop:
                    if player.sum_p > 21 or isinstance(player, Player):
                        self.remove_player(player)
                    break

    def game_start(self):
        """
        начало игры с рассадкой, ставками и раздачей карт
        """
        if not self.starting():
            self.starting()
        self.gen_table()
        self.bet()
        self.create_hand()
        self.ask_card()
        self.check(player)

    def create_hand(self):
        for player in self.players:
            Player.draw(player, deck, 2)
            print('============================================================')
            print(f'{player.showHand()}')


deck = Deck()
bot = Bot()
player = Player()
game = Game()
print(game.game_start())
# player.draw(deck, 2)
# print(player.hand)
#
#
# def encode_complex(obj):
#     if isinstance(obj, complex):
#         return obj.real, obj.imag
#
#
# json.dumps(player.hand, default=encode_complex)
# print(player.hand)
# f, s = player.hand
# new_hand = [f, s]
# print(new_hand)
# new_hand = []
# for i in player.hand:
#     new_hand.append(i)
# print(help(new_hand))
# print(dir(new_hand))
# print(dir(player.hand))
# dealer.draw(deck, 2)
# print(f'Dealer has X and {dealer.dealer_hand[1]}')
# player.draw(deck, 2)
# print(f'You have {player.hand[0]} and {player.hand[1]}')
# if int(str(dealer.dealer_hand[1])) + int(str(dealer.dealer_hand[0])) == 21:
#     print('Dealer has 21 and wins!')
# elif int(str(dealer.dealer_hand[1])) + int(str(dealer.dealer_hand[0])) > 21:
#     print('Dealer has busted')
# while int(str(player.hand[1])) + int(str(player.hand[0])) < 21:
#     action = str(input('Do you want stay or hit?: '))
#     if action == 'hit':
#         player.draw(deck, 1)
#     print('Now you have:', player.hand)
# # int(str(player.hand[1])) + int(str(player.hand[0])) + int(str(player.hand[2])))
