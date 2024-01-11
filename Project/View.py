def main():
    #region Variables
    players = {}
    board = 4 # 4x4
    house = 5
    board_id = (1,2,3,4,5,6,7,8,9,10,11,12)
    bord_house = (3,5,7,9,11)
    player_location = {'player1': 1, 'player2': 1, 'player3':5}
    #endregion
    #region menu
    print(f'''
##########################
###  Jogo do Monopólio ###
##########################

1 - Novo Jogo
2 - Registar Jogadores
3 - Histórico de jogos
''')
    
    #endregion menu
    option = input(int(f'Selectione uma opção: '))
    if option == 1:
        print ('test')
    elif option == 2:
        print ('test 2')
    elif option == 3:
        print ('test3')
    else :
        print(f'Opção selecionada não é válida!')