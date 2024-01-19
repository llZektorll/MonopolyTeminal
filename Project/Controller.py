'''
    Registration of users - Restisto(sim), validação de outro users (não)
    buy location
    build house
    pay rent
    property return
    property reclraim
    sell house
    write
    read
    definition of winning
'''
import random
import json


def save_data(players):
    with open("data.json", "w") as file:
        json.dump(players, file)


def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except (json.JSONDecodeError):
        return []


def roll_dice():
    roll = random.randint(1, 6) + random.randint(1, 6)
    return roll


def reg_player(players, player_name):
    old_players = load_data()
    for players_history in old_players['name']:
        for player in player_name:
            if player != players_history:
                players = ({"name": player, "position": 0, "money": 1500})
                print(f'Player {player} added correctly.')
            else:
                print('Player already exits, loading player.')
                players = ({"name": player, "position": 0, "money": 1500})
    return players


def buy_location(player, board_position):
    for board_location in board_position:
        if player['position'] == board_location:
            if board_location['owner'] == "Board":
                if player['money'] <= board_location['price']:
                    print('Insufficient funds! ')
                elif player['money'] >= board_location['price']:
                    choice = input(
                        'Do you want to buy this lcoation? yes(y) no (n)').lower
                    if choice == 'y':
                        wallet = player['money']
                        price = board_location['price']
                        diference = wallet - price
                        player['money'].update(diference)
                        board_location['owner'].update(player['name'])
                        return player['money'], board_location['owner']
                    else:
                        print('Opted out of buying the location')
            else:
                print('Property already have a owner')


def build_house(player, board_position):
    if board_position['owner'] == player['name']:
        if board_position['house'] <= 3:
            choice = input(
                "Do you want to build a house? y(yes) n(no)").lower()
            if choice == 'y':
                if player['money'] <= (board_position['price'] * 2):
                    print('You do not have the money to buy a house')
                else:
                    wallet = player['money']
                    price = board_position['price'] * 2
                    difrence = wallet - price
                    player['money'].update(difrence)
                    board_position['house'] = board_position['house'] + 1
                    return player['money'], board_position['house']
    else:
        print('You do not own this property')


def pay_rent(player, board_location):
    if board_location['owner'] != player['name']:
        if player['money'] <= (board_location['price'] * 0.10):
            print('Unable to pay rent')
            player['money'].update('0')
            return player['money']
        else:
            diference = player['money'] - (board_location['price'] * 0.10)
            player['money'].update(diference)
            return player['money']

def pawn_house(player, board_location):
    if player['name'] == board_location['owner']:
        choise = input("do you want to pawn the house? y(yes) n(no) ").lower()
        if choise == 'y':
            wallet = board_location['price']
            diference = player['money'] + wallet
            player['money'].update(diference)
            return player['money']
        else:
            print('House NOT powned. ')

def unpawn_house(player, board_location):
    if player['name'] == board_location['owner']:
        choise = input("do you want to un-pawn the house? y(yes) n(no) ").lower()
        if choise == 'y':
            wallet = board_location['price']
            diference = player['money'] - wallet
            player['money'].update(diference)
            return player['money']
        else:
            print('House NOT un-powned. ')


def sell_house(player, board_location):
    if player['name'] == board_location['owner']:
        choise = input("do you want to sell the house? y(yes) n(no) ").lower()
        if choise == 'y':
            wallet = board_location['price']
            diference = player['money'] - wallet
            player['money'].update(diference)
            return player['money']
        else:
            print('House NOT un-powned. ')

