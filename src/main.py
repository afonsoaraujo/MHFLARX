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

#Abertura do arquivo
arqAna = loadData(nomeArq, ArqParametros, diretorioDados)
arqAna.openAna()

# MAIN PRINCIPAL
ana = analiseRec_ANA(1946, 1, arqAna.database)
ana.analise()

plt.figure(1)
ana.plotRecTotal(0)
plt.plot(ana.dados.listaVazao)

plt.figure(2)
filtro = filtroAR_ANA(1956, 1, arqAna.database)
filtro.filtroAR1()

autocorrelacao = autoCorrelacao(filtro.yn1AR1)
autoCorrelacao2 = autoCorrelacao(filtro.yn2AR1)
autocorrelacao.autoCor()
autoCorrelacao2.autoCor()
autocorrelacao.autoCorParcial()
autoCorrelacao2.autoCorParcial()

precipitacao1 = precipitacao(ana.dados.listaVazao, ana.dados.listaData, autocorrelacao.pautoCoef)
precipitacao2 = precipitacao(ana.dados.listaVazao, ana.dados.listaData, autoCorrelacao2.pautoCoef)

precipitacao1.precipitacaoEfetiva()
precipitacao2.precipitacaoEfetiva()

plt.figure(20)
precipitacao1.plotPrecipitacao()
plt.figure(30)
precipitacao2.plotPrecipitacao()

plt.show()