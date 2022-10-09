import random
from xml.dom.expatbuilder import parseString
import pandas as pd


df = pd.DataFrame()

players = []
num_players = 0

# CONFIGURACOES INICIAIS DO JOGO
print('*********************************')
print('ZOMBIE DICE')
print('São necessários pelo menos 2 jogadores para pode jogar Zombie Dice.')
print('*********************************\n')

green = ('C', 'E', 'C', 'P', 'C', 'P')
yellow = ('C', 'E', 'P', 'C', 'E', 'P')
red = ('E', 'P', 'E', 'C', 'E', 'P')
# d1 = green
# d2 = green
# d3 = green
# d4 = green
# d5 = green
# d6 = green
# d7 = yellow
# d8 = yellow
# d9 = yellow
# d10 = yellow
# d11 = red
# d12 = red
# d13 = red
rolled_dices = []
count_players = 0
winner = None  # variável que armazena o nome do vencedor

while True:
    try:
        num_players = int(input('Quantas pessoas vão jogar? '))
        break
    except ValueError:
        print('Por favor, entre com um número!')


for i in range(0, num_players):
    players.append([input(f'Digite o nome do jogador número {count_players+1}: '), 0, 0, 0, 0])
    count_players += 1

df = pd.DataFrame(players, columns=['PLAYER', 'C', 'E', 'P', 'PLAYS'])
print(df)


# DEFININDO RANDIMICAMENTE O JOGADOR INICIAL
iplayer = df.sample(replace=False)  # seleciona randimicamente o primeiro jogador
p = iplayer.iloc[0]['PLAYER']  # armazena o nome do jogador
index = iplayer.index[0]  # armazena o indice do jogador
print(index, p)  # essa variável armazena o numero do jogador atual através do índice do dataframe

# FUNCOES
def play(dice):
    match dice:
        case 'd1':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1  # df.loc[index, ['C']] = 1
            print(f'DADO: VERDE, face {face[0]}')
        case 'd2':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: VERDE, face {face[0]}')
        case 'd3':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: VERDE, face {face[0]}')
        case 'd4':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: VERDE, face {face[0]}')
        case 'd5':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: VERDE, face {face[0]}')
        case 'd6':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: VERDE, face {face[0]}')
        case 'd7':
            face = random.sample(yellow, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: AMARELO, face {face[0]}')
        case 'd8':
            face = random.sample(yellow, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: AMARELO, face {face[0]}')
        case 'd9':
            face = random.sample(yellow, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: AMARELO, face {face[0]}')
        case 'd10':
            face = random.sample(yellow, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: AMARELO, face {face[0]}')
        case 'd11':
            face = random.sample(red, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: VERMELHO, face {face[0]}')
        case 'd12':
            face = random.sample(red, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: VERMELHO, face {face[0]}')
        case 'd13':
            face = random.sample(red, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: VERMELHO, face {face[0]}')
        case _:
            print('default')

    rolled_dices.append(dice)

def check_win():
    c = df.loc[[index]]
    
    for i, j in df.iterrows():
        if j['C'] == 13:
            return j['PLAYER']

def next_player(index):
    if index != df.tail(1).index[0]:
        index += 1
    else:
        index = 0
    return index

# JOGADA

# ROLAR OS DADOS
# REGISTRAR OS PONTOS
# VERIFICAR SE VENCEU
# SE NAO VENCEU VERIFICAR SE ACUMULOU 3 ESPINGAS
# SE NAO ACUMULOU VERIFICAR SE QUER JOGAR DE NOVO

# ROLANDO OS DADOS
while winner == None:
    input(f'Jogador {p}, role os dados')
    dice_number = str(random.randrange(1, 14))  # determina ramdomicamente o dado
    dice = 'd' + dice_number  # armazena o dado atual
    play(dice)  # registra os pontos
    df.loc[index, ['PLAYS']] = df.loc[index, ['PLAYS']] + 1  # registra a jogada
    print(df)
    index = next_player(index)
    print(index)
    winner = check_win()
    


print(f'O JOGADOR VENCEDOR É {winner}')
print('FIM DO JOGO')


# def score():
#     # deve ser registrado o ponto no dict, com o nome da pessoa e qual faze saiu
#     # a cada ponto deve verificar condição de: 1-vitória, 2-derrota, e se nenhuma acontecer se ele quer jogar novamente
#     pass



# def check_lose():
#     pass

# def check_play_again():
#     pass

# def check_tie():
#     pass




