# -*- coding:utf-8 -*
'''     filtroAr - Filtro Auto Regressivo de ordem 1 - escrito por Lucas Ribeiro Magalhães - UFRJ


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
from getData_ANA import*
from leituraArq_ANA import*
import analiseRec_ANA
import AjusteLinear
#import autocorrelacao
from matplotlib import pyplot as plt
import numpy as np

''' Definição de listas e variáveis utilizadas para o filtro'''
yn1AR1 = [] #Componente lenta
yn2AR1 = [] #Comoponente componente intermediaria./rapida


''' ------------------- Rotina para analiseRec_ANA ------------------- '''

for q in range(analiseRec_ANA.qtd_graph):
    dados = dadosArq(analiseRec_ANA.ano_usuario + q, analiseRec_ANA.qtd_graph, analiseRec_ANA.database)
    dados.vazoesDia()

    ''' Parametros do filtro '''
    tiRec     = 2     # tempo mínimo para inicio de uma recessão (DEPENDE DE UMA DETERMINADA BACIA)
    tfRec     = 2     # tempo minimo anterior do fim de uma recessão (DEPENDE DE UMA DETERMINADA BACIA) [VALOR MÍNIMO: 2]
    varVazao  = 2    # Variação minima de vazao entre recessão

    ''' Definição de variaveis e listas de rotinas '''
    derivada        = []    # Lista da derivada da vazao do ano q
    
    ''' Funções principais '''
    derivada = np.gradient(dados.listaVazao)    # Calcula a derivada da vazão
    analiseRec_ANA.filtroRec(tiRec, varVazao)    # Chama a função que filtra os dados da vazao anual
    analiseRec_ANA.matrizRecessao.append(analiseRec_ANA.vetorRecDias)   # Adiciona os dias de recessão ao vetor geral de recessão
    analiseRec_ANA.matrizRecessao.append(analiseRec_ANA.vetorRecVazao)    # Adiciona a vazão da recessão ao vetor geral de recessão
    #plotRecTotal(q*2)
    #plt.plot(dados.listaVazao)

'''---------------------------------------------------------------------------- '''

''' ------------------- Rotina Regressão linear -------------------  '''

K = AjusteLinear.regreLinear(analiseRec_ANA.recVazao)       # Faz o ajuste linear

''' Faz a separação das constantes de tempo da bacia
    Para selecionar escolher onde separar, clique no grafico plotado '''
if (AjusteLinear.constante == 1):
    x = plt.ginput(1, show_clicks = True)       
    lista1 = []
    lista2 = []
    for i in range(len(analiseRec_ANA.recVazao)):
        if (analiseRec_ANA.recVazao[i] > int(x[0][0])):
            lista1.append(analiseRec_ANA.recVazao[i])
        else:
            lista2.append(analiseRec_ANA.recVazao[i])

    plt.figure(3)
    K1 = AjusteLinear.regreLinear(lista1)
    plt.figure(2)
    K2 = AjusteLinear.regreLinear(lista2)

    AjusteLinear.Ks.append(K1)
    AjusteLinear.Ks.append(K2)
else:
    AjusteLinear.Ks.append(K)
print(AjusteLinear.Ks)
plt.show()

'''---------------------------------------------------------------------------- '''

''' ------------------- Rotina Filtro AR -------------------  '''

Vazao = dadosArq(1983, 1, analiseRec_ANA.database)
Vazao.vazoesDia()
yn  = Vazao.listaVazao # Vazão total
yn2 = []
xn  = [] #Preciptação

''' Filtro AR1 '''
if (len(AjusteLinear.Ks) > 1):
    # Primeiro filtra o sinal yn com K1
    T1 = float(abs(1/(np.log(AjusteLinear.Ks[0])))) #Constante para Yn1
    T2 = float(abs(1/(np.log(AjusteLinear.Ks[1])))) #Constante para Yn2
    print(T1)
    print(T2)
    alpha2 = 0.65 #Constante para Yn1
    alpha1 = 0.83 #Constante para Yn2
    deltaT = 1 #Intervalo de discretização
    for i in range(len(yn)):
        try:
            if i == 0:
                sinalFiltradoK1 = (deltaT/T1)*yn[i]
                yn1AR1.insert(i, sinalFiltradoK1)
            else:
                sinalFiltradoK1 = (deltaT/T1)*yn[i] + alpha1*((1 - (deltaT/T1))*yn1AR1[i-1])
                yn1AR1.insert(i, sinalFiltradoK1)
        except IndexError:
            sinalFiltradoK1 = (deltaT/T1)*yn[i] + alpha1*((1 - (deltaT/T1))*yn1AR1[i-1])
            yn1AR1.insert(i, sinalFiltradoK1)
        sinalYn2 = yn[i] - yn1AR1[i]
        yn2.insert(i, sinalYn2)
        if (sinalYn2 <= 0):
            print("Diminua o Alpha1!")
            break
    for i in range(len(yn2)):
        try:
            if i == 0:
                sinalFiltradoK2 = (deltaT/T2)*yn2[i]
                yn2AR1.insert(i, sinalFiltradoK2)
            else:
                sinalFiltradoK2 = (deltaT/T2)*yn2[i] + alpha2*((1 - (deltaT/T2))*yn2AR1[i-1])
                yn2AR1.insert(i, sinalFiltradoK2)
        except IndexError:
            sinalFiltradoK2 = (deltaT/T2)*yn2[i] + alpha2*((1 - (deltaT/T2))*yn2AR1[i-1])
            yn2AR1.insert(i, sinalFiltradoK2)
        sinalYn3 = yn2[i] - yn2AR1[i]
        if (sinalYn3 <= 0):
            print("Diminua o Alpha2!")
            break
else:
    T = float(abs(1/(np.log(AjusteLinear.Ks[0]))))
    alpha  = 0.83
    deltaT = 1
    for i in range(len(yn)):
        try:
            if i == 0:
                sinalFiltradoK1 = (deltaT/T)*yn[i]
                yn1AR1.insert(i, sinalFiltradoK1)
            else:
                sinalFiltradoK1 = (deltaT/T)*yn[i] + alpha*((1 - (deltaT/T))*yn1AR1[i-1])
                yn1AR1.insert(i, sinalFiltradoK1)
        except IndexError:
            sinalFiltradoK1 = (deltaT/T)*yn[i] + alpha*((1 - (deltaT/T))*yn1AR1[i-1])
            yn1AR1.insert(i, sinalFiltradoK1)
        sinalYn2 = yn[i] - yn1AR1[i]
        yn2.insert(i, sinalYn2)
        if (sinalYn2 <= 0):
            print("Diminua o Alpha!")
            break

plt.figure(0)
plt.title("Componente Lenta para o Posto: " + str("Rio Jangada") + " no ano de " + str(1983))
plt.plot(Vazao.listaData, yn, linewidth = 0.5)
plt.plot(Vazao.listaData, yn1AR1, 'r--', linewidth = 0.5)

plt.figure(0)
plt.title("Componente Intermediaria para o Posto: " + str("Rio Jangada") + " no ano de " + str(1983))
#plt.plot(Vazao.listaData, yn)
plt.plot(Vazao.listaData, yn2AR1, 'g-.', linewidth = 0.5)

'''---------------------------------------------------------------------------- '''

plt.show()