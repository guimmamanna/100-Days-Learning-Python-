import random


def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def calculate_score(hand):
    score = sum(hand)
    if score == 21 and len(hand) == 2:
        return 0
    if 11 in hand and score > 21:
        hand[hand.index(11)] = 1
    return sum(hand)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw."
    if dealer_score == 0:
        return "Dealer has Blackjack. You lose."
    if user_score == 0:
        return "You win with a Blackjack!"
    if user_score > 21:
        return "You went over. You lose."
    if dealer_score > 21:
        return "Dealer went over. You win!"
    if user_score > dealer_score:
        return "You win!"
    return "You lose."


def play_game():
    user_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            if input("Type 'y' to get another card, 'n' to pass: ") == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while calculate_score(dealer_cards) != 0 and calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())

    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")
    print(compare(calculate_score(user_cards), calculate_score(dealer_cards)))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
