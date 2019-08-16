# -*- coding:utf-8 -*

import csv
import numpy as np

nomeArq          = "vazoes_C_65370000"
diretorioDados1  = "D:/OneDrive/MHFLARX/dados/"
diretorioDados2  = "C:/Users/lucas/OneDrive/MHFLARX/dados/"
header      = []    # Lista com o numero dos postos
listaData   = []
listaHora   = []
listavazoes1 = []

posto = "Var1"

''' Abertura do arquivo '''
try:
    # Leitura dos arquivos e disposição correta em forma matricial para análise
    with open(diretorioDados2 + nomeArq, "r") as csvfile:
        database = np.genfromtxt(csvfile, dtype = str, delimiter = ';', skip_header = )

    for p in range(len(database[0])-1):
        header.append(str(database[0][p]))

except FileNotFoundError:
    print("Arquivo não encontrado! Diretorio incorreto!")

indice_posto = header.index(posto)

for i in range(len(database)-1):
    listavazoes1.append(database[i+1][indice_posto])
    listaHora.append(database[i+1][1])
    listaData.append(database[i+1][0])
    
horainicial = int(listaHora[0][0:2])
minInicial  = int(listaHora[0][3:5])
deltaMinutoMin = int(listaHora[0][3:5]) - int(listaHora[1][3:5])


escala = 2 # 0 para escala diária, 1 para horária, 2 para minutos
''' para escalas de hora e minuto, escolher o delta t dentro de cada elif '''

if(escala == 0): # Escala diária
    listaDataAux = []
    listaVazaoAux = []
    somavazoes = 0
    contador = 0

    for k in range(len(database) - 1):
        try:
            if (listaData[k] == listaData[k+1]):
                contador = contador + 1
                somavazoes = somavazoes + float(listavazoes1[k])
            else:
                somavazoes = somavazoes + float(listavazoes1[k])
                contador = contador + 1
                media = somavazoes/contador
                listaDataAux.append(listaData[k-1])
                listaVazaoAux.append(media)
                contador = 0
                somavazoes = 0
        except IndexError:
            if (listaData[k] == listaData[-1]):
                contador = contador + 1
                somavazoes = somavazoes + float(listavazoes1[k])
            else:
                somavazoes = somavazoes + float(listavazoes1[k])
                contador = contador + 1
                media = somavazoes/contador
                listaDataAux.append(listaData[k-1])
                listaVazaoAux.append(media)
                contador = 0
                somavazoes = 0

elif(escala == 1): # Escala Horária
    deltaHora = 10
    listaDataAux = []
    listaHoraAux = []
    listaVazaoAux = []
    somavazoes = 0
    contador = 0

    for k in range(len(database) - 1):
        try:
            if (listaData[k] == listaData[k+1]):
                if not ((horainicial - int(listaHora[k+1][0:2])) == abs(deltaHora)):
                    contador = contador + 1
                    somavazoes = somavazoes + float(listavazoes1[k])
                else:
                    somavazoes = somavazoes + float(listavazoes1[k])
                    contador = contador + 1
                    media = somavazoes/contador
                    listaDataAux.append(listaData[k-1])
                    listaHoraAux.append(listaHora[k-1])
                    listaVazaoAux.append(media)
                    contador = 0
                    somavazoes = 0
                    horainicial = int(listaHora[k+1][0:2])
            else:
                somavazoes = somavazoes + float(listavazoes1[k])
                contador = contador + 1
                media = somavazoes/contador
                listaDataAux.append(listaData[k-1])
                listaHoraAux.append(listaHora[k-1])
                listaVazaoAux.append(media)
                contador = 0
                somavazoes = 0
                horainicial = int(listaHora[k+1][0:2])
        except IndexError:
            if (listaData[k] == listaData[-1]):
                if not ((horainicial - int(listaHora[-1][0:2])) == abs(deltaHora)):
                    contador = contador + 1
                    somavazoes = somavazoes + float(listavazoes1[k])
                else:
                    somavazoes = somavazoes + float(listavazoes1[k])
                    contador = contador + 1
                    media = somavazoes/contador
                    listaDataAux.append(listaData[k-1])
                    listaHoraAux.append(listaHora[k-1])
                    listaVazaoAux.append(media)
                    contador = 0
                    somavazoes = 0
                    horainicial = int(listaHora[-1][0:2])
            else:
                somavazoes = somavazoes + float(listavazoes1[k])
                contador = contador + 1
                media = somavazoes/contador
                listaDataAux.append(listaData[k-1])
                listaHoraAux.append(listaHora[k-1])
                listaVazaoAux.append(media)
                contador = 0
                somavazoes = 0
                horainicial = int(listaHora[-1][0:2])

elif(escala == 2): # Escala de minutos
    deltaMin = 4*deltaMinutoMin #Multiplo da variável deltaMinmínimo
    listaDataAux = []
    listaHoraAux = []
    listaVazaoAux = []
    somavazoes = 0
    contador = 0

    for k in range(len(database) - 1):
        try:
            if (listaData[k] == listaData[k+1]):
                if(int(listaHora[k][0:2]) == int(listaHora[k+1][0:2])):
                    if not ((minInicial - int(listaHora[k+1][3:5])) == abs(deltaMin)):
                        contador = contador + 1
                        somavazoes = somavazoes + float(listavazoes1[k])
                    else:
                        somavazoes = somavazoes + float(listavazoes1[k])
                        contador = contador + 1
                        media = somavazoes/contador
                        listaDataAux.append(listaData[k-1])
                        listaHoraAux.append(listaHora[k-1])
                        listaVazaoAux.append(media)
                        contador = 0
                        somavazoes = 0
                        minInicial = int(listaHora[k+1][3:5])
                else:
                    somavazoes = somavazoes + float(listavazoes1[k])
                    contador = contador + 1
                    media = somavazoes/contador
                    listaDataAux.append(listaData[k-1])
                    listaHoraAux.append(listaHora[k-1])
                    listaVazaoAux.append(media)
                    contador = 0
                    somavazoes = 0
                    minInicial = int(listaHora[k+1][3:5])
            else:
                somavazoes = somavazoes + float(listavazoes1[k])
                contador = contador + 1
                media = somavazoes/contador
                listaDataAux.append(listaData[k-1])
                listaHoraAux.append(listaHora[k-1])
                listaVazaoAux.append(media)
                contador = 0
                somavazoes = 0
                minInicial = int(listaHora[k+1][3:5])
        except IndexError:
            if (listaData[k] == listaData[-1]):
                if(int(listaHora[k][0:2]) == int(listaHora[-1][0:2])):
                    if not ((minInicial - int(listaHora[-1][3:5])) == abs(deltaMin)):
                        contador = contador + 1
                        somavazoes = somavazoes + float(listavazoes1[k])
                    else:
                        somavazoes = somavazoes + float(listavazoes1[k])
                        contador = contador + 1
                        media = somavazoes/contador
                        listaDataAux.append(listaData[k-1])
                        listaHoraAux.append(listaHora[k-1])
                        listaVazaoAux.append(media)
                        contador = 0
                        somavazoes = 0
                        minInicial = int(listaHora[-1][3:5])
                else:
                    somavazoes = somavazoes + float(listavazoes1[k])
                    contador = contador + 1
                    media = somavazoes/contador
                    listaDataAux.append(listaData[k-1])
                    listaHoraAux.append(listaHora[k-1])
                    listaVazaoAux.append(media)
                    contador = 0
                    somavazoes = 0
                    minInicial = int(listaHora[-1][3:5])
            else:
                somavazoes = somavazoes + float(listavazoes1[k])
                contador = contador + 1
                media = somavazoes/contador
                listaDataAux.append(listaData[k-1])
                listaHoraAux.append(listaHora[k-1])
                listaVazaoAux.append(media)
                contador = 0
                somavazoes = 0
                minInicial = int(listaHora[-1][3:5])