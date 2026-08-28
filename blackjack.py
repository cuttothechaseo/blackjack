import random

SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
CARD_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}


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


def calculate_hand_value(hand):
    total = 0
    aces_count = 0

    for card in hand:
        rank, suit = card
        total += CARD_VALUES[rank]
        if rank == "A":
            aces_count += 1

    while total > 21 and aces_count > 0:
        total -= 10
        aces_count -= 1

    return total


def get_player_action():
    while True:
        valid_response = ["h", "s"]
        response = input("hit or stand? (h/s)").lower()

        if response in valid_response:
            return response


def player_turn(deck, player_hand):

    while True:
        player_total = calculate_hand_value(player_hand)
        print(f"You have {player_total}")

        if player_total >= 21:
            return player_total

        player_action = get_player_action()

        if player_action == "s":
            return player_total

        if player_action == "h":
            deal_card(deck, player_hand)


def dealer_turn(deck, dealer_hand):
    dealer_total = calculate_hand_value(dealer_hand)

    while dealer_total < 17:
        deal_card(deck, dealer_hand)
        dealer_total = calculate_hand_value(dealer_hand)

    return dealer_total


def determine_winner(player_total, dealer_total):
    if player_total > 21:
        print("Player busted - Dealer wins.")
    elif dealer_total > 21:
        print("Dealer busted - Player wins!")
    elif player_total > dealer_total:
        print("Player beat Dealer - Player wins!")
    elif player_total < dealer_total:
        print("Dealer beat Player - Dealer wins.")
    else:
        print("Player tied Dealer - it's a tie.")


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

    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    print(f"Player Hand: {player_hand} - {player_total}")
    print(f"Dealer Hand: {dealer_hand} - {dealer_total}")

    player_total = player_turn(deck, player_hand)

    if player_total <= 21:
        dealer_total = dealer_turn(deck, dealer_hand)
        print(f"Dealer Total: {dealer_total}")
        print(f"Player Total: {player_total}")
    else:
        print(f"Dealer Total: {dealer_total}")
        print(f"Player Total: {player_total}")

    determine_winner(player_total, dealer_total)


if __name__ == "__main__":
    main()
