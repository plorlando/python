import random
import pandas as pd


df = pd.DataFrame()

players = []
num_players = 0

# CONFIGURACOES INICIAIS DO JOGO
print('*********************************')
print('ZOMBIE DICE')
print('São necessários pelo menos 2 jogadores para pode jogar Zombie Dice.')
print('*********************************\n')

green = ("C", "E", "C", "P", "C", "P")
yellow = ("C", "E", "P", "C", "E", "P")
red = ("E", "p", "E", "C", "E", "P")
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

count_players = 0

num_players = int(input('Quantas pessoas irão jogar? '))

for i in range(0, num_players):
    players.append([input(f'Digite o nome do jogador número {count_players+1}: '), 0, 0, 0])
    count_players += 1

df = pd.DataFrame(players, columns=['PLAYER', 'C', 'E', 'P'])
print(df)


# DEFININDO O JOGADOR INICIAL
iplayer = df.sample(replace=False)

p = iplayer.iloc[0]['PLAYER']
index = iplayer.index[0]
print(index)

# ROLANDO OS DADOS
print(f'Jogador {p}, role os dados')

# df.loc[index, ['C']] = 1
# df.loc[index, ['E']] = 2
# df.loc[index, ['P']] = 3


# DEFINIÇÃO DE VARIÁVEIS E FUNCOES
# 2 a 99 jogadores

dice_number = str(random.randrange(1, 14))

dice = 'd' + dice_number

match dice:
    case 'd1':
        face = random.sample(green, 1)
        print(f'd1, {face}')
    case 'd2':
        face = random.sample(green, 1)
        print(f'd2, {face}')
    case 'd3':
        face = random.sample(green, 1)
        print(f'd3, {face}')
    case 'd4':
        face = random.sample(green, 1)
        print(f'd4, {face}')
    case 'd5':
        face = random.sample(green, 1)
        print(f'd5, {face}')
    case 'd6':
        face = random.sample(green, 1)
        print(f'd7, {face}')    
    case 'd7':
        face = random.sample(yellow, 1)
        print(f'd7, {face}')
    case 'd8':
        face = random.sample(yellow, 1)
        print(f'd8, {face}')
    case 'd9':
        face = random.sample(yellow, 1)
        print(f'd9, {face}')
    case 'd10':
        face = random.sample(yellow, 1)
        print(f'd10, {face}')
    case 'd11':
        face = random.sample(red, 1)
        print(f'd11, {face}')
    case 'd12':
        face = random.sample(red, 1)
        print(f'd12, {face}')
    case 'd13':
        face = random.sample(red, 1)
        print(f'd13, {face}')
    case _:
        print('default')



df.loc[index, face] = df.loc[index, face] + 1
print(df)



# def play():
#     # deve ser sorteados 3 dados por jogada, cada um deles representa uma vitima atacada
#     # fazer um random para determinar qual dado foi sorteado
#     # fazer um segundo random dentro do dado sorteado para sortear a face do dado
#     # somar o ponto sorteado nos pontos do jogador
#     pass

# def score():
#     # deve ser registrado o ponto no dict, com o nome da pessoa e qual faze saiu
#     # a cada ponto deve verificar condição de: 1-vitória, 2-derrota, e se nenhuma acontecer se ele quer jogar novamente
#     pass

# def check_win():
#     pass

# def check_lose():
#     pass

# def check_play_again():
#     pass

# def check_tie():
#     pass




