import random
import json

# File path
player_file = "saved_data.json"

# Load information from file


def load_file():
    try:
        with open(player_file, 'r') as file:
            player_info = json.load(file)
    except FileNotFoundError:
        player_info = {}
    return player_info

# Save player information


def save_file(player_file, player_info):
    with open(player_file, 'w') as file:
        json.dump(player_info, file, indent=2)

# Register player


def reg_player():
    global players
    number_players = int(input('How many people will play? '))
    for count in range(number_players):
        player_name = input(f'Enter the name for the player {count+1}: ')
        players.append({"name": player_name, "position": 0, "money": 1500,
                       "properties": 0, "games_won": 0, "games_played": 0})

# Display board


def display_board():
    print('Monopoly Board ......')
    for i, property in enumerate(board):
        owner_info = (f'Owner: {property["owner"]}')
        if property['pawned']:
            owner_info += " (Pawned)"
        print(
            f"{i}. {property['name']} - ${property['cost']} - {owner_info} - Houses: {property['houses']}")

# Pay Rent


def pay_rent(player, owner, rent):
    for p in player:
        if p['name'] != owner:
            if p['money'] <= rent:
                p['money'] -= rent
                print(f"{player['name']} paid €{rent} in rent to {owner}.")

# Buy Property


def buy_property(player, property):
    property['owner'] = player['name']
    player['money'] -= property['cost']
    player['properties'] += 1
    print(
        f"{player['name']} bought {property['name']} for ${property['cost']}.")

#  Build a house


def build_house(player, property):
    property['houses'] += 1
    player['money'] -= 100
    print(f"{player['name']} built a house on {property['name']}.")

# Pawn Property


def pawn_property(player, property):
    property['pawned'] = True
    print(
        f"{player['name']} pawned {property['name']}. Rent on this property is now $0.")

# Buy back the property


def buy_back_property(player, property):
    property['pawned'] = False
    player['money'] -= property['cost']
    print(
        f"{player['name']} bought back {property['name']} for ${property['cost']}.")

# Sell house


def sell_house(player, property):
    property['houses'] -= 1
    player['money'] += 50
    print(f"{player['name']} sold a house on {property['name']} for $50.")

# Check Winner


def check_winner(player):
    global players, board
    for location in board:
        if location['owner'] != None:
            continue
        else:
            owned_properties = sum(
                1 for prop in board if prop['owner'] == player['name'])
            if owned_properties > len(board) / 2:
                player['games_won'] += 1
                print(f"Congratulations, {player['name']}! You won the game!")
                save_file(player_info)

# Dice Roll


def dice_roll():
    roll = random.randint(1, 6) + random.randint(1, 6)
    return roll


# Player turn
def play_turn(player):
    global board, players, player_info
    roll = dice_roll()
    print(f"{player['name']}'s turn. Dice roll: {roll}")

    player['position'] = (player['position'] + roll) % len(board)
    current_property = board[player['position']]

    print(f"{player['name']} landed on {current_property['name']}")

    if not current_property['owner']:
        print(f"{current_property['name']} is unowned. Do you want to buy it?")
        response = input("Enter 'yes' or 'no': ").lower()
        if response == 'yes' and player['money'] >= current_property['cost']:
            buy_property(player, current_property)
    elif current_property['owner'] == player['name']:
        print(
            f"{player['name']}, what do you want to do with {current_property['name']}?")
        print("1. Build a house")
        print("2. Pawn the property")
        print("3. Sell a house")
        choice = input("Enter the number of your choice: ")
        if choice == '1' and player['money'] >= 100:
            build_house(player, current_property)
        elif choice == '2':
            pawn_property(player, current_property)
        elif choice == '3' and current_property['houses'] > 0:
            sell_house(player, current_property)

    elif current_property['pawned']:
        print(
            f"{current_property['name']} is pawned. Do you want to buy it back?")
        response = input("Enter 'yes' or 'no': ").lower()
        if response == 'yes' and player['money'] >= current_property['cost']:
            buy_back_property(player, current_property)
    else:
        rent_amount = current_property['rent']
        print(
            f"{player['name']}, you landed on {current_property['name']} owned by {current_property['owner']}.")
        print(f"You owe ${rent_amount} in rent.")
        if player['money'] >= rent_amount:
            pay_rent(player, current_property['owner'], rent_amount)
        else:
            print(
                f"{player['name']} doesn't have enough money to pay the rent. Property goes uncollected.")


# Play the game


def play_game():
    global players, current_player
    while True:
        player = players[current_player]
        display_board()
        play_turn(player)
        check_winner(player)

        current_player = (current_player + 1) % len(players)
