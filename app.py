import matplotlib.pyplot as plt
import random as r
import math
import numpy as np

def norma(ponto):
	return (ponto[0]**2 + ponto[1]**2)**0.5


def produtoEscalar(ponto1, ponto2):
	return ponto1[0]*ponto2[0] + ponto1[1]*ponto2[1]


def anguloEntreVetores(ponto1, ponto2):
	norma1 = norma(ponto1)
	norma2 = norma(ponto2)

	produto_escalar = produtoEscalar(ponto1, ponto2)

	cos = produto_escalar/(norma1*norma2)
	if cos > 1:
		cos = 1
	if cos < -1:
		cos = -1
	anguloRadianos = math.acos(cos)
	anguloGraus = 180*anguloRadianos/np.pi

	return float((int(anguloGraus*10000)))/10000


def formatText(text):
	if ',' in text:
		text = text.replace(',', '.')
	
	return float(text)


def deslocaEixo(curva, novaRef):
	novaCurva = []
	for ponto in curva:
		aux = []
		aux = aux + [ponto[0] - novaRef[0]]
		aux = aux + [ponto[1] - novaRef[1]]
		novaCurva = novaCurva + [aux]

	return novaCurva

def buscaPontoRandom(pontos):
	return r.randint(0,len(pontos)-1)

def calculaMenorAngulo(vetorPontos):
	angulos = []
	for ponto in vetorPontos:
		if not(ponto[0] == 0 and ponto[1] == 0):
			angulos = angulos + [anguloEntreVetores([abs(ponto[0]), abs(ponto[1])], [1, 0])]
		else:
			angulos = angulos + [1000]

	indice = 0
	angulo = 1000
	for i in range(0, len(angulos)):
		if angulos[i] < angulo:
			angulo = angulos[i]
			indice = i

	return indice

def calculaMaiorAngulo(vetorPontos, ref):
	angulos = []
	for ponto in vetorPontos:
		if not(ponto[0] == 0 and ponto[1] == 0):
			angulos = angulos + [anguloEntreVetores(ponto, ref)]
		else:
			angulos = angulos + [0]

	indice = 0
	angulo = 0
	for i in range(0, len(angulos)):
		if angulos[i] > angulo:
			angulo = angulos[i]
			indice = i

	return indice

def buscaMenorR(vetorPontos):
	menorR = vetorPontos[0][0]
	indice = 0
	for i in range(0, len(vetorPontos)):
		if vetorPontos[i][0] < menorR:
			indice = i
			menorR = vetorPontos[i][0]

	return indice

def pnl(vetorPontos):
	vertices = []
	pontoAleatorio = buscaPontoRandom(vetorPontos)
	vertices = vertices + [calculaMenorAngulo(deslocaEixo(vetorPontos, vetorPontos[pontoAleatorio]))]

	novoVetorPontos = deslocaEixo(vetorPontos, vetorPontos[vertices[0]])
	vertices = vertices + [calculaMaiorAngulo(novoVetorPontos, novoVetorPontos[pontoAleatorio])]

	plt.scatter(vetorPontos[pontoAleatorio][0], vetorPontos[pontoAleatorio][1], marker="o", color="red")
	plt.scatter(vetorPontos[vertices[0]][0], vetorPontos[vertices[0]][1], marker="o", color="black")
	plt.scatter(vetorPontos[vertices[1]][0], vetorPontos[vertices[1]][1], marker="o", color="green")

	i = 1
	while vertices[i] != vertices[0] and i < 100:
		print(i)
		novoVetorPontos = deslocaEixo(vetorPontos, vetorPontos[vertices[i]])
		vertices = vertices + [calculaMaiorAngulo(novoVetorPontos, novoVetorPontos[vertices[i-1]])]
		i = i + 1


	novosVertices = set()
	for x in vertices:
		novosVertices.add(x)

	poligono = []
	for x in novosVertices:
		poligono = poligono + [vetorPontos[x]]

	vertices = []
	pontoAleatorio = buscaPontoRandom(poligono)
	vertices = vertices + [calculaMenorAngulo(deslocaEixo(poligono, poligono[pontoAleatorio]))]

	novoVetorPontos = deslocaEixo(poligono, poligono[vertices[0]])
	vertices = vertices + [calculaMaiorAngulo(novoVetorPontos, novoVetorPontos[pontoAleatorio])]

	i = 1
	while vertices[i] != vertices[0] and i < 100:
		print(i)
		novoVetorPontos = deslocaEixo(poligono, poligono[vertices[i]])
		vertices = vertices + [calculaMaiorAngulo(novoVetorPontos, novoVetorPontos[vertices[i-1]])]
		i = i + 1

	return vertices

	


def nuvemPontos(pontosX, pontosY, color='blue'):
	# plt.plot(pontosX, pontosY)
	plt.scatter(pontosX, pontosY, marker="x", color=color)
	# plt.show()

def plotPnL(pontosX, pontosY, titulo=''):
	nuvemPontos(pontosX, pontosY)
	
	plt.title(titulo)
	plt.xlabel('G(S)')
	plt.ylabel('B(S)')
	vertices = pnl(formata(pontosX, pontosY))

	plt.show()
	# plt.savefig('test.png')

def formata(pontosX, pontosY):
	vetor = []
	for i in range(0, len(pontosX)):
		aux = []
		aux = aux + [pontosX[i]]
		aux = aux + [pontosY[i]]
		vetor = vetor + [aux]

	return vetor

def main(TextoX, TextoY):
	arquivo = open(TextoX, 'r')
	x = arquivo.read()
	arquivo.close()
	x = x.split('\n')
	if x[-1] == '':
		x.pop()

	arquivo = open(TextoY, 'r')
	y = arquivo.read()
	arquivo.close()
	y = y.split('\n')
	if y[-1] == '':
		y.pop()

	n_x = [formatText(num) for num in x]
	n_y = [formatText(num) for num in y]

	plotPnL(n_x, n_y)



TextoX = '/home/mauricio/Documentos/MEGA/Projeto Lugar Geométrico/0/x.txt'
TextoY = '/home/mauricio/Documentos/MEGA/Projeto Lugar Geométrico/0/y.txt'
main(TextoX, TextoY)