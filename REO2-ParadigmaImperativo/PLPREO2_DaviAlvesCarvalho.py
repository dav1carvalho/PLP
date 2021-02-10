# UTF-8
import sys
import math

nome_do_arquivo = sys.argv[1]

cont = 0
arq = open(nome_do_arquivo, 'r')

with open(nome_do_arquivo) as file:
    file.seek(0)
    verifica_dado = file.read(1)
    if not verifica_dado:
        print("O arquivo está vazio!")
        exit()
    else:
        file.seek(0)


for linha in arq:
    cont += 1

arq.close()


xs = []
ys = []

arq1 = open(nome_do_arquivo, 'r')
try:

    for linha in arq1.readlines():
        x, y = map(float, linha.split(','))
        xs.append(x)
        ys.append(y)

    somaX = 0
    somaY = 0

    for soma in xs:
        somaX += soma

    for soma in ys:
        somaY += soma

    mediaX = somaX/cont
    mediaY = somaY/cont

    aux = 0
    soma_cima = 0

    while aux < cont:
        soma_cima = soma_cima + ((xs[aux] - mediaX)*(ys[aux] - mediaY))
        aux += 1

    aux1 = 0
    quadradoX = 0
    quadradoY = 0

    while aux1 < cont:
        quadradoX = quadradoX + ((xs[aux1] - mediaX)**2)
        quadradoY = quadradoY + ((ys[aux1] - mediaY)**2)
        aux1 += 1

    raiz_baixo = math.sqrt((quadradoX * quadradoY))

    coeficiente = soma_cima/raiz_baixo

    print(coeficiente)

except ValueError:
    print("Os dados são inválidos!!")
    exit()

arq1.close()
