import random
from xml.dom.expatbuilder import parseString
import pandas as pd


df = pd.DataFrame()

players = []
num_players = 0



####################

# ADICIONAR RODADAS, POIS TODOS OS JOGADORES DEVEM JOGAR, e SE NAQUELA RODADA
# GANHAR QUE CONSEGUIR MAIS CEREBROS, SE SAIR MAIS DE 13

#############


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
dices_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
available_dices = ['d1', 'd2', 'd3', 'd4', 'd5','d6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13']
count_players = 0
winner = None  # variável que armazena o nome do vencedor

while True:
    try:
        num_players = int(input('Informe a quantidade de jogadores: '))

        if num_players < 2:
                print('A quantidade de jogadores deve ser igual ou maior que dois!)
                      
    except ValueError:
        print('Por favor, entre com um número!')


for i in range(0, num_players):
    players.append([input(f'Digite o nome do jogador número {count_players+1}: '), 0, 0, 0, 0])
    count_players += 1

df = pd.DataFrame(players, columns=['PLAYER', 'C', 'E', 'P', 'PLAYS'])
print(df)


# DEFININDO RANDOMICAMENTE O JOGADOR INICIAL
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

def check_win():
    for i, j in df.iterrows():
        if j['C'] == 13:
            return j['PLAYER']

def next_player(index):
    if index != df.tail(1).index[0]:
        index += 1
    else:
        index = 0
    return index

def check_shots():
    for i, j in df.iterrows():
        if j['E'] == 3:
            return i

def remove_dice(available_dices, dice, dices_numbers, dice_number):
    available_dices.remove(dice)
    dices_numbers.remove(int(dice_number))

# JOGADA

# ROLAR OS DADOS
# REGISTRAR OS PONTOS
# VERIFICAR SE VENCEU
# SE NAO VENCEU VERIFICAR SE ACUMULOU 3 ESPINGAS
# SE NAO ACUMULOU VERIFICAR SE QUER JOGAR DE NOVO

# ROLANDO OS DADOS
while winner == None:
    print(f'DADOS DISPONIVEIS: {available_dices}')
    p = df.iloc[index]['PLAYER']
    input(f'Jogador {p}, role os dados')

    # DETERMINA RANDOMICAMENTE O DADO
    dice_number = str(random.choice(dices_numbers))
    dice = 'd' + dice_number

    
    play(dice)  # registra os pontos
    

    df.loc[index, ['PLAYS']] = df.loc[index, ['PLAYS']] + 1  # registra a jogada
    print(df)

    if df.loc[index]['E'] == 3:
        print('LEVOU 3 TIROS, SEUS CEREBROS SERÃO ZERADOS E VOCÊ DEVE PASSAR A VEZ')
        df.loc[index, ['E']] = 0
        df.loc[index, ['C']] = 0
        df.loc[index, ['P']] = 0
        index = next_player(index)

    remove_dice(available_dices, dice, dices_numbers, dice_number)  # remove o dado sorteado dos dados disponíveis
    play_again = input('VOCÊ QUER JOGAR NOVAMENTE (S/N)? ').lower()

    if play_again == 'n':
        index = next_player(index)
        available_dices = ['d1', 'd2', 'd3', 'd4', 'd5','d6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13']
        dices_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        

    winner = check_win()
    


print(f'O JOGADOR VENCEDOR É {winner}')
print('FIM DO JOGO')



# def check_lose():
#     pass

# def check_play_again():
#     pass

# def check_tie():
#     pass




