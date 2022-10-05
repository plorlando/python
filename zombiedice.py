import random


# DEFINIÇÃO DE VARIÁVEIS E FUNCOES
# 2 a 99 jogadores
data = {}


jogadores = []

j = 'jogadores'
dado_verde = ("c", "e", "c"," p", "c", "p")
dado_amarelo = ("c", "e", "p", "c", "e", "p")
dado_vermelho = ("e", "p", "e", "c", "e", "p")
d1 = dado_verde
d2 = dado_verde
d3 = dado_verde
d4 = dado_verde
d5 = dado_verde
d6 = dado_verde
d7 = dado_amarelo
d8 = dado_amarelo
d9 = dado_amarelo
d10 = dado_amarelo
d11 = dado_vermelho
d12 = dado_vermelho
d13 = dado_vermelho

count_players = 1

def add_player(p, c):
    # jogadores.append(p)
    data.update({c: {'name': p,
        "c": 0,
        "e": 0,
        "p": 0
        }
    })


def play():
    # deve ser sorteados 3 dados por jogada, cada um deles representa uma vitima atacada
    # fazer um random para determinar qual dado foi sorteado
    # fazer um segundo random dentro do dado sorteado para sortear a face do dado
    # somar o ponto sorteado nos pontos do jogador
    pass

def score():
    # deve ser registrado o ponto no dict, com o nome da pessoa e qual faze saiu
    # a cada ponto deve verificar condição de: 1-vitória, 2-derrota, e se nenhuma acontecer se ele quer jogar novamente
    pass

def check_win():
    pass

def check_lose():
    pass

def check_play_again():
    pass

def check_tie():
    pass

# CONFIGURACOES INICIAIS DO JOGO
print('*********************************')
print('ZOMBIE DICE')
print('São necessários pelo menos 2 jogadores para pode jogar Zombie Dice.')
print('*********************************\n')

while j != '' and count_players <= 99:
    j = input(f'Digite o nome do jogador numero {count_players} (deixe em branco para começar a jogar): ')

    if j != '':
        add_player(j, count_players)

    count_players += 1
    print('\n')

total_players = count_players

if total_players >= 2:


    # initial_player = random.choice(data['player'])
    print(data[2]['name'])
    # pos = data[initial_player]['pos']

    # print(f'O jogador que vai iniciar o jogo é {initial_player}')
    # print(f'A posição do jogador inicial é {pos}')
    # print(f'Total de jogadores: {total_players}')
    # print(data)
else:
    print('O jogo precisa ter no mínimo 2 jogares. Reinicie o jogo.')