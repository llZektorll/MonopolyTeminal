from Controller import *


def main():
    players = []
    current_player = 0
    board = [
        {"name": "Primeira Casa", "price": 200,
            "owner": None, "house": 0, "pawn": False, "rent": 20},
        {"name": "Campo Grande", "price": 60, "owner": None,
            "house": 0, "pawn": False, "rent": 6},
        {"name": "Caixa da Comunidade", "price": 10,
            "owner": None, "house": 0, "pawn": False, "rent": 1},
        {"name": "Rua Faria Guimarães", "price": 60,
         "owner": None, "house": 0, "pawn": False, "rent": 6},
        {"name": "Pague imposto sobre Capitais", "price": 200,
            "owner": None, "house": 0, "pawn": False, "rent": 20},
        {"name": "Estação do Rossio", "price": 200,
            "owner": None, "house": 0, "pawn": False, "rent": 20},
        {"name": "Alamenda das linhas de Torres", "price": 100,
            "owner": None, "house": 0, "pawn": False, "rent": 10},
        {"name": "Tasca do Zé", "price": 10, "owner": None,
            "house": 0, "pawn": False, "rent": 1},
        {"name": "Avenida das Nações Unidas", "price": 100,
            "owner": None, "house": 0, "pawn": False, "rent": 10},
        {"name": "Avenida 24 de Julho", "price": 120,
            "owner": None, "house": 0, "pawn": False, "rent": 12},
        {"name": "Hotel Moinas", "price": 10, "owner": None,
            "house": 0, "pawn": False, "rent": 1},
        {"name": "Avenida Central", "price": 140,
            "owner": None, "house": 0, "pawn": False, "rent": 14},
        {"name": "Companhia de Electricidade", "price": 150,
            "owner": None, "house": 0, "pawn": False, "rent": 15},
        {"name": "Rua Ferreira Borges", "price": 140,
            "owner": None, "house": 0, "pawn": False, "rent": 14},
    ]
    print('''
##########################
###  Jogo do Monopólio ###
##########################

9 - Sair
1 - Novo Jogo
2 - Histórico de jogos
''')
    menu_option = input('Escolha uma opção: ')
    if menu_option == "1":
        reg_player(players)
        play_game(players, current_player, board)
        main()
    if menu_option == "2":
        player_history = load_file()
        print(player_history)
        main()
    if menu_option == "9":
        quit()
    else:
        print('Opção inválida')
        main()
