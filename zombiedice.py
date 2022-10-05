import random



# DEFINIÇÃO DE VARIÁVEIS E FUNCOES
jogadores = []
data = {}
j = 'jogadores'

def add_player(p):
    jogadores.append(p)
    data.update({ p: {
        "c": 0,
        "e": 0,
        "p": 0
        }
    })


# CONFIGURACOES INICIAIS DO JOGO
print('*********************************')
print('ZOMBIE DICE')
print('*********************************\n')
while j != '':
    j = input('Digite o nome do jogador (deixe em branco para começar a jogar): ')
    if j != '':
        add_player(j)

jogador_inicial = random.choice(jogadores)
pos = jogadores.index(jogador_inicial)
total_jog = len(jogadores)

print(f'O jogador que vai iniciar o jogo é {jogador_inicial}')
print(f'A posição do jogador inicial é {pos}')
print(f'Total de jogadores: {total_jog}')
print(data)