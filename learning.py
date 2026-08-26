"""A short value-flow exercise before building blackjack.

Complete deal_one_card() without changing main().
"""


def deal_one_card(deck, hand):
    """Move the final card from deck to hand and return the dealt card."""
    # TODO 1: Remove the final card from deck and store it in a variable.
    # Find the list method that removes and returns an item at the same time.
    dealt_card = deck.pop()

    # TODO 2: Add that card to hand.
    hand.append(dealt_card)

    # TODO 3: Return the dealt card.
    return dealt_card


def main():
    deck = ["2 of hearts", "King of spades", "Ace of clubs"]
    player_hand = []

    dealt_card = deal_one_card(deck, player_hand)

    print(f"Dealt card: {dealt_card}")
    print(f"Deck: {deck}")
    print(f"Player hand: {player_hand}")


if __name__ == "__main__":
    main()
