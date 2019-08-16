# -*- coding:utf-8 -*
'''     analiseRec - Análise de Recessão - escrito por Lucas Ribeiro Magalhães - UFRJ

Esté código tem função de analisar as recessões de no posto escolhido pelo usuario durante o tempo escolhido e retornar
esses dados numa matriz de n recessões em n anos.

Para que o código funcione é preciso 2 arquivos:
VazoesDiarias.csv
    Arquivo do Cepel contendo as vazões, em escala diária, das bacias hidrográficas desde 1932.
    
Postos e parametros.csv
    Arquivo contendo o nome dos postos e parametros que auxiliam a filtragem (tiRec, varVazao).

Para usar em diferentes PCs fazer adicionar o diretório de suas bibliotecas e alterar a variável "diretorioDados" [linha 53].

Na ordem de execução esse é o primeiro arquivo de código!
'''

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
from getData import*
from leituraArq_CEPEL import*
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np
import csv
import statsmodels.api as sm


''' Definição de variáveis que serão utilizadas para instanciar objeto leituraArq '''
ano_usuario     = 1931  # Definição do ano que o usuário quer plotar
posto_usuario   = 173   # Definição do posto o qual o usuário que ver os dados
qtd_graph       = 1     # Define a quantidade de graficos que o usuário quer comparar

matrizRecessao  = []    # Matriz com os vetores de recessão do ano escolhido
lista_posto     = []    # Lista com o numero dos postos
nomes_posto     = []    # Lista com o nome dos postos
vetorRecDias    = []    # Lista com o vetor de dias para recessão, para todos os n anos agrupados
vetorRecVazao   = []    # Lista com o vetor de vazão para recessão, para todos os n anos agrupados
recVazao        = []    # lista com todas as recessões para o calculo de autocorrelação

nomeArq         = "VazoesDiarias.csv"
ArqParametros   = "Postos e parametros.csv"
diretorioDados  = "C:/Users/lucas/OneDrive/MHFLARX/dados/"
diretorioDados3  = "C:/Users/Afonso/OneDrive/work/modelos/MHFLARX/dados/"


''' Leitura do arquivo '''
try:
    # Leitura dos arquivos e disposição correta em forma matricial para análise
    with open(diretorioDados + nomeArq, "r") as csvfile:
        database = np.genfromtxt(csvfile, dtype = str, delimiter = ',', skip_header = 0)

    with open(diretorioDados + ArqParametros, "r") as csvfile:
        parametros = np.genfromtxt(csvfile, dtype = str, delimiter = ',', skip_header = 0)

    for p in range(len(database[0])-1):
        lista_posto.append(str(database[0][p+1]))

except FileNotFoundError:
    print("Arquivo não encontrado! Diretorio incorreto!")


''' Funções '''
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
    for d in range(int(dados.listaData[-1])):
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
                    if (len(recVazao) <= 5): 
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

# Plot o vetor recessão
def plotRec(listaData, listaVazao, ind):
    plt.figure(ind + 1)
    plt.plot(listaData, listaVazao,  linewidth = dados.line_plot)
    plt.title("Recessão com fim no dia " + str(ind))
    plt.xlabel("Dias")
    plt.ylabel("Vazão")
    #plt.show()

# Plot de toda recessão anual
def plotRecTotal(indGraph):
    plt.plot(matrizRecessao[indGraph], matrizRecessao[indGraph + 1], 'o', ms = 2)
    plt.title("Recessao")
    plt.xlabel("Dias")
    plt.ylabel("Vazão")
    #plt.show()


''' Loop principal, repete as funções para qtd_graph anos. '''
for q in range(qtd_graph):

    ''' Instanciação de objetos '''
    dados = dadosArq(ano_usuario + q, posto_usuario, qtd_graph, database, lista_posto)
    dados.vazoesDia()

    ''' Parametros do filtro '''
    for i in range(len(parametros)):
        if (str(posto_usuario) == parametros[i][0]):
            tiRec     = parametros[i][3] # tempo mínimo para inicio de uma recessão (DEPENDE DE UMA DETERMINADA BACIA)
            tfRec     = 2     # tempo minimo anterior do fim de uma recessão (DEPENDE DE UMA DETERMINADA BACIA) [VALOR MÍNIMO: 2]
            try:
                varVazao  = float(parametros[i][4])     # Variação minima de vazao entre recessão
            except ValueError:
                varVazao  = 15    # Variação alterável
                print("A variavel varVazao não foi encontrada e está no valor default de: " + str(varVazao) + ".")
            nomePosto = parametros[i][2]     # Nome do Posto
            ''' Definição de variaveis e listas de rotinas '''
            derivada        = []    # Lista da derivada da vazao do ano q
            
            ''' Funções principais '''
            derivada = np.gradient(dados.listaVazao)    # Calcula a derivada da vazão
            filtroRec(tiRec, varVazao)    # Chama a função que filtra os dados da vazao anual
            matrizRecessao.append(vetorRecDias)   # Adiciona os dias de recessão ao vetor geral de recessão
            matrizRecessao.append(vetorRecVazao)    # Adiciona a vazão da recessão ao vetor geral de recessão

            ''' Plot dos dados obtidos '''
            #plt.figure(q)
            #plotRecTotal(q*2)
            #dados.graphPlot(nomePosto)
plt.show()