# -*- coding:utf-8 -*
''' Importação de bibliotecas utilizadas '''
import leituraArq_CEPEL
import AjusteLinear
import filtroAR
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np
import statsmodels.api as sm

# Função de faz a autocorrelação parcial
def autoCorrecParcial(listaVazao):
    sm.graphics.tsa.plot_pacf(listaVazao, lags = 10, use_vlines = False, linestyle = '-')
    pautoCoef = sm.tsa.stattools.pacf(listaVazao, nlags = 10)
    print(pautoCoef)

''' Autocorrelação '''
sm.graphics.tsa.plot_acf(filtroAR.yn1AR1, lags = 50, use_vlines = False, linestyle = '-')
sm.graphics.tsa.plot_acf(filtroAR.yn2AR1, lags = 50, use_vlines = False, linestyle = '-')
autoCoef = sm.tsa.stattools.acf(filtroAR.yn1AR1, nlags = 5)

''' Autocorrelação Parcial '''
# Faz a Autocorrelação Parcial para encontrar o lag do modelo
autoCorrecParcial(filtroAR.yn1AR1)
autoCorrecParcial(filtroAR.yn2AR1)

''' Equação do modelo Autoregressivo AR(1) '''





plt.show()