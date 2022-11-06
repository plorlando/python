from random import randint, shuffle

class Dado:
    def __init__(self, cor, lados, ladoSorteado):
        self.cor = cor
        self.lados = lados
        self.ladoSorteado = ladoSorteado


class Jogador:
    def __init__(self, nome, cerebros, tiros):
        self.nome = nome
        self.cerebros = cerebros
        self.tiros = tiros


def SiglaParaAcao(argument):
    switcher = {
        "C": "Cerebro",
        "P": "Passo",
        "T": "Tiro",
    }
    return switcher.get(argument, "Ñ Implementada")


def JogaDado(listaDados):
    dado = listaDados.pop()
    numSorteado = randint(0, 5)
    dado.ladoSorteado = dado.lados[numSorteado]
    print("    ", dado.cor, ' ', SiglaParaAcao(dado.ladoSorteado))

    return dado


def VerificaTipoLado(listaDadosJogados, jogadorAtual):
    for dado in listaDadosJogados:
        if (dado.ladoSorteado == "C"):
            jogadorAtual.cerebros = jogadorAtual.cerebros + 1
        elif (dado.ladoSorteado == "T"):
            jogadorAtual.tiros = jogadorAtual.tiros + 1


ALUNA = "GABRIELLY CAROLINE DA ROSA"
GTI = "GESTÃO DA TECNOLOGIA DA INFORMAÇÃO"

print(ALUNA)
print(GTI)
print("SEJAM BEM VINDOS AO JOGO ZOMBIE DICE! VAMOS COMEÇAR?\n")
numJogadores = 0
while (numJogadores < 2):
    numJogadores = int(input("INFORME O NUMERO DE JOGADORES: "))

    if (numJogadores < 2):
        print(">>ATENÇÃO<< O JOGO PRECISA NO MÍNIMO DE 2 JOGADORES PARA INICIAR A PARTIDA !n")

listaJogadores = []

for i in range(numJogadores):
    nome = input('Informe o nome do jogador ' + str(i + 1) + ': ')
    listaJogadores.append(Jogador(nome, 0, 0))

ladosDadoVerde = ["C", "P", "C", "T", "P", "C"]
ladosDadoAmarelo = ["T", "P", "C", "T", "P", "C"]
ladosDadoVermelho = ["T", "P", "T", "C", "P", "T"]
alguemGanhou = False

dadoVerde = Dado("Verde ", ladosDadoVerde, "")
dadoAmarelo = Dado("Amarelo", ladosDadoAmarelo, "")
dadoVermelho = Dado("Vermelho", ladosDadoVermelho, "")

listaDados = [
    dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde,
    dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
    dadoVermelho, dadoVermelho, dadoVermelho
]

listaDadosJogados = []

print('INICIANDO O JOGO...')
while (not alguemGanhou):
    for jogadorAtual in listaJogadores:
        print('É a vez de', jogadorAtual.nome + '...')

        shuffle(listaDados)
        numSorteado = randint(0, 5)

        d1 = JogaDado(listaDados)
        d2 = JogaDado(listaDados)
        d3 = JogaDado(listaDados)

        shuffle(listaDados)

        listaDadosJogados.clear()
        listaDadosJogados.append(d1)
        listaDadosJogados.append(d2)
        listaDadosJogados.append(d3)

        VerificaTipoLado(listaDadosJogados, jogadorAtual)

        listaDados.append(d1)
        listaDados.append(d2)
        listaDados.append(d3)

        shuffle(listaDados)

        print("    " + jogadorAtual.nome)
        print("        " + "Cerebros ", jogadorAtual.cerebros)
        print("        " + "Tiros ", jogadorAtual.tiros)

        for jogador in listaJogadores:
            if (jogador.cerebros >= 13):
                print('O jogador ', jogador.nome, ' Ganhou\n')
                alguemGanhou = True

        for jogador in listaJogadores:
            if (jogador.tiros >= 3):
                print('O jogador ', jogador.nome, ' Perdeu\n')
                listaJogadores.remove(jogador)

        if (len(listaJogadores) == 1):
            print('O jogador ', listaJogadores[0].nome, ' Ganhou\n')
            alguemGanhou = True
            break

print('FIM DO JOGO')