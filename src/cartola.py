import requests
import json
from random import randint

def getTimeJogador(clubes, jogador):
    for clube in clubes:
        if(jogador['clube_id']== clube):
            return clube['nome']

def getNomePosicao(id):
    if(id == 1):
        return "goleiro"
    elif(id==2):
        return "latera"
    elif(id==3):
        return "zagueiro"
    elif(id==4):
        return "meiuca"
    else:
        return "atacante"
    

def buscaListaJogadoresEClubes():
    request = requests.get(f"https://api.cartola.globo.com/atletas/mercado")
    tudo = json.loads(request.content)
    jogadores_e_tecnicos = tudo['atletas']
    clubes = tudo['clubes']
    jogadores = []
    jogadores_provaveis = []

    #retira tecnicos da lista
    for jogador in jogadores_e_tecnicos:
        if(jogador['posicao_id'] != 6):
            jogadores.append(jogador)

    #deixa so os provaveis e com minimo pra valorizar igual ou menor q media de pontos
    for jogador in jogadores:
        if(jogador['status_id'] == 7) and (jogador['minimo_para_valorizar'] <= jogador['media_num']) and jogador['media_num']>5:
            jogadores_provaveis.append(jogador)

    return jogadores_provaveis,clubes

#seleciona pitaco da rodada
def getPitacoDaRodada():
    jogadores = buscaListaJogadoresEClubes()[0]
    escolha = randint(0,len(jogadores)-1)
    escolhido = jogadores[escolha]
    clubes = buscaListaJogadoresEClubes()[1]
    #mapea informacoes do jogador escolhido

    pitaco = {}
    pitaco["nome"] = escolhido['apelido']
    pitaco['clube'] = getTimeJogador(clubes,escolhido)
    pitaco['minimo_para_valorizar'] = escolhido['minimo_para_valorizar']
    pitaco["posicao"] = getNomePosicao(escolhido['posicao_id'])

    return pitaco