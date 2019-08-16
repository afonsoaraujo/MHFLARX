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
        listaData       --> é uma lista vazia onde será colocado os dias do período escolhido para análise de recessões
        listaVazao      --> é uma lista vazia onde será colocado as vazões do período escolhido para análise de recessões
        line_plot       --> e a definição de um float para a espessura (ou raio) da linha (ou pontos) para plotagem dos dados

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
        self.line_plot     = float(0.5)
        self.dados         = dados
        self.listaPosto    = listaPosto
    
    def findPosto(self): 
        self.indice_posto = self.listaPosto.index(self.posto_usuario) + 1   # indice_posto é a variável que indica qual o indice que se encontra o posto o qual o usuário está pesquisando

    def graphPlotPlus(self):
        self.findPosto()   # Chama a função self.findPosto()
        for q in range(self.qtd_graph):
            globals()['datas%d' % int(self.ano_usuario + q)] = []   # Definição de listas dinâmicas para plot
            globals()['vazao%d' % int(self.ano_usuario + q)] = []                      
            for i in range(len(self.dados)):                       
                data_arq  = self.dados[i][0]    # data_arq é a variável que armazena todas as datas existentes no arquivo no formato string                    
                data      = Data(data_arq)  # Instanciação do objeto Data         
                if (data.ano == int(self.ano_usuario + q)):
                    vazao = self.dados[i][self.indice_posto]    # vazao é a variável que armazena todas as vazões no periodo escolhido
                    globals()['vazao%d' % int(self.ano_usuario + q)].append(int(vazao))
                    globals()['datas%d' % int(self.ano_usuario + q)].append(data.diasAno())

        # Plotagem dos dados no mesmo gráfico, caso queira em gráficos separados, descomentar a linha plt.figure(self.qtd_graph)
        for qs in range(self.qtd_graph):
            #plt.figure(self.qtd_graph) 
            plt.plot(globals()['datas%d' % int(self.ano_usuario + qs)], globals()['vazao%d' % int(self.ano_usuario + qs)], linewidth = self.line_plot)
            plt.title(str(self.ano_usuario) + ' para: ' + str(self.ano_usuario + qs)) # Título que indica o primeiro ano escolhido até  ultimo plotado
            plt.xlabel('Dias')
            plt.ylabel('Vazoes (m^3/s)')
            continue
        #plt.show()

    def graphPlot(self, nomePosto):
        self.findPosto()   # Chama a função self.findPosto()
        globals()['datas%d' % int(self.ano_usuario)] = []   # Definição de listas dinâmicas para plot
        globals()['vazao%d' % int(self.ano_usuario)] = []                      
        for i in range(len(self.dados)):                       
            data_arq  = self.dados[i][0]    # data_arq é a variável que armazena todas as datas existentes no arquivo no formato string                    
            data      = Data(data_arq)  # Instanciação do objeto Data         
            if (data.ano == int(self.ano_usuario)):
                vazao = self.dados[i][self.indice_posto]    # vazao é a variável que armazena todas as vazões no periodo escolhido
                globals()['vazao%d' % int(self.ano_usuario)].append(int(vazao))
                globals()['datas%d' % int(self.ano_usuario)].append(data.diasAno())

        # Plotagem dos dados no mesmo gráfico, caso queira em gráficos separados, descomentar a linha plt.figure(self.qtd_graph) 
        plt.plot(globals()['datas%d' % int(self.ano_usuario)], globals()['vazao%d' % int(self.ano_usuario)], linewidth = self.line_plot)
        plt.title(nomePosto + "no ano de " + str(self.ano_usuario)) # Título que indica o primeiro ano escolhido até  ultimo plotado
        plt.xlabel('Dias')
        plt.ylabel('Vazoes (m^3/s)')
        #plt.show()

    def vazoesDia(self):
        # Chama a função self.findPosto()
        self.findPosto()      
        for i in range(self.dados.__len__()):                       
            data_arq  = self.dados[i][0]    # data_arq é a variável que armazena todas as datas existentes no arquivo no formato string              
            data      = Data(data_arq)  # Instanciação do objeto Data
            if (data.ano == int(self.ano_usuario)):
                vazao = self.dados[i][self.indice_posto]    # vazao é a variável que armazena todas as vazões no periodo escolhido
                self.listaData.append(float(data.diasAno()))
                self.listaVazao.append(float(vazao))