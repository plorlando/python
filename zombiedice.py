import random


# DEFINIÇÃO DE VARIÁVEIS E FUNCOES
jogadores = []
data = {}
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

def add_player(p):
    jogadores.append(p)
    data.update({ p: {
        "c": 0,
        "e": 0,
        "p": 0
        }
    })


def jogada():
    pass

def check_win():
    pass

def check_lose():
    pass

def check_play_again():
    pass

# CONFIGURACOES INICIAIS DO JOGO
print('*********************************')
print('ZOMBIE DICE')
print('São necessários pelo menos 2 jogadores para pode jogar Zombie Dice.')
print('*********************************\n')

while j != '':
    j = input('Digite o nome do jogador (deixe em branco para começar a jogar): ')
    if j != '':
        add_player(j)

total_jog = len(jogadores)

if total_jog >= 2:
    jogador_inicial = random.choice(jogadores)
    pos = jogadores.index(jogador_inicial)

    print(f'O jogador que vai iniciar o jogo é {jogador_inicial}')
    print(f'A posição do jogador inicial é {pos}')
    print(f'Total de jogadores: {total_jog}')
    print(data)
else:
    print('O jogo precisa ter no mínimo 2 jogares. Reinicie o jogo.')