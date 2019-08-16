# -*- coding:utf-8 -*
'''     AjusteLinear - Realiza o Ajuste Linear - escrito por Lucas Ribeiro Magalhães - UFRJ

Esse código tem como saida o ajuste linear das recessões previamente analisadas no arquivo analiseRec.py
O ajuste é nas vazões q(t) x q(t+1)

O ajuste é feito e em seguida é retornado as constantes K do filtro auto regressivo

O código também faz a separação de constantes por meio da função ginput() e refaz o ajuste linear
'''

''' Importação de bibliotecas utilizadas '''
#import analiseRec_ANA
from matplotlib import pyplot as plt
import numpy as np

constante = 1 # Essa varrável indica a necessidade de separar em mais constantes de tempo, caso 0 sim, caso 1 não
Ks = [] # lista com as constantes de cada regressão linear


# Plot Qt x Qt+1 e regressao linear
def regreLinear(listaVazao):
    listaVazao = np.asarray(listaVazao)
    x = listaVazao[:, np.newaxis]
    coefAngular, _, _, _ = np.linalg.lstsq(x[:len(x) - 1], listaVazao[1:len(listaVazao)], rcond=None)
    
    #Plot dos dados
    plt.plot(listaVazao[:len(listaVazao) - 1], listaVazao[1:len(listaVazao)], 'o', label = "Qt x Qt+1")
    plt.legend()
    plt.plot(listaVazao[:len(listaVazao) - 1], coefAngular*np.array(listaVazao[:len(listaVazao) - 1 ]), 'r', label = 'Ajuste Linear', linewidth = 0.5)
    plt.legend()
    plt.title("Ajuste Linear")
    plt.xlabel("Vazão")
    plt.ylabel("Vazao + 1")
    return coefAngular