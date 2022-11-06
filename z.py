import pandas as pd
import random


####################

# ADICIONAR RODADAS, POIS TODOS OS JOGADORES DEVEM JOGAR, e SE NAQUELA RODADA
# GANHAR QUE CONSEGUIR MAIS CEREBROS, SE SAIR MAIS DE 13

#############


# CONFIGURACOES INICIAIS DO JOGO
print('\033[1:31;107m====================================================\033[m')
print('ZOMBIE DICE')
print('São necessários pelo menos 2 jogadores para pode jogar Zombie Dice.')
print('\033[1:31;107m====================================================\033[m\n')


# DEFINIÇÃO DE VARIÁVEIS INICIAIS
df = pd.DataFrame()  # criação de um dataframe vazio
players = []  # dicionário vazio para armazenar o nome dos jogadores
num_players = 0
dices_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
available_dices = ['d1', 'd2', 'd3', 'd4', 'd5','d6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13']
count_players = 0
winner = None  # variável que armazena o nome do vencedor
game_on = True


# DEFINIÇÃO DE VARIÁVEIS AUXILIARES
green = ('C', 'E', 'C', 'P', 'C', 'P')
yellow = ('C', 'E', 'P', 'C', 'E', 'P')
red = ('E', 'P', 'E', 'C', 'E', 'P')

# FUNCOES
def play(dice):
    match dice:
        case 'd1':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1  # df.loc[index, ['C']] = 1
            print(f'DADO SORTEADO: VERDE, face {face[0]}')
        case 'd2':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: VERDE, face {face[0]}')
        case 'd3':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: VERDE, face {face[0]}')
        case 'd4':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: VERDE, face {face[0]}')
        case 'd5':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: VERDE, face {face[0]}')
        case 'd6':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: VERDE, face {face[0]}')
        case 'd7':
            face = random.sample(yellow, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: AMARELO, face {face[0]}')
        case 'd8':
            face = random.sample(yellow, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: AMARELO, face {face[0]}')
        case 'd9':
            face = random.sample(yellow, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: AMARELO, face {face[0]}')
        case 'd10':
            face = random.sample(yellow, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: AMARELO, face {face[0]}')
        case 'd11':
            face = random.sample(red, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: VERMELHO, face {face[0]}')
        case 'd12':
            face = random.sample(red, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: VERMELHO, face {face[0]}')
        case 'd13':
            face = random.sample(red, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: VERMELHO, face {face[0]}')
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

def remove_dice(available_dices, dice):
    available_dices.remove(dice)


# WHILE QUE ENGLOBA TODO O JOGO
while game_on == True:    
    try:
        num_players = int(input('Informe a quantidade de jogadores (digite 0 se quiser sair do jogo): '))
        if num_players <= 0:
            game_on = False
        elif num_players == 1:
            print('O jogo deve ter 2 ou mais jogadores\n')
            game_on = True
        elif num_players >= 2:
            for i in range(0, num_players):
                players.append([input(f'Digite o nome do jogador número {count_players+1}: '), 0, 0, 0, 0])
    except ValueError:
        print('Por favor, entre com um número inteiro!')


    # CONVERS   ÃO DA LISTA CRIADA EM UM DATAFRAME DO PANDAS PARA REGISTRO ESTATÍSTICO DAS JOGADAS
    df = pd.DataFrame(players, columns=['PLAYER', 'C', 'E', 'P', 'PLAYS'])
    print(df)


    # DEFININDO RANDOMICAMENTE O JOGADOR INICIAL
    iplayer = df.sample(replace=False)  # seleciona randomicamente o primeiro jogador
    p = iplayer.iloc[0]['PLAYER']  # armazena o nome do jogador
    index = iplayer.index[0]  # armazena o indice do jogador
    print(index, p)  # essa variável armazena o numero do jogador atual através do índice do dataframe

# JOGADA

# ROLAR OS DADOS
# REGISTRAR OS PONTOS

# VERIFICACOES:
# 1. se alguem atingiu 13 pontos, assim vencendo o jogo
# 2. se o jogador atual levou 3 tiros, perdendo assim sua vez
# 2.1. se o jogador levou 3 tiros perde a vez, e assim zera tudo dele (conferir essa regra)
# 3. se o jogador atual quer passar a vez
# 4. se tem dados disponíveis no tubos, se não ele tem que passar a vez

    # ROLANDO OS DADOS
    while winner == None:

        p = df.iloc[index]['PLAYER']  # armazena o nome do jogador atual
        input(f'Jogador {p}, role os dados - DADOS DISPONIVEIS: {available_dices}')

        # DETERMINA RANDOMICAMENTE O DADO
        dice = str(random.choice(available_dices))

        play(dice)  # registra os pontos
        

        df.loc[index, ['PLAYS']] = df.loc[index, ['PLAYS']] + 1  # registra a jogada
        print(df)
        print()

        if df.loc[index]['E'] == 3:
            print('LEVOU 3 TIROS, SEUS CEREBROS SERÃO ZERADOS E VOCÊ DEVE PASSAR A VEZ')
            df.loc[index, ['E']] = 0
            df.loc[index, ['C']] = 0
            df.loc[index, ['P']] = 0
            index = next_player(index)

        remove_dice(available_dices, dice)  # remove o dado sorteado dos dados disponíveis

        if len(available_dices) <= 0:
            print(f'Jogador {p}, acabaram seus dados, você deve passar a vez')
            play_again = 'n'
        else:
            play_again = input('VOCÊ QUER JOGAR NOVAMENTE (S/N)? ').lower()

        if play_again == 'n':
            index = next_player(index)
            available_dices = ['d1', 'd2', 'd3', 'd4', 'd5','d6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13']
            

        winner = check_win()

        if winner != None:
            print(f'O JOGADOR VENCEDOR É {winner}')
            game_on = False


print('FIM DO JOGO')
print('OBRIGADO')




