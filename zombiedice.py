



# DEFINIÇÃO DE VARIÁVEIS
jogadores = []
data = {}
data['pedro'] = {
        "c": 0,
        "p": 0,
        "e": 0
    }
data['luciane'] = {
        "c": 0,
        "p": 0,
        "e": 0
    }
data['luciane']['p'] = 8
print(data)

while not '':
    j = input('Digite o nome do jogador (deixe em branco para começar a jogar): ')
    print(j)
    jogadores = jogadores.append(j)
    print(jogadores)

print(jogadores)