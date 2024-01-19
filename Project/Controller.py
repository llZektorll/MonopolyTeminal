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


def reg_player(players, player_name):
    for player in player_name:
        players = ({"name": player, "position": 0, "money": 1500})
        print(f'Player {player} added correctly.')
        print(players)
    return players


def ComprarPropriedade(CardPosition, Jogador):
    if (SaldoJogadores <= 0):
        print('Saldo insuficiente.')

    if (Board_Position[CardPosition] != CardPosition):
        print('Jogador não esta na Propriedade.')

    if (Board_Position[CardPosition]["owner"] != Jogador):
        print('Propriedade já tem proprietário.')

    if (Board_Position[CardPosition]["owner"] == "Board"):
        Board_Position[CardPosition]["owner"] == Jogador
        print('Propriedade adquirida com sucesso.')


def ConstruirCasa(CardPosition, Jogador):
    if (SaldoJogadores <= 0):
        print('Saldo insuficiente.')

    if (Board_Position[CardPosition]["owner"] != Jogador):
        print('não é proprietário.')

    if (Board_Position[CardPosition]["house"] >= 5):
        print('Propriedade já tem proprietário.')

    if (Board_Position[CardPosition]["owner"] == Jogador):
        print('Casa construida com sucesso.')


def PagarAluguer(JogadorRecpetor, Jogador):
    if (SaldoJogadores[Jogador] <= 0):
        print('Saldo insuficiente.')

    if (Board_Position[CardPosition]["owner"] != JogadorRecpetor):
        print('Receptor não é proprietário.')

    if (Board_Position[CardPosition]["owner"] == JogadorRecpetor):
        SaldoJogadores[JogadorRecpetor] = "valor da casa"
        print('Aluguer pago com sucesso.')


def HipotecarPropriedade(CardPosition, Jogador):
    if (Board_Position[CardPosition]["owner"] != Jogador):
        print('não é proprietário.')

    if (Board_Position[CardPosition]["Hipotecada"] == True):
        print('Propriedade já esta hipotecada.')

    if (Board_Position[CardPosition]["Hipotecada"] == False):
        Board_Position[CardPosition]["Hipotecada"] = True
        print('Propriedade hipotecada com sucesso.')


def DeshipotecarPropriedade(CardPosition, Jogador):
    if (Board_Position[CardPosition]["owner"] != Jogador):
        print('não é proprietário.')

    if (Board_Position[CardPosition]["Hipotecada"] == False):
        print('Propriedade  não esta hipotecada.')

    if (SaldoJogadores[Jogador] <= 0):
        print('Saldo insuficiente.')

    if (Board_Position[CardPosition]["Hipotecada"] == True):
        Board_Position[CardPosition]["Hipotecada"] = False
        print('Propriedade deshipotecada com sucesso.')


def VenderCasa(CardPosition, Jogador):
    if (Board_Position[CardPosition]["owner"] != Jogador):
        print('não é proprietário.')

    if (Board_Position[CardPosition]["house"] <= 0):
        print('Sem casas para vender.')

    if (Board_Position[CardPosition]["house"] < 0):
        print('Casas vendida com sucesso.')
