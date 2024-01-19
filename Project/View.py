from Controller import *


def main():

    player_info_file = "c:/file.json"

    # region Variables
    players = []
    player_name = []
    roll = 0
    board_position = {
        0: {
            "position": "0",
            "name": "Casa de Partida",
            "color": "white",
            "price": "200",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        1: {
            "position": "1",
            "name": "Campo Grande",
            "color": "Purple",
            "price": "60",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        2: {
            "position": "2",
            "name": "Caixa da Comunidade",
            "color": "White",
            "price": "0",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        3: {
            "position": "3",
            "name": "Rua Faria Guimarães",
            "color": "Purple",
            "price": "60",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        4: {
            "position": "4",
            "name": "Pague imposto sobre Capitais",
            "color": "White",
            "price": "200",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        5: {
            "position": "5",
            "name": "Estação do Rossio",
            "color": "Black",
            "price": "200",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        6: {
            "position": "6",
            "name": "Alamenda das linhas de Torres",
            "color": "Cyan",
            "price": "100",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        7: {
            "position": "7",
            "name": "Sorte",
            "color": "White",
            "price": "0",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        8: {
            "position": "8",
            "name": "Avenida das Nações Unidas",
            "color": "Cyan",
            "price": "100",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        9: {
            "position": "9",
            "name": "Avenida 24 de Julho",
            "color": "Cyan",
            "price": "120",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        10: {
            "position": "10",
            "name": "Cadeia",
            "color": "White",
            "price": "0",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        11: {
            "position": "11",
            "name": "Avenida Central",
            "color": "Purple",
            "price": "140",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        12: {
            "position": "12",
            "name": "Companhia de Electricidade",
            "color": "White",
            "price": "150",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
        13: {
            "position": "13",
            "name": "Rua Ferreira Borges",
            "color": "Purple",
            "price": "140",
            "owner": "Board",
            "house": 0,
            "pawn": "no"},
    }

    # endregion
    while True:
        # region menu
        print(f'''
    ##########################
    ###  Jogo do Monopólio ###
    ##########################

    1 - Novo Jogo
    2 - Histórico de jogos
    9 - Sair
    ''')

        # endregion menu
        option = int(input(f'Selectione uma opção: '))
        if option == 1:
            while True:
                if len(players) < 2:
                    player_name_1 = input("What is the player 1 name? ")
                    player_name_2 = input("What is the player 2 name? ")
                    player_name_3 = input("What is the player 3 name? ")
                    player_name = (player_name_1, player_name_2, player_name_3)
                    run_player = reg_player(players, player_name)
                    print(run_player)
                    continue

        elif option == 2:
            print('test 2')
        elif option == 9:
            quit()
        else:
            print(f'Opção selecionada não é válida!')
