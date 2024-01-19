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
    with open("data1.json", "w") as file:
        json.dump(players, file)


def load_data():
    try:
        with open("data1.json", "r") as file:
            return json.load(file)
    except (json.JSONDecodeError):
        return []


def dice_roll():
    roll = random.randint(1, 6) + random.randint(1, 6)
    return roll


def reg_player(players, player_name):
    for player in player_name:
        players = ({"name": player, "position": 0, "money": 1500})
        print(f'Player {player} added correctly.')
        print(players)
    return players


def comprar_propriedade(board_position, player):
    if (player['money'] <= 0):
        print('Insufficient funds.')
    if (board_position[CardPosition]["owner"] != player):
        print('Propriedade já tem proprietário.')
    if (board_position[CardPosition]["owner"] == "Board"):
        board_position[CardPosition]["owner"] == Jogador
        print('Propriedade adquirida com sucesso.')


def ConstruirCasa(CardPosition, Jogador):
    if (SaldoJogadores <= 0):
        print('Saldo insuficiente.')

    if (board_position[CardPosition]["owner"] != Jogador):
        print('não é proprietário.')

    if (board_position[CardPosition]["house"] >= 5):
        print('Propriedade já tem proprietário.')

    if (board_position[CardPosition]["owner"] == Jogador):
        print('Casa construida com sucesso.')


def PagarAluguer(JogadorRecpetor, Jogador):
    if (SaldoJogadores[Jogador] <= 0):
        print('Saldo insuficiente.')

    if (board_position[CardPosition]["owner"] != JogadorRecpetor):
        print('Receptor não é proprietário.')

    if (board_position[CardPosition]["owner"] == JogadorRecpetor):
        SaldoJogadores[JogadorRecpetor] = "valor da casa"
        print('Aluguer pago com sucesso.')


def HipotecarPropriedade(CardPosition, Jogador):
    if (board_position[CardPosition]["owner"] != Jogador):
        print('não é proprietário.')

    if (board_position[CardPosition]["Hipotecada"] == True):
        print('Propriedade já esta hipotecada.')

    if (board_position[CardPosition]["Hipotecada"] == False):
        board_position[CardPosition]["Hipotecada"] = True
        print('Propriedade hipotecada com sucesso.')


def DeshipotecarPropriedade(CardPosition, Jogador):
    if (board_position[CardPosition]["owner"] != Jogador):
        print('não é proprietário.')

    if (board_position[CardPosition]["Hipotecada"] == False):
        print('Propriedade  não esta hipotecada.')

    if (SaldoJogadores[Jogador] <= 0):
        print('Saldo insuficiente.')

    if (board_position[CardPosition]["Hipotecada"] == True):
        board_position[CardPosition]["Hipotecada"] = False
        print('Propriedade deshipotecada com sucesso.')


def VenderCasa(CardPosition, Jogador):
    if (board_position[CardPosition]["owner"] != Jogador):
        print('não é proprietário.')

    if (board_position[CardPosition]["house"] <= 0):
        print('Sem casas para vender.')

    if (board_position[CardPosition]["house"] < 0):
        print('Casas vendida com sucesso.')
