
import random

#dealer stands if value is 17 or lesser

class Game:
    def __init__(self):
        self.cards = make_deck()
        self.dealer_cards = []
        self.player_cards = []

    def inital_cards(self):
        for i in range(2): self.player_cards.append(self.cards.pop())


        for i in range(2): self.dealer_cards.append(self.cards.pop())

        






def make_deck():
    cards = []
    suits = ["spades", "clubs", "diamonds", "hearts"]

    cards = [(suit, value) for value in range(2,15) for suit in suits]
    random.shuffle(cards)
    print(len(cards))
    return cards


def card_value(card_tuple):

    if (card_tuple[1] >= 10 and card_tuple[1] < 15):
        return 10
    if (card_tuple[1] == 14):
        return 11

    return card_tuple[1]


def player_loop(cards):

    player_value = 0

    while (True):

        print("Select one of the options")
        print("1. Hit")
        print("2. Stop")
        val = int(input("Enter choice: "))

        if (val == 2):
            break

        index = random.randint(0,51)
        card = cards[index]
        print("")
        print(f"You got {card[1]} {card[0]}")
        player_value += card_value(card)
        print(f"Total value: {player_value}")
        print("")

        cards.remove(card)
        if (player_value > 21):
            print("BUST!")
            return -1
    
    return player_value
