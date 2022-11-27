### IMPORTANTE ###
# Esse código somente roda em PYTHON 3.10 ou superior, por causa da função MATCH
# ALUNO: PEDRO LOR ORLANDO

import os
import pandas as pd
from colorama import Fore, Back, Style, init, deinit
import random

clear = lambda: os.system('cls')
clear()

# DEFINIÇÃO DE VARIÁVEIS INICIAIS
df = pd.DataFrame()  # criação de um dataframe vazio
players = []  # dicionário vazio para armazenar o nome dos jogadores
num_players = 0  # variável que vai armazenar o numero de zogadores
dices_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
available_dices = ['d1', 'd2', 'd3', 'd4', 'd5','d6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13']
count_players = 0
winner = None  # variável que armazena o nome do vencedor
game_on = True

# DEFINIÇÃO DAS VARIÁVEIS QUE REPRESENTAM OS DADOS
green = ('CEREBRO', 'TIRO', 'CEREBRO', 'PASSO', 'CEREBRO', 'PASSO')
yellow = ('CEREBRO', 'TIRO', 'PASSO', 'CEREBRO', 'TIRO', 'PASSO')
red = ('TIRO', 'PASSO', 'TIRO', 'CEREBRO', 'TIRO', 'PASSO')

def play(dice, df, green, yellow, red, index):
    match dice:
        case 'd1':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1  # df.loc[index, ['CEREBRO']] = 1
            print(f'DADO SORTEADO: {Fore.GREEN}VERDE{Style.RESET_ALL}, FACE: {face[0]}')
        case 'd2':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: {Fore.GREEN}VERDE{Style.RESET_ALL}, FACE: {face[0]}')
        case 'd3':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: {Fore.GREEN}VERDE{Style.RESET_ALL}, FACE: {face[0]}')
        case 'd4':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: {Fore.GREEN}VERDE{Style.RESET_ALL}, FACE: {face[0]}')
        case 'd5':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: {Fore.GREEN}VERDE{Style.RESET_ALL}, FACE: {face[0]}')
        case 'd6':
            face = random.sample(green, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: {Fore.GREEN}VERDE{Style.RESET_ALL}, FACE: {face[0]}')
        case 'd7':
            face = random.sample(yellow, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: {Fore.YELLOW}AMARELO{Style.RESET_ALL}, FACE: {face[0]}')
        case 'd8':
            face = random.sample(yellow, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: {Fore.YELLOW}AMARELO{Style.RESET_ALL}, FACE: {face[0]}')
        case 'd9':
            face = random.sample(yellow, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: {Fore.YELLOW}AMARELO{Style.RESET_ALL}, FACE: {face[0]}')
        case 'd10':
            face = random.sample(yellow, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO: {Fore.YELLOW}AMARELO{Style.RESET_ALL}, FACE: {face[0]}')
        case 'd11':
            face = random.sample(red, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: {Fore.RED}VERMELHO{Style.RESET_ALL}, FACE: {face[0]}')
        case 'd12':
            face = random.sample(red, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: {Fore.RED}VERMELHO{Style.RESET_ALL}, FACE: {face[0]}')
        case 'd13':
            face = random.sample(red, 1)
            df.loc[index, face] = df.loc[index, face] + 1
            print(f'DADO SORTEADO: {Fore.RED}VERMELHO{Style.RESET_ALL}, FACE: {face[0]}')
        case _:
            print('default')
    print('\n')

# essa função verifica se tem alguém com 13 pontos nos cérebros, determinando assim um vencedor
def check_win(df):
    for i, j in df.iterrows():
        if j['CEREBRO'] == 13:
            return j['PLAYER']


def next_player(index, df):
    if index != df.tail(1).index[0]:
        index += 1
    else:
        index = 0
    return index


def check_shots(df):
    for i, j in df.iterrows():
        if j['TIRO'] == 3:
            return i


def record_the_move(index, df):
    df.loc[index, ['PLAYS']] = df.loc[index, ['PLAYS']] + 1


# Essa função remove da lista de dados disponíveis o dado sorteado
def remove_dice(available_dices, dice):
    available_dices.remove(dice)


# ESSA FUNCAO DETERMINA RANDOMICAMENTE O DADO COM BASE NOS DADOS DISPONÍVEIS
def set_dice(available_dices):
    dice = str(random.choice(available_dices))
    return dice

init()
print(Fore.WHITE + Back.GREEN + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' + Style.RESET_ALL)
print()
print('ZOMBIE DICE')
print('São necessários pelo menos 2 jogadores para pode jogar Zombie Dice.')
print()
print(Fore.WHITE + Back.GREEN + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n' + Style.RESET_ALL)

# FUNCOES
# A função play registra o ponto no DataFrame(DF) localizando o índice do jogador atual e qual a face que foi sorteada


# WHILE QUE ENGLOBA TODO O JOGO
while game_on == True:    
    try:
        num_players = int(input('Informe a quantidade de jogadores (digite 0 se quiser sair do jogo): '))
        print('\n')
        if num_players <= 0:
            game_on = False
            break
        elif num_players == 1:
            print('O jogo deve ter 2 ou mais jogadores\n')
            game_on = True
        elif num_players >= 2:
            for i in range(0, num_players):
                players.append([input(f'Digite o nome do jogador número {count_players+1}: '), 0, 0, 0, 0])
    except ValueError:
        print('Por favor, entre com um número inteiro!')
        continue


    # CONVERSÃO DA LISTA CRIADA EM UM DATAFRAME DO PANDAS PARA REGISTRO ESTATÍSTICO DAS JOGADAS
    df = pd.DataFrame(players, columns=['PLAYER', 'CEREBRO', 'TIRO', 'PASSO', 'PLAYS'])

    # DEFININDO RANDOMICAMENTE O JOGADOR INICIAL
    iplayer = df.sample(replace=False)  # seleciona randomicamente o primeiro jogador
    p = iplayer.iloc[0]['PLAYER']  # armazena o nome do jogador
    index = iplayer.index[0]  # armazena o indice do jogador atual, no início do jogo será o jogador sorteado

    # ROLANDO OS DADOS - AQUI ACONTECE UMA JOGADA COMPLETA
    while winner == None:
        play_again = 's'
        p = df.iloc[index]['PLAYER']  # armazena o nome do jogador atual
        print('-'.ljust(109, '-'))
        print(f'Jogador {Fore.BLACK}{Back.WHITE}{p}{Style.RESET_ALL}, Role os dados pressionando <ENTER>')
        input(f'DADOS DISPONIVEIS NO TUBO: {available_dices}')
        
        # REGISTROS DA JOGADA
        dice = set_dice(available_dices)  # armazena o dado atual 
        play(dice, df, green, yellow, red, index)  # registra os pontos
        record_the_move(index, df)  # registra a quantidade de jogadas
        remove_dice(available_dices, dice)  # remove o dado sorteado dos dados disponíveis
        print(f'{Fore.WHITE}{Back.GREEN}PLACAR GERAL{Style.RESET_ALL}'.ljust(70, '-'))
        print(f'{df.to_string(index=False)}\n')
        print('-'.ljust(56, '-'))
        print()

        ################################# VERIFICAR OS PASSO

        # VERIFICACOES:
        # 1. se alguem atingiu 13 pontos, assim vencendo o jogo
        winner = check_win(df)
        if winner != None:
            game_on = False

        # 2. se o jogador atual levou 3 TIRO, perdendo assim sua vez
        if df.loc[index]['TIRO'] == 3:
            print(f'JOGADOR {Fore.WHITE}{Back.GREEN}{p}{Style.RESET_ALL} LEVOU 3 TIRO, SEUS CEREBRO SERÃO ZERADOS E VOCÊ DEVE PASSAR A VEZ')
            df.loc[index, ['TIRO']] = 0
            df.loc[index, ['CEREBRO']] = 0
            df.loc[index, ['PASSO']] = 0
            play_again = 'n' 

        
        # 3. se tem dados disponíveis no tubos, se não ele tem ele tem que passar a vez
        if len(available_dices) <= 0:
            print(f'Jogador {Fore.WHITE}{Back.GREEN}{p}{Style.RESET_ALL}, acabaram seus dados, você deve passar a vez')
            play_again = 'n'


        # 4. se o jogador atual quer passar a vez
        if play_again == 's':
            ask = input(f'Jogador {Fore.BLACK}{Back.WHITE}{p}{Style.RESET_ALL},VOCÊ QUER JOGAR NOVAMENTE (S/N)? ').lower()
            if ask == 'n':
                play_again = 'n'


        # 5. verifica se o jogador atual PODE continuar jogando
        if play_again == 'n':
            index = next_player(index, df)
            available_dices = ['d1', 'd2', 'd3', 'd4', 'd5','d6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13']  # retorna todos os dados para o tubo
        
        clear()

if game_on == True:
    print(f'O JOGADOR VENCEDOR É {winner}')
print('FIM DO JOGO')
print('OBRIGADO')
deinit()




