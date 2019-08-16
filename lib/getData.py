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
            m = self.mes
            i = 0
            totalDiasAno = 0
            if(m == 1):
                totalDiasAno = self.dia
                return totalDiasAno
            else:
                for i in range(m-1):
                    totalDias = int(self.diasB[i])
                    totalDiasAno = totalDiasAno + totalDias
                totalDiasAno = totalDiasAno + self.dia
                return totalDiasAno
        else:
            m = self.mes
            i = 0
            totalDiasAno = 0
            if(m == 1):
                totalDiasAno = self.dia
                return totalDiasAno
            else:
                for i in range(m-1):
                    totalDias = int(self.dias[i])
                    totalDiasAno = totalDiasAno + totalDias
                totalDiasAno = totalDiasAno + self.dia
                return totalDiasAno

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