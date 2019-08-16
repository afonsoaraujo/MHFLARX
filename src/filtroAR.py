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
from getData import*
from leituraArq_CEPEL import*
import AjusteLinear
#import autocorrelacao
from matplotlib import pyplot as plt
import numpy as np

''' Definição de listas e variáveis utilizadas '''
yn1AR1 = [] #Componente lenta
yn2AR1 = [] #Comoponente componente intermediaria./rapida


Vazao = dadosArq(1980, analiseRec.posto_usuario, 1, analiseRec.database, analiseRec.lista_posto)
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
    alpha1 = 0.98 #Constante para Yn1
    alpha2 = 0.97 #Constante para Yn2
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
    alpha = 0.9
    deltaT = 1
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
        if (sinalYn2 <= 0):
            print("Diminua o Alpha1!")
            break

plt.figure(0)
plt.title("Componente Lenta para o Posto: " + str(analiseRec.nomePosto) + " no ano de " + str(analiseRec.ano_usuario))
plt.plot(Vazao.listaData, yn, linewidth = 0.5)
plt.plot(Vazao.listaData, yn1AR1, 'r--', linewidth = 0.5)

plt.figure(0)
plt.title("Componente Intermediaria para o Posto: " + str(analiseRec.nomePosto) + " no ano de " + str(analiseRec.ano_usuario))
#plt.plot(Vazao.listaData, yn)
plt.plot(Vazao.listaData, yn2AR1, 'g-.', linewidth = 0.5)

plt.show()