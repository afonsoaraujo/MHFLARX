# -*- coding:utf-8 -*

''' Importação e alocação de diretorio de bibliotecas '''
import sys
diretorioLib1 = "C:/Users/Lucas/OneDrive/MHFLARX/lib"
sys.path.append(diretorioLib1)

''' Importação de bibliotecas utilizadas '''
from lib import*

nomeArq         = "vazoes_SC_65370000.csv"
ArqParametros   = "Postos e parametros.csv"
diretorioDados  = "C:/Users/lucas/OneDrive/MHFLARX/dados/"

# Definições de variáveis de armazenamento de dados globais
lista_posto     = []    # Lista com o numero dos postos
nomes_posto     = []    # Lista com o nome dos postos


''' Leitura do arquivo '''
    # Quando trocar de CEPEL e ANA lembrar de mudar o skipheader do database --> CEPEL - 0, ANA - 1 

try:
    # Leitura dos arquivos e disposição correta em forma matricial para análise
    with open(diretorioDados + nomeArq, "r") as csvfile:
        database = np.genfromtxt(csvfile, dtype = str, delimiter = ';', skip_header = 1)

    with open(diretorioDados + ArqParametros, "r") as csvfile:
        parametros = np.genfromtxt(csvfile, dtype = str, delimiter = ',', skip_header = 0)

    for p in range(len(database[0])-1):
        lista_posto.append(str(database[0][p+1]))

except FileNotFoundError:
    print("Arquivo não encontrado! Diretorio incorreto!")


# MAIN PRINCIPAL
ana = analiseRec_ANA(1946, 1, database)
ana.analise()

plt.figure(1)
ana.plotRecTotal(0)
plt.plot(ana.dados.listaVazao)

plt.figure(2)
filtro = filtroAR_ANA(1956, 1, database)
filtro.filtroAR1()

plt.show()