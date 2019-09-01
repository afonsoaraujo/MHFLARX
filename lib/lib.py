# -*- coding:utf-8 -*

import numpy as np                   # Biblioteca padrão (Python 3.X), baixada (Python 2.X)
from matplotlib import pyplot as plt # Biblioteca baixada (matplotlib)
from scipy import stats
import numpy as np
import csv
import statsmodels.api as sm

class Data:
    
    '''
    A classe Data tem função de instanciar objetos no formato de data no seguinte formato: "AAAA-MM-DD"
    Onde "AAAA" é o ano em 4 digitos, "MM" é o mes com 2 digitos, "DD" é o dia com 2 digitos.

    Atributos:
        data     --> é a definição da string a ser tratada
        bissexto --> é a definição da variável booleana para verificação do ano bissexto
        dias     --> é uma lista contendo o numero de dias referentes aos meses do ano não bissexto
        diasB    --> é uma lista contendo o número de dias referentes aos meses do ano bissexto
        nomes    --> é uma lista contendo os nomes com 3 caracteres referentes aos meses do ano

    Métodos:
        __init__(self, data) --> função de instanciação do objeto data, necessita da string no formato correto.
        anoBissexto(self) --> função que retorna se o ano é bissexto ou não
        diasMes(self, mes) --> função que retorna o numero de dias do mes indicado
        diasAno(self) --> função que retorna uma lista com os dias do ano em análise
    
    '''
    data = ""
    bissexto = False
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    diasB = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    nomes = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN",
             "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"]

    def __init__(self, data):
        self.ano = int(data[6:10])
        self.mes = int(data[0:2])
        self.dia = int(data[3:5])

    def anoBissexto(self):
        if ((self.ano % 4 == 0 and self.ano % 100 != 0) or self.ano % 400 == 0):
            self.bissexto = True
            return self.bissexto
        else:
            self.bissexto = False
            return self.bissexto

    def diasMes(self, mes):
        self.anoBissexto()
        if(self.anoBissexto == True):
            if(mes == 1):
                return self.diasB[0]
            if(mes == 2):
                return self.diasB[1]
            if(mes == 3):
                return self.diasB[2]
            if(mes == 4):
                return self.diasB[3]
            if(mes == 5):
                return self.diasB[4]
            if(mes == 6):
                return self.diasB[5]
            if(mes == 7):
                return self.diasB[6]
            if(mes == 8):
                return self.diasB[7]
            if(mes == 9):
                return self.diasB[8]
            if(mes == 10):
                return self.diasB[9]
            if(mes == 11):
                return self.diasB[10]
            if(mes == 12):
                return self.diasB[11]
        else:
            if(mes == 1):
                return self.dias[0]
            if(mes == 2):
                return self.dias[1]
            if(mes == 3):
                return self.dias[2]
            if(mes == 4):
                return self.dias[3]
            if(mes == 5):
                return self.dias[4]
            if(mes == 6):
                return self.dias[5]
            if(mes == 7):
                return self.dias[6]
            if(mes == 8):
                return self.dias[7]
            if(mes == 9):
                return self.dias[8]
            if(mes == 10):
                return self.dias[9]
            if(mes == 11):
                return self.dias[10]
            if(mes == 12):
                return self.dias[11]

    def diasAno(self):
        self.anoBissexto()
        if(self.bissexto == True):
            listaAno = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
            41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,
            82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,
            117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,
            148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,
            179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,
            210,211,212,213,214,215,216,217,218,219,220,221,223,224,225,226,227,228,229,230,231,232,233,234,235,235,236,237,238,239,240,
            241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,
            272,273,274,275,276,277,278,279,280,
            281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,
            312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,
            343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366]
            return listaAno
        else:
            listaAno = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
            41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,
            82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,
            117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,
            148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,
            179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,
            210,211,212,213,214,215,216,217,218,219,220,221,223,224,225,226,227,228,229,230,231,232,233,234,235,235,236,237,238,239,240,
            241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,
            272,273,274,275,276,277,278,279,280,
            281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,
            312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,
            343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365]
            return listaAno

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
        listaPosto      --> é uma lista contendo todos os postos a serem analisados, é um input de dados

    Métodos:
        __init__(self, ano, posto, qtd_graph, dados, listaPosto) --> função de instanciação do objeto dadosArq, as informações tem que ser passadas na ordem correta
        findPosto(self) --> função que encontra o posto escolhido na lista de postos geral
        vazoesDia_CEPEL(self) --> função que faz a leitura dos dados do CEPEL
        vazoesDia_ANA(self) --> função que faz a leitura dos dados do ANA
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
                        print(j)
                        print(len(self.listaVazao))
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

class analiseRec_CEPEL:
    '''
    A classe analiseRec_CEPEL tem função de realizar a analise de recessão do posto escolhido com base no banco de dados do CEPEL

    Esté código tem função de analisar as recessões de no posto escolhido pelo usuario durante o tempo escolhido e retornar
    esses dados numa matriz de n recessões em n anos.

    Para que o código funcione é preciso 2 arquivos:
        VazoesDiarias.csv
            Arquivo do Cepel contendo as vazões, em escala diária, das bacias hidrográficas desde 1932.
    
        Postos e parametros.csv
            Arquivo contendo o nome dos postos e parametros que auxiliam a filtragem (tiRec, varVazao).

    Atributos:
        input_ano        --> input do ano escolhido
        input_posto      --> input do posto escolhido
        input_deltaT     --> input da quantidade de anos observada
        input_database   --> input de uma matriz contendo todos os dados utilizaveis do arquivo principal
        input_postos     --> input de uma lista contendo todos os postos a serem analisados
        input_parametros --> input de uma matriz contendo todos os dados utilizaveis do arquivo de parametros

    Métodos:
        __init__(self, ano, posto, deltaT, database, listaP, parametros) --> função de instanciação do objeto dadosArq, as informações tem que ser passadas na ordem correta
        filtroRec(self, tiRec, varVazao) --> função que faz o primeiro filtro de recessões
        plotRecTotal(self, indGraph) --> função que plota a recessão
        analise(self) --> função que faz a analise em conjunto com as funções anteriores

    '''
    matrizRecessao  = []    # Matriz com os vetores de recessão do ano escolhido
    vetorRecDias    = []    # Lista com o vetor de dias para recessão, para todos os n anos agrupados
    vetorRecVazao   = []    # Lista com o vetor de vazão para recessão, para todos os n anos agrupados
    recVazao        = []    # lista com todas as recessões para o calculo de autocorrelação

    def __init__(self, ano, posto, deltaT, database, listaP, parametros):
        self.input_ano        = int(ano)
        self.input_posto      = int(posto)
        self.input_deltaT     = int(deltaT)
        self.input_database   = database
        self.input_postos     = listaP
        self.input_parametros = parametros

    def filtroRec(self, tiRec, varVazao):
        d = 0
        i = 0
        j = 0
        jmax = 5
        if(self.tiRec == 'N/A'):
            self.tiRec = 5
        else:
            self.tiRec = int(self.tiRec)
        for d in range(len(self.dados.listaData)):
            if (self.derivada[d] < 0 ):
                if (i >= self.tiRec):
                    try:
                        if ( abs(self.dados.listaVazao[d + 1] - self.dados.listaVazao[d]) <= self.varVazao):
                            if (j > jmax):
                                self.vetorRecDias.insert(d, 0)
                                self.vetorRecVazao.insert(d, 0)
                                if (d == int(self.dados.listaData[-1])):
                                    break
                            else:
                                if (self.derivada[d + self.tfRec - 2] < 0):
                                    if (self.derivada[d + self.tfRec - 1] < 0):
                                        if (self.derivada[d + self.tfRec] < 0):
                                            self.vetorRecDias.insert(d, self.dados.listaData[d])
                                            self.vetorRecVazao.insert(d, self.dados.listaVazao[d])
                                            self.recVazao.insert(d, self.dados.listaVazao[d])
                                            i = i + 1
                                else:
                                    self.vetorRecDias.insert(d, 0)
                                    self.vetorRecVazao.insert(d, 0)
                                    i = 0
                                if (d == int(self.dados.listaData[-1])):
                                    break
                                j = j + 1
                        else:
                            j = 0
                            if (self.derivada[d + self.tfRec - 2] < 0):
                                if (self.derivada[d + self.tfRec - 1] < 0):
                                    if (self.derivada[d + self.tfRec] < 0):
                                        self.vetorRecDias.insert(d, self.dados.listaData[d])
                                        self.vetorRecVazao.insert(d, self.dados.listaVazao[d])
                                        self.recVazao.insert(d, self.dados.listaVazao[d])
                                        i = i + 1
                            else:
                                self.vetorRecDias.insert(d, 0)
                                self.vetorRecVazao.insert(d, 0)
                                i = 0
                            if (d == int(self.dados.listaData[-1])):
                                break
                    except IndexError:
                        if (abs(self.dados.listaVazao[-1] - self.dados.listaVazao[d]) <= self.varVazao):
                            if (j > jmax):
                                self.vetorRecDias.insert(d, 0)
                                self.vetorRecVazao.insert(d, 0)
                                if (d == int(self.dados.listaData[-1])):
                                    break
                            else:
                                if (self.derivada[int(self.dados.listaData[-1]) - 3] < 0):
                                    if (self.derivada[int(self.dados.listaData[-1]) - 2] < 0):
                                        if (self.derivada[int(self.dados.listaData[-1]) - 1] < 0):
                                            self.vetorRecDias.insert(d, self.dados.listaData[d])
                                            self.vetorRecVazao.insert(d, self.dados.listaVazao[d])
                                            self.recVazao.insert(d, self.dados.listaVazao[d])
                                            i = i + 1
                                else:
                                    self.vetorRecDias.insert(d, 0)
                                    self.vetorRecVazao.insert(d, 0)
                                    i = 0
                                if (d == int(self.dados.listaData[-1])):
                                    break
                                j = j + 1
                        else:
                            j = 0
                            if (self.derivada[int(self.dados.listaData[-1]) - 3] < 0):
                                if (self.derivada[int(self.dados.listaData[-1]) - 2] < 0):
                                    if (self.derivada[int(self.dados.listaData[-1]) - 1] < 0):
                                        self.vetorRecDias.insert(d, self.dados.listaData[d])
                                        self.vetorRecVazao.insert(d, self.dados.listaVazao[d])
                                        self.recVazao.insert(d, self.dados.listaVazao[d])
                                        i = i + 1
                            else:
                                self.vetorRecDias.insert(d, 0)
                                self.vetorRecVazao.insert(d, 0)
                                i = 0
                            if (d == int(self.dados.listaData[-1])):
                                break
                else:
                    i = i + 1
                    self.vetorRecDias.insert(d,0)
                    self.vetorRecVazao.insert(d,0)
            else:
                if (d == int(self.dados.listaData[-1])):
                    break
                else:
                    try:
                        if (len(self.recVazao) <= 4): 
                            self.vetorRecDias.insert(d,0)
                            self.vetorRecVazao.insert(d,0)
                            i = 0
                        else:
                            self.vetorRecDias.insert(d,0)
                            self.vetorRecVazao.insert(d,0)
                            i = 0
                    except ValueError:
                        self.vetorRecDias.insert(d,0)
                        self.vetorRecVazao.insert(d,0)
                        i = 0
    
    def plotRecTotal(self, indGraph):
        plt.plot(self.matrizRecessao[indGraph], self.matrizRecessao[indGraph + 1], 'o', ms = 2)
        plt.title("Recessao")
        plt.xlabel("Dias")
        plt.ylabel("Vazão")
    
    def analise(self):
        self.dados = dadosArq(self.input_ano, self.input_posto, self.input_deltaT, self.input_database, self.input_postos)
        self.dados.vazoesDia_CEPEL()

        for i in range(len(self.input_parametros)):
            if (str(self.input_posto) == self.input_parametros[i][0]):
                self.tiRec     = self.input_parametros[i][3] # tempo mínimo para inicio de uma recessão (DEPENDE DE UMA DETERMINADA BACIA)
                self.tfRec     = 2     # tempo minimo anterior do fim de uma recessão (DEPENDE DE UMA DETERMINADA BACIA) [VALOR MÍNIMO: 2]
                try:
                    self.varVazao  = float(self.input_parametros[i][4])     # Variação minima de vazao entre recessão
                except ValueError:
                    self.varVazao  = 15    # Variação alterável
                    print("A variavel varVazao não foi encontrada e está no valor default de: " + str(self.varVazao) + ".")
                self.nomePosto = self.input_parametros[i][2]     # Nome do Posto
                ''' Definição de variaveis e listas de rotinas '''
                self.derivada        = []    # Lista da derivada da vazao do ano q
                
                ''' Funções principais '''
                self.derivada = np.gradient(self.dados.listaVazao)    # Calcula a derivada da vazão
                self.filtroRec(self.tiRec, self.varVazao)    # Chama a função que filtra os dados da vazao anual
                self.matrizRecessao.append(self.vetorRecDias)   # Adiciona os dias de recessão ao vetor geral de recessão
                self.matrizRecessao.append(self.vetorRecVazao)    # Adiciona a vazão da recessão ao vetor geral de recessão

class analiseRec_ANA:
    '''
    A classe analiseRec_ANA tem função de realizar a analise de recessão do posto escolhido com base no banco de dados do ANA

    Esté código tem função de analisar as recessões de no posto escolhido pelo usuario durante o tempo escolhido e retornar
    esses dados numa matriz de n recessões em n anos.

    Para que o código funcione é preciso 1 arquivo que segue o padrão de base de dados do ANA disponível em seu site

    Atributos:
        input_ano        --> input do ano escolhido
        input_deltaT     --> input da quantidade de anos observada
        input_database   --> input de uma matriz contendo todos os dados utilizaveis do arquivo principal
       
    Métodos:
        __init__(self, ano, posto, deltaT, database, listaP, parametros) --> função de instanciação do objeto dadosArq, as informações tem que ser passadas na ordem correta
        filtroRec(self, tiRec, varVazao) --> função que faz o primeiro filtro de recessões
        plotRecTotal(self, indGraph) --> função que plota a recessão
        analise(self) --> função que faz a analise em conjunto com as funções anteriores

    '''
    matrizRecessao  = []    # Matriz com os vetores de recessão do ano escolhido
    vetorRecDias    = []    # Lista com o vetor de dias para recessão, para todos os n anos agrupados
    vetorRecVazao   = []    # Lista com o vetor de vazão para recessão, para todos os n anos agrupados
    recVazao        = []    # lista com todas as recessões para o calculo de autocorrelação

    def __init__(self, ano, deltaT, database):
        self.input_ano        = int(ano)
        self.input_deltaT     = int(deltaT)
        self.input_database   = database

    def filtroRec(self, tiRec, varVazao):
        d = 0
        i = 0
        j = 0
        jmax = 5
        if(self.tiRec == 'N/A'):
            self.tiRec = 5
        else:
            self.tiRec = int(self.tiRec)
        for d in range(len(self.dados.listaData)):
            if (self.derivada[d] < 0 ):
                if (i >= self.tiRec):
                    try:
                        if ( abs(self.dados.listaVazao[d + 1] - self.dados.listaVazao[d]) <= self.varVazao):
                            if (j > jmax):
                                self.vetorRecDias.insert(d, 0)
                                self.vetorRecVazao.insert(d, 0)
                                if (d == int(self.dados.listaData[-1])):
                                    break
                            else:
                                if (self.derivada[d + self.tfRec - 2] < 0):
                                    if (self.derivada[d + self.tfRec - 1] < 0):
                                        if (self.derivada[d + self.tfRec] < 0):
                                            self.vetorRecDias.insert(d, self.dados.listaData[d])
                                            self.vetorRecVazao.insert(d, self.dados.listaVazao[d])
                                            self.recVazao.insert(d, self.dados.listaVazao[d])
                                            i = i + 1
                                else:
                                    self.vetorRecDias.insert(d, 0)
                                    self.vetorRecVazao.insert(d, 0)
                                    i = 0
                                if (d == int(self.dados.listaData[-1])):
                                    break
                                j = j + 1
                        else:
                            j = 0
                            if (self.derivada[d + self.tfRec - 2] < 0):
                                if (self.derivada[d + self.tfRec - 1] < 0):
                                    if (self.derivada[d + self.tfRec] < 0):
                                        self.vetorRecDias.insert(d, self.dados.listaData[d])
                                        self.vetorRecVazao.insert(d, self.dados.listaVazao[d])
                                        self.recVazao.insert(d, self.dados.listaVazao[d])
                                        i = i + 1
                            else:
                                self.vetorRecDias.insert(d, 0)
                                self.vetorRecVazao.insert(d, 0)
                                i = 0
                            if (d == int(self.dados.listaData[-1])):
                                break
                    except IndexError:
                        if (abs(self.dados.listaVazao[-1] - self.dados.listaVazao[d]) <= self.varVazao):
                            if (j > jmax):
                                self.vetorRecDias.insert(d, 0)
                                self.vetorRecVazao.insert(d, 0)
                                if (d == int(self.dados.listaData[-1])):
                                    break
                            else:
                                if (self.derivada[int(self.dados.listaData[-1]) - 3] < 0):
                                    if (self.derivada[int(self.dados.listaData[-1]) - 2] < 0):
                                        if (self.derivada[int(self.dados.listaData[-1]) - 1] < 0):
                                            self.vetorRecDias.insert(d, self.dados.listaData[d])
                                            self.vetorRecVazao.insert(d, self.dados.listaVazao[d])
                                            self.recVazao.insert(d, self.dados.listaVazao[d])
                                            i = i + 1
                                else:
                                    self.vetorRecDias.insert(d, 0)
                                    self.vetorRecVazao.insert(d, 0)
                                    i = 0
                                if (d == int(self.dados.listaData[-1])):
                                    break
                                j = j + 1
                        else:
                            j = 0
                            if (self.derivada[int(self.dados.listaData[-1]) - 3] < 0):
                                if (self.derivada[int(self.dados.listaData[-1]) - 2] < 0):
                                    if (self.derivada[int(self.dados.listaData[-1]) - 1] < 0):
                                        self.vetorRecDias.insert(d, self.dados.listaData[d])
                                        self.vetorRecVazao.insert(d, self.dados.listaVazao[d])
                                        self.recVazao.insert(d, self.dados.listaVazao[d])
                                        i = i + 1
                            else:
                                self.vetorRecDias.insert(d, 0)
                                self.vetorRecVazao.insert(d, 0)
                                i = 0
                            if (d == int(self.dados.listaData[-1])):
                                break
                else:
                    i = i + 1
                    self.vetorRecDias.insert(d,0)
                    self.vetorRecVazao.insert(d,0)
            else:
                if (d == int(self.dados.listaData[-1])):
                    break
                else:
                    try:
                        if (len(self.recVazao) <= 4): 
                            self.vetorRecDias.insert(d,0)
                            self.vetorRecVazao.insert(d,0)
                            i = 0
                        else:
                            self.vetorRecDias.insert(d,0)
                            self.vetorRecVazao.insert(d,0)
                            i = 0
                    except ValueError:
                        self.vetorRecDias.insert(d,0)
                        self.vetorRecVazao.insert(d,0)
                        i = 0
    
    def plotRecTotal(self, indGraph):
        plt.plot(self.matrizRecessao[indGraph], self.matrizRecessao[indGraph + 1], 'o', ms = 2)
        plt.title("Recessao")
        plt.xlabel("Dias")
        plt.ylabel("Vazão")
    
    def analise(self):
        self.dados = dadosArq(self.input_ano, 0, self.input_deltaT, self.input_database, [])
        self.dados.vazoesDia_ANA()

        self.tiRec     = 2     # tempo mínimo para inicio de uma recessão (DEPENDE DE UMA DETERMINADA BACIA)
        self.tfRec     = 4     # tempo minimo anterior do fim de uma recessão (DEPENDE DE UMA DETERMINADA BACIA) [VALOR MÍNIMO: 2]
        self.varVazao  = 1     # Variação minima de vazao entre recessão
        ''' Definição de variaveis e listas de rotinas '''
        self.derivada        = []    # Lista da derivada da vazao do ano q
                
        ''' Funções principais '''
        self.derivada = np.gradient(self.dados.listaVazao)    # Calcula a derivada da vazão
        self.filtroRec(self.tiRec, self.varVazao)    # Chama a função que filtra os dados da vazao anual
        self.matrizRecessao.append(self.vetorRecDias)   # Adiciona os dias de recessão ao vetor geral de recessão
        self.matrizRecessao.append(self.vetorRecVazao)    # Adiciona a vazão da recessão ao vetor geral de recessão

class AjusteLinear:
    '''
    A classe ajusteLinear - Realiza o Ajuste Linear - escrito por Lucas Ribeiro Magalhães - UFRJ

    Esse código tem como saida o ajuste linear das recessões previamente analisadas no arquivo analiseRec.py
    O ajuste é nas vazões q(t) x q(t+1)

    O ajuste é feito e em seguida é retornado as constantes K do filtro auto regressivo

    O código também faz a separação de constantes por meio da função ginput() e refaz o ajuste linear
    '''
    Ks = []         # lista com as constantes de cada regressão linear
    constante = 1   # Essa varrável indica a necessidade de separar em mais constantes de tempo, caso 0 sim, caso 1 não

    def __init__(self, lista):
        self.input_lista = lista

    # Plot Qt x Qt+1 e regressao linear
    def regreLinear(self, lista):
        lista = np.asarray(lista)
        x = lista[:, np.newaxis]
        self.coefAngular, _, _, _ = np.linalg.lstsq(x[:len(x) - 1], lista[1:len(lista)], rcond=None)
        
        #Plot dos dados
        plt.plot(lista[:len(lista) - 1], lista[1:len(lista)], 'o', label = "Qt x Qt+1")
        plt.legend()
        plt.plot(lista[:len(lista) - 1], self.coefAngular*np.array(lista[:len(lista) - 1 ]), 'r', label = 'Ajuste Linear', linewidth = 0.5)
        plt.legend()
        plt.title("Ajuste Linear")
        plt.xlabel("Vazão")
        plt.ylabel("Vazao + 1")
        return self.coefAngular
    
    def separaK(self, lista):
        if (self.constante == 1):
            x = plt.ginput(1, show_clicks = True)       
            self.lista1 = []
            self.lista2 = []
            for i in range(len(lista)):
                if (lista[i] > int(x[0][0])):
                    self.lista1.append(lista[i])
                else:
                    self.lista2.append(lista[i])

            plt.figure(10)
            self.K1 = self.regreLinear(self.lista1)
            plt.figure(11)
            self.K2 = self.regreLinear(self.lista2)

            self.Ks.append(self.K1)
            self.Ks.append(self.K2)
        else:
            self.K = self.regreLinear(lista)
            self.Ks.append(self.K)
        print(self.Ks)  

class filtroAR_CEPEL:
    '''
    A classe filtroAR realiza a filtragem auto regressiva de ordem 1
    
    '''  

    def __init__(self, ano, posto, deltaT, dados, listaPosto):
        self.input_ano       = int(ano)
        self.input_posto     = str(posto)
        self.input_deltaT    = 1
        self.input_database  = dados
        self.input_postos    = listaPosto
        self.yn1AR1          = [] #Componente lenta
        self.yn2AR1          = [] #Comoponente componente intermediaria./rapida

        # Instanciação de um novo objeto vazão
        self.vazao = dadosArq(self.input_ano, self.input_posto, self.input_deltaT, self.input_database, self.input_postos)
        self.vazao.vazoesDia_CEPEL()
        self.yn        = self.vazao.listaVazao # Vazão total
        self.listaData = self.vazao.listaData  # Lista Data
        self.yn2       = []

        # instanciação do objeto ajuste linear
        self.ajuste = AjusteLinear(self.yn)
        self.ajuste.regreLinear(self.yn)
        self.ajuste.separaK(self.yn)

    def filtroAR1(self):
        if (len(self.ajuste.Ks) > 1):
            # Primeiro filtra o sinal yn com K1
            T1 = float(abs(1/(np.log(self.ajuste.Ks[0])))) #Constante para Yn1
            T2 = float(abs(1/(np.log(self.ajuste.Ks[1])))) #Constante para Yn2
            print(T1)
            print(T2)
            alpha1 = 0.98 #Constante para Yn1
            alpha2 = 0.97 #Constante para Yn2
            deltaT = 1 #Intervalo de discretização
            for i in range(len(self.yn)):
                try:
                    if i == 0:
                        sinalFiltradoK1 = (deltaT/T1)*self.yn[i]
                        self.yn1AR1.insert(i, sinalFiltradoK1)
                    else:
                        sinalFiltradoK1 = (deltaT/T1)*self.yn[i] + alpha1*((1 - (deltaT/T1))*self.yn1AR1[i-1])
                        self.yn1AR1.insert(i, sinalFiltradoK1)
                except IndexError:
                    sinalFiltradoK1 = (deltaT/T1)*self.yn[i] + alpha1*((1 - (deltaT/T1))*self.yn1AR1[i-1])
                    self.yn1AR1.insert(i, sinalFiltradoK1)
                sinalYn2 = self.yn[i] - self.yn1AR1[i]
                self.yn2.insert(i, sinalYn2)
                if (sinalYn2 <= 0):
                    print("Diminua o Alpha1!")
                    break
            for i in range(len(self.yn2)):
                try:
                    if i == 0:
                        sinalFiltradoK2 = (deltaT/T2)*self.yn2[i]
                        self.yn2AR1.insert(i, sinalFiltradoK2)
                    else:
                        sinalFiltradoK2 = (deltaT/T2)*self.yn2[i] + alpha2*((1 - (deltaT/T2))*self.yn2AR1[i-1])
                        self.yn2AR1.insert(i, sinalFiltradoK2)
                except IndexError:
                    sinalFiltradoK2 = (deltaT/T2)*self.yn2[i] + alpha2*((1 - (deltaT/T2))*self.yn2AR1[i-1])
                    self.yn2AR1.insert(i, sinalFiltradoK2)
                sinalYn3 = self.yn2[i] - self.yn2AR1[i]
                if (sinalYn3 <= 0):
                    print("Diminua o Alpha2!")
                    break
        else:
            T = float(abs(1/(np.log(self.ajuste.Ks[0]))))
            alpha = 0.9
            deltaT = 1
            for i in range(len(self.yn)):
                try:
                    if i == 0:
                        sinalFiltradoK1 = (deltaT/T)*self.yn[i]
                        self.yn1AR1.insert(i, sinalFiltradoK1)
                    else:
                        sinalFiltradoK1 = (deltaT/T)*self.yn[i] + alpha*((1 - (deltaT/T))*self.yn1AR1[i-1])
                        self.yn1AR1.insert(i, sinalFiltradoK1)
                except IndexError:
                    sinalFiltradoK1 = (deltaT/T)*self.yn[i] + alpha*((1 - (deltaT/T))*self.yn1AR1[i-1])
                    self.yn1AR1.insert(i, sinalFiltradoK1)
                sinalYn2 = self.yn[i] - self.yn1AR1[i]
                if (sinalYn2 <= 0):
                    print("Diminua o Alpha1!")
                    break

        plt.figure(0)
        plt.title("Componente Lenta para o Posto: ...  no ano de " + str(self.input_ano))
        plt.plot(self.listaData, self.yn, linewidth = 0.5)
        plt.plot(self.listaData, self.yn1AR1, 'r--', linewidth = 0.5)

        plt.figure(0)
        plt.title("Componente Intermediaria para o Posto: ...  no ano de " + str(self.input_ano))
        plt.plot(self.listaData, self.yn2AR1, 'g-.', linewidth = 0.5)

class filtroAR_ANA:
    '''
    A classe filtroAR realiza a filtragem auto regressiva de ordem 1
    
    '''  

    def __init__(self, ano, deltaT, dados):
        self.input_ano       = int(ano)
        self.input_deltaT    = 1
        self.input_database  = dados
        self.yn1AR1          = [] #Componente lenta
        self.yn2AR1          = [] #Comoponente componente intermediaria./rapida

        # Instanciação de um novo objeto vazão
        self.vazaoFiltro = dadosArq(self.input_ano, 0, self.input_deltaT, self.input_database, [])
        self.vazaoFiltro.vazoesDia_ANA()
        self.yn        = self.vazaoFiltro.listaVazao # Vazão total
        self.listaData = self.vazaoFiltro.listaData  # Lista Data
        self.yn2       = []

        # instanciação do objeto ajuste linear
        self.ajuste = AjusteLinear(self.yn)
        self.ajuste.regreLinear(self.yn)
        self.ajuste.separaK(self.yn)

    def filtroAR1(self):
        if (len(self.ajuste.Ks) > 1):
            # Primeiro filtra o sinal yn com K1
            T1 = float(abs(1/(np.log(self.ajuste.Ks[0])))) #Constante para Yn1
            T2 = float(abs(1/(np.log(self.ajuste.Ks[1])))) #Constante para Yn2
            print(T1)
            print(T2)
            alpha1 = 0.5 #Constante para Yn1
            alpha2 = 0.5 #Constante para Yn2
            deltaT = 1 #Intervalo de discretização
            for i in range(len(self.yn)):
                try:
                    if i == 0:
                        sinalFiltradoK1 = (deltaT/T1)*self.yn[i]
                        self.yn1AR1.insert(i, sinalFiltradoK1)
                    else:
                        sinalFiltradoK1 = (deltaT/T1)*self.yn[i] + alpha1*((1 - (deltaT/T1))*self.yn1AR1[i-1])
                        self.yn1AR1.insert(i, sinalFiltradoK1)
                except IndexError:
                    sinalFiltradoK1 = (deltaT/T1)*self.yn[i] + alpha1*((1 - (deltaT/T1))*self.yn1AR1[i-1])
                    self.yn1AR1.insert(i, sinalFiltradoK1)
                sinalYn2 = self.yn[i] - self.yn1AR1[i]
                self.yn2.insert(i, sinalYn2)
                if (sinalYn2 <= 0):
                    print("Diminua o Alpha1!")
                    break
            for i in range(len(self.yn2)):
                try:
                    if i == 0:
                        sinalFiltradoK2 = (deltaT/T2)*self.yn2[i]
                        self.yn2AR1.insert(i, sinalFiltradoK2)
                    else:
                        sinalFiltradoK2 = (deltaT/T2)*self.yn2[i] + alpha2*((1 - (deltaT/T2))*self.yn2AR1[i-1])
                        self.yn2AR1.insert(i, sinalFiltradoK2)
                except IndexError:
                    sinalFiltradoK2 = (deltaT/T2)*self.yn2[i] + alpha2*((1 - (deltaT/T2))*self.yn2AR1[i-1])
                    self.yn2AR1.insert(i, sinalFiltradoK2)
                sinalYn3 = self.yn2[i] - self.yn2AR1[i]
                if (sinalYn3 <= 0):
                    print("Diminua o Alpha2!")
                    break
        else:
            T = float(abs(1/(np.log(self.ajuste.Ks[0]))))
            alpha = 0.9
            deltaT = 1
            for i in range(len(self.yn)):
                try:
                    if i == 0:
                        sinalFiltradoK1 = (deltaT/T)*self.yn[i]
                        self.yn1AR1.insert(i, sinalFiltradoK1)
                    else:
                        sinalFiltradoK1 = (deltaT/T)*self.yn[i] + alpha*((1 - (deltaT/T))*self.yn1AR1[i-1])
                        self.yn1AR1.insert(i, sinalFiltradoK1)
                except IndexError:
                    sinalFiltradoK1 = (deltaT/T)*self.yn[i] + alpha*((1 - (deltaT/T))*self.yn1AR1[i-1])
                    self.yn1AR1.insert(i, sinalFiltradoK1)
                sinalYn2 = self.yn[i] - self.yn1AR1[i]
                if (sinalYn2 <= 0):
                    print("Diminua o Alpha1!")
                    break

        plt.figure(0)
        plt.title("Componente Lenta para o Posto: ...  no ano de " + str(self.input_ano))
        plt.plot(self.listaData, self.yn, linewidth = 0.5)
        plt.plot(self.listaData, self.yn1AR1, 'r--', linewidth = 0.5)

        plt.figure(0)
        plt.title("Componente Intermediaria para o Posto: ...  no ano de " + str(self.input_ano))
        plt.plot(self.listaData, self.yn2AR1, 'g-.', linewidth = 0.5)