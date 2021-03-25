import random
import json


class Dealer:
    """
    инициализация карт диллера
    """

    def __init__(self):
        self.dealer_hand = []

    def draw(self, deck, num=2):
        """
        взятие n карт из колоды до тех пор, пока они там есть
        """
        for _ in range(num):
            card = deck.deal()
            if card:
                self.dealer_hand.append(card)
            else:
                return False
        return True


class Card:
    def __init__(self, suit, val):
        """
            инициализация масти и значения карты
        """
        self.suit = suit
        self.value = val

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
                self.cards.append(Card(suit, val))

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
        return True

    def showHand(self):
        """
        отображение руки игрока
        """
        for card in self.hand:
            return f'{card.show()}'

    def discard(self):
        """
        сброс карты из руки
        """
        return self.hand.pop()


deck = Deck()
dealer = Dealer()
player = Player()
# deck.shuffle()
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
