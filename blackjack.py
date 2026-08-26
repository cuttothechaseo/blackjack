import random

SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")


def create_deck():
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            deck.append((rank, suit))

    return deck


def shuffle_deck(deck):
    random.shuffle(deck)


def deal_card(deck, hand):
    dealt_card = deck.pop()
    hand.append(dealt_card)
    return dealt_card


def main():
    deck = create_deck()
    shuffle_deck(deck)
    player_hand = []
    dealer_hand = []

    for _ in range(2):
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)

    print(f"Player Hand: {len(player_hand)}")
    print(f"Dealer Hand: {len(dealer_hand)}")
    print(f"Cards remaining: {len(deck)}")


if __name__ == "__main__":
    main()
