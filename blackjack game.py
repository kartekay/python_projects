import random

def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    return [(rank, suit) for rank in ranks for suit in suits]

def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        rank = card[0]
        if rank in ['J', 'Q', 'K']:
            score += 10
        elif rank == 'A':
            aces += 1
            score += 11
        else:
            score += int(rank)
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

def display_hand(hand, name):
    print(f"{name}'s hand: {', '.join([f'{rank} of {suit}' for rank, suit in hand])}")

def blackjack():
    while True:
        deck = create_deck()
        random.shuffle(deck)
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        while True:
            display_hand(player_hand, "Player")
            print(f"Player's score: {calculate_score(player_hand)}")
            if calculate_score(player_hand) > 21:
                print("Player busts! Dealer wins.")
                break
            move = input("Hit or Stand? (h/s): ").lower()
            if move == 'h':
                player_hand.append(deck.pop())
            elif move == 's':
                break
        if calculate_score(player_hand) <= 21:
            while calculate_score(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
            display_hand(dealer_hand, "Dealer")
            print(f"Dealer's score: {calculate_score(dealer_hand)}")
            player_score = calculate_score(player_hand)
            dealer_score = calculate_score(dealer_hand)
            if dealer_score > 21 or player_score > dealer_score:
                print("Player wins!")
            elif player_score < dealer_score:
                print("Dealer wins!")
            else:
                print("It's a tie!")
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

blackjack()
