from p1_random import P1Random

# define a menu function
def menu():
    print("1. Get another card\n2. Hold hand")
    print("3. Print statistics\n4. Exit")
    print("")

rng = P1Random()
# print(rng.next_int(13) + 1)

# Set initial variables and boolean for continuing a game
game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
tie_games = 0

# Control the number of games the player will play
while game_continue:  # game #1, #2, #3, ...
    # 1.  print game number message
    game_num += 1
    print(f"START GAME #{game_num}")
    print()
    # 2. deal a card to the player automatically
    player_hand = 0
    # deal a card to the player
    card = rng.next_int(13) + 1
    if card == 1:
        print("Your card is a ACE!")
        card = 1
    elif 2 <= card <= 10:
        print(f"Your card is a {card}!")
    # For face cards, assign their value as 10 but print their "name" to the output
    elif card == 11:
        print("Your card is a JACK!")
        card = 10
    elif card == 12:
        print("Your card is a QUEEN!")
        card = 10
    elif card == 13:
        print("Your card is a KING!")
        card = 10
    # 3. add card number to the player hand value
    player_hand += card
    # 4. print hand value
    print(f"Your hand is: {player_hand}")
    print()
    # 5. Keep playing the current game by prompting the player to choose a menu option
    no_winner = True
    while no_winner:
        # print four menu options
        menu()
        # ask/prompt player for an input to choose menu option
        option = int(input("Choose an option: "))
        print()
        if option == 1:
            # deal a card to the player
            card = rng.next_int(13) + 1
            if card == 1:
                print("Your card is a ACE!")
                card = 1
            elif 2 <= card <= 10:
                print(f"Your card is a {card}!")
            elif card == 11:
                print("Your card is a JACK!")
                card = 10
            elif card == 12:
                print("Your card is a QUEEN!")
                card = 10
            elif card == 13:
                print("Your card is a KING!")
                card = 10
            player_hand += card
            print(f"Your hand is: {player_hand}")
            print()
            if player_hand == 21:
                print("BLACKJACK! You win!")
                player_wins += 1
                no_winner = False
            elif player_hand > 21:
                print("You exceeded 21! You lose.")
                print()
                dealer_wins += 1
                no_winner = False
        elif option == 2:
            # deal a card to the dealer
            dealer_hand = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            print()
            # compare the player hand with dealer hand value
            # determine who wins the game
            if dealer_hand > 21:
                player_wins += 1
                print("You win!")
                print()
            elif dealer_hand == player_hand:
                tie_games += 1
                print("It's a tie! No one wins!")
                print()
            elif dealer_hand > player_hand:
                dealer_wins += 1
                print("Dealer wins!")
                print()
            no_winner = False
        elif option == 3:
            # print statistics. set the percentage of player wins to two decimal places
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {tie_games}")
            print(f"Total # of games played is: {game_num - 1}")
            print(f"Percentage of Player wins: {100 * player_wins / (game_num - 1):.2f}%")
            print()
        elif option == 4:
            no_winner = False # get out of the inner while loop
            game_continue = False # get out of outer while loop
        else:
            # Print error message if any option other than 1, 2, 3 or 4 is inputted
            print("Invalid input!\nPlease enter an integer value between 1 and 4.")
            print()

# 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 6, 3, 4



