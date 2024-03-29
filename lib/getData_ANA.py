# -*- coding:utf-8 -*

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
        diasAno(self) --> função que retorna o número de dias que a data requerida tem no ano vigente
        diasMes(self) --> função que retorna o número de dias no mes têm
        proxDia(self) --> função que retorna o próximo dia com base na data inicial (DISCUTÍVEL A NECESSIDADE)
    '''
    data = ""
    bissexto = False
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    diasB = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    nomes = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN",
             "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"]

    def __init__(self, data):
        self.ano = int(data[6:10])
        self.dia = int(data[0:2])
        self.mes = int(data[3:5])

    def anoBissexto(self):
        if ((self.ano % 4 == 0 and self.ano % 100 != 0) or self.ano % 400 == 0):
            self.bissexto = True
            return self.bissexto
        else:
            self.bissexto = False
            return self.bissexto
        
    def diasMes(self, mes):
        self.anoBissexto()
        if(self.bissexto == True):
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

    def proxDia(self):
        self.anoBissexto()
        diaAtual = self.dia
        mesAtual = self.mes
        if (self.bissexto == True):
            if (diaAtual == 31):
                self.dia = 1
                if not (mesAtual == 12):
                    self.mes = self.mes + 1
                    return self.dia

            elif ((mesAtual == 4 or mesAtual == 6 or mesAtual == 9 or mesAtual == 11) and diaAtual == 30):
                self.dia = 1
                self.mes = self.mes + 1
                return self.dia

            elif (mesAtual == 2 and diaAtual == 29):
                self.dia = 1
                self.mes = self.mes + 1
                return self.dia

            else:
                self.dia = self.dia + 1
                return self.dia

        else:
            if (diaAtual == 31):
                self.dia = 1
                if not (mesAtual == 12):
                    self.mes = self.mes + 1
                    return self.dia

            elif ((mesAtual == 4 or mesAtual == 6 or mesAtual == 9 or mesAtual == 11) and diaAtual == 30):
                self.dia = 1
                self.mes = self.mes + 1
                return self.dia

            elif (mesAtual == 2 and diaAtual == 29):
                self.dia = 1
                self.mes = self.mes + 1
                return self.dia

            else:
                self.dia = self.dia + 1
                return self.dia
    
    def proxAno(self):
        self.ano = self.ano + 1