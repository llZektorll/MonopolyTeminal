import random
import json

# region Menu


def inintialize_menu():
    return ('''
##########################
###  Jogo do Monopólio ###
##########################

0 - Sair
1 - Novo Jogo
2 - Registar Jogadores
3 - Ver Jogadores
4 - Histórico de jogos
''')
# endregion

# region DiceRoll


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)
# endregion

# region Player


def create_or_load_player(existing_players):
    players = []
    player_count = 0
    while player_count > 2:
        player_name = input("Enter your player name: ")
        if player_name in existing_players:
            choice = input(f"Player '{
                           player_name}' already exists. Do you want to reuse this player? (yes/no): ")
            if choice.lower() == 'no':
                return create_or_load_player(existing_players)
            elif choice.lower() == 'yes':
                players.append(
                    {"name": player_name, "position": 0, "money": 1500})
        player_count + 1
    return players


def display_players(players):
    print("Current Players: ")
    for player in players:
        print(f"{player['name']} - Position: {player['position']
                                              }, Money: ${player['money']}")
# endregion

# region Board


def inintialize_board():
    return [
        {"name": "Go", "cost": 0, "rent": 0, "owner": None},
        {"name": "house_1", "cost": 350, "rent": 35, "owner": None},
        {"name": "house_2", "cost": 250, "rent": 25, "owner": None},
        {"name": "house_3", "cost": 150, "rent": 15, "owner": None},
        {"name": "house_4", "cost": 650, "rent": 65, "owner": None},
        {"name": "house_5", "cost": 450, "rent": 45, "owner": None},
        {"name": "house_6", "cost": 250, "rent": 25, "owner": None},
        {"name": "house_7", "cost": 350, "rent": 35, "owner": None},
        {"name": "house_8", "cost": 150, "rent": 15, "owner": None},
        {"name": "house_9", "cost": 550, "rent": 55, "owner": None},
        {"name": "house_10", "cost": 450, "rent": 45, "owner": None},
        {"name": "house_11", "cost": 350, "rent": 35, "owner": None},
    ]


def display_board(board):
    print("Current Board:")
    for property in board:
        print(
            f"{property['name']} - Owner: {property['owner'] if property['owner'] else 'None'}")

# endregion

# reggion Property

# endregion


def player_location(player, current_property):
    print(f"{player['name']} landed on {current_property['name']}.")
    if current_property['owner'] == None:
        choice = input("Enter 'yes' to buy or 'no' to skip: ")
        if choice.lower() == 'yes' and player['money'] >= current_property['cost']:
            player['money'] -= current_property['cost']
            current_property['owner'] = player['name']
            print(f"{player['name']} bought {current_property['name']} for €{
                  current_property['cost']}.")
        else:
            print(f"{player['name']} chose not to buy {
                  current_property['name']}.")
    elif current_property['owner'] != None:
        rent_amount = current_property['rent']
        print(f"{player['name']} landed on {
              current_property['name']} owned by {current_property['owner']}.")
        print(f"{player['name']} pays ${rent_amount} rent to {
              current_property['owner']}.")
        player['money'] -= rent_amount
    elif current_property['owner'] == player:
        print(f"{player['name']} landed on his property {
              current_property['name']}.")
        choice = input("Enter 'yes' to SELL or 'no' to skip: ")
        if choice.lower() == 'yes':
            player['money'] += current_property['cost']
            current_property['owner'] = None
            print(f"{player['name']} sold {current_property['name']} for €{
                  current_property['cost']}.")
        else:
            print(f"{player['name']} chose not to Sell {
                  current_property['name']}.")
