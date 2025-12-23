
from random import randint

def make_deck():
    cards = []
    suits = ["spades", "clubs", "diamonds", "hearts"]

    cards = [(suit, value) for value in range(2,14) for suit in suits]
    
    return cards


def card_value(card_tuple):

    if (card_tuple[1] >= 10 and card_tuple[1] < 14):
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

        index = randint(0,51)
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
