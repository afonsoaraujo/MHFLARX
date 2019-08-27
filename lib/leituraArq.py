# -*- coding:utf-8 -*

import numpy as np                   # Biblioteca padrão (Python 3.X), baixada (Python 2.X)
from matplotlib import pyplot as plt # Biblioteca baixada (matplotlib)
from getData import*                 # Biblioteca própria (getData)

class dadosArq:
    '''
    A classe dadosArquivo tem função de instanciar objetos das entradas que o usuário escolher para realizar as devidas análises
    Entradas essas que são (respectivamente): ano (inteiro de 4 digitos), 
                                              posto (inteiro de 1, 2 ou 3 digitos), 
                                              quantidade (um número n inteiro) de gráficos para o plot dos dados.

    Atributos:
        ano_usuario     --> é a definição de um inteiro para o ano de análise escolhido
        posto_usuario   --> é a definição da uma string para o posto de análise escolhido
        qtd_graph       --> é a definição de um inteiro para a quantidade de gráficos(anos) subsequentes que serão plotados
        dados           --> é uma matriz contendo uma lista de vazão e datas do período escolhido para análise de recessões

    Métodos:
        __init__(self, ano, posto, qtd_graph) --> função de instanciação do objeto dadosArq, as informações tem que ser passadas na ordem correta
        lerArquivo(self) --> função que lê o arquivo
        graphPlotPlus(self) --> função que plota o(os) gráfico(os) de acordo com self.ano_usuario e self.qtd_graph
        graphPlot(self) --> função que plota somente o dado do ano escolhido
        vazoesDia(self) --> função que retorna uma lista de dias e vazões somente do ano escolhido para utilização em recessões ou outros afins
    '''
    
    def __init__(self, ano, posto, qtd_graph, dados, listaPosto):

        self.ano_usuario   = int(ano)
        self.posto_usuario = str(posto)
        self.qtd_graph     = int(qtd_graph)
        self.listaData     = []
        self.listaVazao    = []
        self.dados         = dados
        self.listaPosto    = listaPosto

    def findPosto(self): 
        self.indice_posto = self.listaPosto.index(self.posto_usuario) + 1   # indice_posto é a variável que indica qual o indice que se encontra o posto o qual o usuário está pesquisando

    def vazoesDia_CEPEL(self):
        # Chama a função self.findPosto()
        self.findPosto()      
        for i in range(self.dados.__len__()):                       
            data_arq  = self.dados[i][0]    # data_arq é a variável que armazena todas as datas existentes no arquivo no formato string              
            data      = Data(data_arq)  # Instanciação do objeto Data
            if (data.ano == int(self.ano_usuario)):
                vazao = self.dados[i][self.indice_posto]    # vazao é a variável que armazena todas as vazões no periodo escolhido
                self.listaData = data.diasAno()
                self.listaVazao.append(float(vazao))

    def vazoesDia_ANA(self): 
        for i in range(self.dados.__len__()):                       
            data_arq  = self.dados[i][2]    # data_arq é a variável que armazena todas as datas existentes no arquivo no formato string     
            data      = Data(data_arq)  # Instanciação do objeto Data
            bissexto = data.anoBissexto()
            if (self.ano_usuario == data.ano):
                for j in range(data.diasMes(data.mes)):
                    self.listaData = data.diasAno()
                    x = self.dados[i][16+j].replace(",", ".")
                    if (x == ""):
                        x = 0
                        self.listaVazao.append(x)
                    else:
                        self.listaVazao.append(float(x))
        for j in range(self.dados.__len__()): 
            data_arq2  = self.dados[j][2]
            data2      = Data(data_arq2)  # Instanciação do objeto Data
            if (self.ano_usuario == data2.ano):
                bissexto = data2.anoBissexto()
                if(bissexto == True):
                    if(len(self.listaVazao)<366):
                        a = 366 - len(self.listaVazao)
                        for k in range(a):
                            self.listaVazao.append(0)
                else:
                    if(len(self.listaVazao)<365):
                        a = 365 - len(self.listaVazao)
                        for k in range(a):
                            self.listaVazao.append(0)