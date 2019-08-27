# -*- coding:utf-8 -*

''' Importação e alocação de diretorio de bibliotecas '''
import sys
diretorioLib1 = "C:/Users/Lucas/OneDrive/MHFLARX/lib"
diretorioLib2 = "D:/OneDrive/MHFLARX/lib"
diretorioLib3 = "C:/Users/Afonso/OneDrive/work/modelos/MHFLARX/lib"
diretorioLib4 = "C:/Users/afons/OneDrive/work/modelos/MHFLARX/lib"
diretorioLib5 = "D:/work/modelos/MHFLARX/lib"
sys.path.append(diretorioLib1)
sys.path.append(diretorioLib2)
sys.path.append(diretorioLib3)
sys.path.append(diretorioLib4)
sys.path.append(diretorioLib5)

''' Importação de bibliotecas utilizadas '''

import csv
import numpy as np
from getData import*
from leituraArq import*
from matplotlib import pyplot as plt


''' Definição de variáveis que serão utilizadas para instanciar objeto leituraArq '''
ano_usuario     = 1946  # Definição do ano que o usuário quer plotar
qtd_graph       = 1     # Define a quantidade de graficos que o usuário quer comparar

matrizRecessao  = []    # Matriz com os vetores de recessão do ano escolhido
vetorRecDias    = []    # Lista com o vetor de dias para recessão, para todos os n anos agrupados
vetorRecVazao   = []    # Lista com o vetor de vazão para recessão, para todos os n anos agrupados
recVazao        = []    # lista com todas as recessões para o calculo de autocorrelação

nomeArq          = "vazoes_SC_65370000.csv"
diretorioDados1  = "C:/Users/afons/OneDrive/work/modelos/MHFLARX/dados"
diretorioDados2  = "C:/Users/lucas/OneDrive/MHFLARX/dados/"
diretorioDados3  = "C:/Users/Afonso/OneDrive/work/modelos/MHFLARX/dados/"
diretorioDados4  = "D:/work/modelos/MHFLARX/dados/"


try:
    # Leitura dos arquivos e disposição correta em forma matricial para análise
    with open(diretorioDados2 + nomeArq, "r") as csvfile:
        database = np.genfromtxt(csvfile, dtype = str, delimiter = ';', skip_header = 1)

except FileNotFoundError:
    print("Arquivo não encontrado! Diretorio incorreto!")

# Função que filtra os valores brutos de vazões somente nas recessões
def filtroRec(tiRec, varVazao):
    d = 0
    i = 0
    j = 0
    jmax = 5
    if(tiRec == 'N/A'):
        tiRec = 5
    else:
        tiRec = int(tiRec)
    for d in range(len(dados.listaData)):
        if (derivada[d] < 0 ):
            if (i >= tiRec):
                try:
                    if ( abs(dados.listaVazao[d + 1] - dados.listaVazao[d]) <= varVazao):
                        if (j > jmax):
                            vetorRecDias.insert(d, 0)
                            vetorRecVazao.insert(d, 0)
                            if (d == int(dados.listaData[-1])):
                                break
                        else:
                            if (derivada[d + tfRec - 2] < 0):
                                if (derivada[d + tfRec - 1] < 0):
                                    if (derivada[d + tfRec] < 0):
                                        vetorRecDias.insert(d, dados.listaData[d])
                                        vetorRecVazao.insert(d, dados.listaVazao[d])
                                        recVazao.insert(d, dados.listaVazao[d])
                                        i = i + 1
                            else:
                                vetorRecDias.insert(d, 0)
                                vetorRecVazao.insert(d, 0)
                                i = 0
                            if (d == int(dados.listaData[-1])):
                                break
                            j = j + 1
                    else:
                        j = 0
                        if (derivada[d + tfRec - 2] < 0):
                            if (derivada[d + tfRec - 1] < 0):
                                if (derivada[d + tfRec] < 0):
                                    vetorRecDias.insert(d, dados.listaData[d])
                                    vetorRecVazao.insert(d, dados.listaVazao[d])
                                    recVazao.insert(d, dados.listaVazao[d])
                                    i = i + 1
                        else:
                            vetorRecDias.insert(d, 0)
                            vetorRecVazao.insert(d, 0)
                            i = 0
                        if (d == int(dados.listaData[-1])):
                            break
                except IndexError:
                    if (abs(dados.listaVazao[-1] - dados.listaVazao[d]) <= varVazao):
                        if (j > jmax):
                            vetorRecDias.insert(d, 0)
                            vetorRecVazao.insert(d, 0)
                            if (d == int(dados.listaData[-1])):
                                break
                        else:
                            if (derivada[int(dados.listaData[-1]) - 3] < 0):
                                if (derivada[int(dados.listaData[-1]) - 2] < 0):
                                    if (derivada[int(dados.listaData[-1]) - 1] < 0):
                                        vetorRecDias.insert(d, dados.listaData[d])
                                        vetorRecVazao.insert(d, dados.listaVazao[d])
                                        recVazao.insert(d, dados.listaVazao[d])
                                        i = i + 1
                            else:
                                vetorRecDias.insert(d, 0)
                                vetorRecVazao.insert(d, 0)
                                i = 0
                            if (d == int(dados.listaData[-1])):
                                break
                            j = j + 1
                    else:
                        j = 0
                        if (derivada[int(dados.listaData[-1]) - 3] < 0):
                            if (derivada[int(dados.listaData[-1]) - 2] < 0):
                                if (derivada[int(dados.listaData[-1]) - 1] < 0):
                                    vetorRecDias.insert(d, dados.listaData[d])
                                    vetorRecVazao.insert(d, dados.listaVazao[d])
                                    recVazao.insert(d, dados.listaVazao[d])
                                    i = i + 1
                        else:
                            vetorRecDias.insert(d, 0)
                            vetorRecVazao.insert(d, 0)
                            i = 0
                        if (d == int(dados.listaData[-1])):
                            break
            else:
                i = i + 1
                vetorRecDias.insert(d,0)
                vetorRecVazao.insert(d,0)
        else:
            if (d == int(dados.listaData[-1])):
                break
            else:
                try:
                    if (len(recVazao) <= 4): 
                        vetorRecDias.insert(d,0)
                        vetorRecVazao.insert(d,0)
                        i = 0
                    else:
                        vetorRecDias.insert(d,0)
                        vetorRecVazao.insert(d,0)
                        i = 0
                except ValueError:
                    vetorRecDias.insert(d,0)
                    vetorRecVazao.insert(d,0)
                    i = 0

# Plot de toda recessão anual
def plotRecTotal(indGraph):
    plt.plot(matrizRecessao[indGraph], matrizRecessao[indGraph + 1], 'o', ms = 2)
    plt.title("Recessao")
    plt.xlabel("Dias")
    plt.ylabel("Vazão")
    #plt.show()

for q in range(qtd_graph):
    dados = dadosArq(ano_usuario + q, 0 , qtd_graph, database, [])
    dados.vazoesDia_ANA()

    ''' Parametros do filtro '''
    tiRec     = 2     # tempo mínimo para inicio de uma recessão (DEPENDE DE UMA DETERMINADA BACIA)
    tfRec     = 4     # tempo minimo anterior do fim de uma recessão (DEPENDE DE UMA DETERMINADA BACIA) [VALOR MÍNIMO: 2]
    varVazao  = 1    # Variação minima de vazao entre recessão

    ''' Definição de variaveis e listas de rotinas '''
    derivada        = []    # Lista da derivada da vazao do ano q
    


    ''' Funções principais '''
    derivada = np.gradient(dados.listaVazao)    # Calcula a derivada da vazão
    filtroRec(tiRec, varVazao)    # Chama a função que filtra os dados da vazao anual
    matrizRecessao.append(vetorRecDias)   # Adiciona os dias de recessão ao vetor geral de recessão
    matrizRecessao.append(vetorRecVazao)    # Adiciona a vazão da recessão ao vetor geral de recessão
    plotRecTotal(q*2)
    plt.plot(dados.listaVazao)
plt.show()