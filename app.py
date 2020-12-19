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
	anguloRadianos = math.acos(cos)
	anguloGraus = 180*anguloRadianos/np.pi

	return float((int(anguloGraus*10000)))/10000


def formatText(text):
	if ',' in text:
		text = text.replace(',', '.')
	
	return float(text)


def deslocaEixo(curva, novaRef):
	novaCurva = []
	for ponto in vetor:
		aux = []
		aux = aux + [ponto[0] - novaRef[0]]
		aux = aux + [ponto[1] - novaRef[1]]
		novaCurva = novaCurva + [aux]
	return novaCurva

def buscaPontoRandom(pontos):
	return r.randint(0,len(pontos))

def nuvemPontos(pontosX, pontosY, color='blue'):
	# plt.plot(pontosX, pontosY)
	plt.scatter(pontosX, pontosY, marker="x", color=color)
	# plt.show()

def plotPnL(pontosX, pontosY, titulo=''):
	nuvemPontos(pontosX, pontosY)
	
	plt.title('titulo')
	plt.xlabel('G(S)')
	plt.ylabel('B(S)')

	plt.show()
	# plt.savefig('test.png')

# arquivo = open('/home/mauricio/Documentos/MEGA/Projeto Lugar Geométrico/0/x.txt', 'r')
# x = arquivo.read()
# arquivo.close()
# x = x.split('\n')
# if x[-1] == '':
# 	x.pop()

# arquivo = open('/home/mauricio/Documentos/MEGA/Projeto Lugar Geométrico/0/y.txt', 'r')
# y = arquivo.read()
# arquivo.close()
# y = y.split('\n')
# if y[-1] == '':
# 	y.pop()

# n_x = [formatText(num) for num in x]
# n_y = [formatText(num) for num in y]

# plotPnL(n_x, n_y)
