import random
import json
import os


# Load information from file


def load_file():
    try:
        with open('data.json', 'r') as file:
            players = json.load(file)
    except json.decoder.JSONDecodeError:
        players = []
    return players

# Save player information


def save_file(players):
    with open('data.json', 'w') as file:
        json.dump(players, file)

# Register player


def reg_player(players):
    used_names = []
    
    while True:
        try:
            number_players = int(input('Quantas pessoas vão jogar? '))
            if 2 <= number_players <= 4:
                break
            else:
                print('Número inválido. O número de jogadores deve estar entre 2 e 4.')
        except ValueError:
            print('Valor inválido. Insira um número inteiro válido entre 2 e 4.')

    for count in range(number_players):
        while True:
            player_name = input(f'Indique o nome do jogador {count + 1}: ')
            if player_name.strip() != '' and player_name not in used_names:
                used_names.append(player_name)
                break
            elif player_name in used_names:
                print('Este nome já está a ser utilizado. Escolha outro nome.')
            else:
                print('Nome não pode estar em branco.')

        players.append({"name": player_name.strip(), "position": 0, "money": 1500,
                        "properties": 0, "games_won": 0, "games_played": 0})





# Display board


def display_board(board):
    os.system('cls')
    print('\n Tabuleiro do Monopolio ......')
    for i, property in enumerate(board):
        owner_info = (f'Owner: {property["owner"]}')
        if property['pawn'] == True:
            owner_info += " (Penhorado)"

        # Adjust the formatting of the index based on the number of digits
        if i < 10:
            index_format = f"{i}.  "
        else:
            index_format = f"{i}. "

        # Use format specifiers to specify a fixed width for the name
        print(
            f"{index_format}{property['name']:<30} - {property['price']:>3}$ - {owner_info} - Houses: {property['house']}")
    print()

# Pay Rent


def pay_rent(player, owner, rent_amount):
    player['money'] -= rent_amount
    print(
        f"{player['name']} pagou €{rent_amount} em renda ao jogador {owner}.")

# Buy Property


def buy_property(player, property):
    property['owner'] = player['name']
    player['money'] -= property['price']
    player['properties'] += 1
    print(
        f"{player['name']} comprou {property['name']} por €{property['price']}.")

#  Build a house


def build_house(player, property):
    property['house'] += 1
    player['money'] -= 100
    print(f"{player['name']} construiu casa em {property['name']}.")

# Pawn Property


def pawn_property(player, property):
    property['pawn'] = True
    print(
        f"{player['name']} hipotecou {property['name']}.A renda agora é €0.")

# Buy back the property


def buy_back_property(player, property):
    property['pawn'] = False
    player['money'] -= property['price']
    print(
        f"{player['name']} desipotecou a {property['name']} por €{property['price']}.")

# Sell house


def sell_house(player, property):
    property['house'] -= 1
    player['money'] += property['price']
    print(
        f"{player['name']} vendou uma casa em {property['name']} por €{property['price']}.")

# Check Winner


def check_winner(board, players):
    board_status = 0
    for location in board:
        if location['owner'] == None:
            continue
        else:
            board_status += 1
    if board_status == 13:
        bubble_sort(players)
        for p in players:
            if p == players[0]:
                p['games_won'] += 1
                p['games_played'] += 1
                print(f"Parabéns, {p['name']}! Ganhou o jogo!")
                print('És uma máquina e o yoda é o rei!')
            else:
                p['games_played'] += 1
        save_file(players)
        quit()


# Order players

def bubble_sort(players):
    for i in range(len(players)):
        for j in range(0, len(players)-i-1):
            if players[j]['properties'] < players[j+1]['properties']:
                temp = players[j+1]
                players[j+1] = players[j]
                players[j] = temp
                players

# Dice Roll


def dice_roll():
    roll = random.randint(1, 6) + random.randint(1, 6)
    return roll


# Player turn
def play_turn(player, board, players):
    roll = dice_roll()
    print(f"É a vez do jogador {player['name']}.")
    print(f"Lancamento do dado: {roll}")
    print(f'Dinheiro: {player["money"]}')

    player['position'] = (player['position'] + roll) % len(board)
    current_property = board[player['position']]

    print(f"{player['name']} ficou na casa {current_property['name']}")

    if not current_property['owner']:
        buy_property_option = 1
        while buy_property_option == 1:
            print(
                f"{current_property['name']} não tem proprietário. Quer comprar?")
            response = input("Introduz 1 para sim e 2 para não: ")
            if response == "1" and player['money'] >= current_property['price']:
                buy_property(player, current_property)
                buy_property_option = 0
            elif response == "1" and player['money'] < current_property['price']:
                print('Sem capital para efectuar a compra')
                input('Carregue em qualquer botão para continuar')
            elif response == "2":
                print('Propriedade não comprada')
                input('Carregue em qualquer botão para continuar')
                buy_property_option = 0
            else:
                print('Resposta inválida!')
    elif current_property['owner'] == player['name'] and current_property['pawn'] != True:
        while True:
            print(
                f"{player['name']}, qual é a tua ação na propriedade {current_property['name']}?")
            print("1. Construir Casa")
            print("2. Hipotecar Propriedade")
            print("3. Vender Casa")
            choice = input("Selecione uma opção: ")
            if choice == '1' and player['money'] >= 100:
                build_house(player, current_property)
                break  # Exit the loop after a valid choice
            if choice == '1' and player['money'] < 100:
                print('Não tem capital para a compra')
            elif choice == '2':
                pawn_property(player, current_property)
                break  # Exit the loop after a valid choice
            elif choice == '3' and current_property['house'] > 0:
                sell_house(player, current_property)
                break  # Exit the loop after a valid choice
            elif choice =='3' and current_property['house'] == 0:
                print('Não tem casas para vender')
            else:
                print('Opção inválida. Tente novamente.')

    elif current_property['pawn'] == True and current_property['owner'] == player['name']:
        while True:
            print(
                f"{current_property['name']} está hipotecada. Quer desipoteca-la?")
            response = input("Selecione 1 para 'SIM' e 2 para 'NÃO': ").lower()
            if response == '1' and player['money'] >= current_property['price']:
                buy_back_property(player, current_property)
                return
            elif response == '2':
                print('Propriedade não foi desipotecada')
                return
            else:
                print('Opção inválida')
    elif current_property['pawn'] == True and current_property['owner'] != player['name']:
        print(
            f"{current_property['name']} é do jogador {current_property['owner']}.")
        input('Pressione enter para continuar')
    else:
        rent_amount = current_property['rent']
        print(
            f"{player['name']}, ficou na casa {current_property['name']} que pertence ao jogador {current_property['owner']}.")
        print(f"Deve €{rent_amount} de renda.")
        if player['money'] >= rent_amount:
            pay_rent(player, current_property['owner'], rent_amount)
        else:
            print(
                f"{player['name']} não tem dinheiro suficiente para pagar o aluger. O aluguer não é cobrado..")


# Play the game


def play_game(players, current_player, board):
    while True:
        player = players[current_player]
        display_board(board)
        play_turn(player, board, players)
        check_winner(board, players)
        

        current_player = (current_player + 1) % len(players)
