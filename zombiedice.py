import random



# DEFINIÇÃO DE VARIÁVEIS
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


while j != '':
    j = input('Digite o nome do jogador (deixe em branco para começar a jogar): ')
    if j != '':
        add_player(j)

print(random.choice(jogadores))
print(data)