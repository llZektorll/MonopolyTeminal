'''
    Registration of users
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
# Automatic Roll the Dice
def rolldice():
    global a,b
    a = random.randint(1,6)
    b = random.randint(1,6)
    total = a + b
    return total

#Create Users
def reg_player(name):
    if check_player(players, name) == True:
        return False
    else:
        player = {'Name': name, 'Wins': 0, 'Games': 0}
        players.append(player)
        return players


def check_player(players, name):
    for player in players:
        if player['Name'] == name:
            return True
    return False


def escrita_ficheiros(file_1, dados):

    arquivo = open(file_1, "w")
    arquivo.write(dados)
    arquivo.close()


def ler_ficheiro(file_1, dados):

    arquivo = open(file_1, encoding="utf8")
    linhas = arquivo.read()
    arquivo.close()
    return linhas

