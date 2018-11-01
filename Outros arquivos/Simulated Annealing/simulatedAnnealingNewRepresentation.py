import random
from math import exp
import copy
import argparse
import time

def readInstance(filename):
	file = open(filename)
	currentLine = 1
	L = [] #limite inferior do grupo j
	U = [] #limite superior do grupo j
	p = [] #peso de cada vértice
	for line in file:
		fields = line.strip().split()
		if currentLine == 1:
			n = int(fields[0])
			g = int(fields[1])
			A = [[0 for x in range(n)] for y in range(n)]

		if currentLine == 2:
			for j in range(0, g):
				L.append(float(fields[j*2]))
				U.append(float(fields[j*2+1]))

		if currentLine == 3:
			for i in range(0, n):
				p.append(float(fields[i]))

		if currentLine > 3:
			u = int(fields[0])
			v = int(fields[1])
			A[u][v] = float(fields[2]) # não devo criar uma matriz espelhada, pois duplicaria o valor da solução em solutionValue()
		currentLine = currentLine + 1

	file.close()
	print("Terminou de ler instancia")
	return n, g, A, L, U, p

def isFeasible(g, n, solution, L, U, p):
	vertices = []
	for v in range(0,n):
		vertices.append(v) # cria lista de vértices da instância do problema
	for j in range(0, g):		
		groupWeight = 0
		for v in solution[j]:
			vertices[v] = -1 # quando um vértice é visitado, marcamos ele com -1 na lista de vértices
			groupWeight = groupWeight + p[v]
		if (groupWeight < L[j]) or (groupWeight > U[j]):
			return False
	for v in vertices:
		if v != -1:
			return False
	return True

def solutionValue(solution, g, A):
	value = 0
	for j in range(0, g):
		for v in solution[j]:
			for v2 in solution[j]:
				value = value + A[v][v2]
	return value

def createInitialSolution(n, g, L, U, p):
	feasibleSolution = False
	outerIterations = 0
	if n < 100:
		maxIterations = 10000
	else:
		maxIterations = n*n
	while((feasibleSolution == False) and outerIterations < maxIterations):
		solution = []
		currentlyUsedVertices = []
		groupsWeights = []
		for j in range(0, g): #grupo atual que receberá vértices
			groupWeight = 0
			solution.append([])
			innerIterations = 0
			while((groupWeight < L[j]) and innerIterations < maxIterations): #enquanto há tempo, tentamos botar vértices randomicamente no grupo, até atingirmos ou ultrapassarmos seu limite inferior
				vertexIndex = random.randint(0, n-1)
				innerInnerIterations = 0
				while vertexIndex in currentlyUsedVertices:
					if innerInnerIterations == maxIterations:
						exit("Não foi possível criar uma solução inicial factível, embora possa existir uma.")
					vertexIndex = random.randint(0, n-1)
					innerInnerIterations += 1
				groupWeight = groupWeight + p[vertexIndex]
				solution[j].append(vertexIndex)
				currentlyUsedVertices.append(vertexIndex)
				innerIterations += 1
			groupsWeights.append(groupWeight)
		innerIterations = 0
		while((len(currentlyUsedVertices) < n) and innerIterations < maxIterations): # caso ainda existam vértices sem grupo, tentamos adicioná-los a um grupo
			groupIndex = random.randint(0, g-1)
			vertexIndex = random.randint(0, n-1)
			innerInnerIterations = 0
			while vertexIndex in currentlyUsedVertices:
				if innerInnerIterations == maxIterations:
						exit("Não foi possível criar uma solução inicial factível, embora possa existir uma.")
				vertexIndex = random.randint(0, n-1)
				innerInnerIterations += 1
			if groupsWeights[groupIndex] + p[vertexIndex] <= U[groupIndex]:
				groupsWeights[groupIndex] = groupsWeights[groupIndex] + p[vertexIndex]
				solution[groupIndex].append(vertexIndex)
				currentlyUsedVertices.append(vertexIndex)
			innerIterations += 1
		feasibleSolution = isFeasible(g, n, solution, L, U, p) # testa se a solução atual é vactível
		outerIterations += 1
	if outerIterations == 500:
		exit("Não foi possível criar uma solução inicial factível, embora possa existir uma.")
	return solution

def createNeighbor(g, n, solution, L, U, p, kChange):
	newSolution = copy.deepcopy(solution) #trabalhamos sempre com uma cópia da solução atual, pois ela é passada por referência e não queremos alterá-la
	vertexLeft = False 					  # até termos certeza de que a nova solução (gerada pela vizinhança) realmente é factível
	feasibleNewSolution = copy.deepcopy(newSolution)
	iterations = 0
	numberOfChanges = 0
	changedVertices = []
	if n < 100:
		maxIterations = 10000
	else:
		maxIterations = n*n
	while numberOfChanges < kChange:
		vertexLeft = False
		while((vertexLeft == False) and (iterations < maxIterations)): #tenta criar um vizinho a partir de solution n vezes
			losingGroup = random.randint(0, g-1)
			while(len(newSolution[losingGroup]) < 1):
				losingGroup = random.randint(0, g-1)
			differentGroup = 0
			while(differentGroup == 0):
				winningGroup = random.randint(0, g-1)
				if winningGroup != losingGroup:
					differentGroup = 1
			if len(newSolution[losingGroup]) == 1:
				vertexIndexInGroup = 0
			else:
				vertexIndexInGroup = random.randint(0, len(newSolution[losingGroup])-1) #escolhe um vértice do grupo sorteado para perder um vértice
				while newSolution[losingGroup][vertexIndexInGroup] in changedVertices:
					vertexIndexInGroup = random.randint(0, len(newSolution[losingGroup])-1)
			vertexIndex = newSolution[losingGroup][vertexIndexInGroup]	#descobre qual o índice real, no contexto da instância do problema, desse vértice
			del newSolution[losingGroup][vertexIndexInGroup] #deleta o vértice do grupo perdedor...
			newSolution[winningGroup].append(vertexIndex) #... e o adiciona ao grupo ganhador
			if isFeasible(g, n, newSolution, L, U, p) == True:
				vertexLeft = True
				changedVertices.append(vertexIndex)
				feasibleNewSolution = copy.deepcopy(newSolution)
			else:			
				newSolution = copy.deepcopy(feasibleNewSolution)
			iterations += 1
		numberOfChanges += 1
	return newSolution

'''
parâmetros:
s: solução/estado inicial
T: temperatura inicial grande pro algoritmo achar uma adequada
r: fator de resfriamentro no intervalo (0,1), grande para testar várias temperaturas
I: número pequeno de iterações antes de resfriar
pi: probabilidade inicial, no intervalo [0,1]
A: matriz de adjacência não-espelhada
n: nro de vértices
g: nro de grupos
kChange: número de trocas a serem realizadas na criação de um vizinho
'''
def simulatedAnnealingInitialTemperature(s, T, r, I, pi, n, g, A, kChange):
	neighbor = s
	counter = 0
	closestT = T
	closestProbability = 2
	while(T > 0.00000001): #quando T for 0.00000001, a tentativa de ir para vizinhos piores provavelmente nunca irá dar certo, portanto paramos de procurar um T
		movesTried = 0
		movesSucceded = 0
		for i in range(0,I):
			neighbor = createNeighbor(g, n, s, L, U, p, kChange)
			if neighbor != s:			
				delta = solutionValue(neighbor, g, A) - solutionValue(s, g, A)
				exponent = delta/T
			else:
				delta = -1
				exponent = float('-inf') 
			if delta >= 0:
				s = neighbor
			else:
				movesTried = movesTried + 1
				if random.random() < exp(exponent):
					s = neighbor 				    
					movesSucceded = movesSucceded + 1
		if movesTried>0:
			if ((movesSucceded/movesTried) >= pi-0.005) and ((movesSucceded/movesTried) <= pi+0.005):
				return T
			else:
				if abs((movesSucceded/movesTried) - pi) < abs(closestProbability - pi):
					closestProbability = movesSucceded/movesTried
					closestT = T
		T = r*T
	return closestT

'''
parâmetros:
s: solução/estado inicial; uma solução é dada por uma lista de listas. Cada lista representa um grupo, e os valores em cada lista representam os índices dos vértices que estão nesse grupo.
T: temperatura inicial
r: fator de resfriamentro no intervalo (0,1)
I: número de iterações antes de resfriar
pf: probabilidade final, no intervalo [0,1]
A: matriz de adjacência não-espelhada
n: nro de vértices
g: nro de grupos
kChange: número de trocas a serem realizadas na criação de um vizinho
'''
def simulatedAnnealing(s, T, r, I, pf, n, g, A, kChange):
	neighbor = s
	delta = 0
	counter = 0
	while(counter<10):
		movesTried = 0
		movesSucceded = 0
		for i in range(0,I): # Aqui inicia um nível de temperatura, no qual serão criados I vizinhos
			neighbor = createNeighbor(g, n, s, L, U, p, kChange)
			if neighbor != s:			
				delta = solutionValue(neighbor, g, A) - solutionValue(s, g, A)
				exponent = delta/T
			else:
				delta = -1 				 # caso eu não consiga criar um vizinho novo, não devo zerar o contador
				exponent = float('-inf') # assim como não devo permitir que ocorra algum movimento (i.e incrementar movesSucceded); relembrar que exp('-inf')=0
										 # por outro lado, movesTried deve ser incrementado, pois, se chegamos numa solução que não consegue gerar nenhum vizinho novo, devemos cada vez diminuir mais (movesSucceded/movesTried), para aumentarmos o contador
			if delta >= 0: # mesmo que a solução atual possua o mesmo valor do vizinho, atualizamos ela
				s = neighbor
				counter = 0
			else:
				movesTried = movesTried + 1
				if random.random() < exp(exponent): #Ao entrar nesse else, delta sempre vai ser negativo. Logo, exp(delta/t) vai estar entre [0,1]
					s = neighbor 				    #O if acima deve ser < e não <=, já que <= poderia executar o corpo do if mesmo que a probabilidade com que quero atualizar minha solução para pior ( exp(exponent) ) fosse 0.
					movesSucceded = movesSucceded + 1
		if movesTried > 0:
			if (movesSucceded/movesTried) < pf:
				counter = counter + 1
		T = r*T
	return s

def mainSimulatedAnnealing(r, I, n, g, A, L, U, p, pf, pi, kChange, nsi): #p é uma lista com os pesos de cada vértice, enquanto pi e pf são, respectivamente, probabilidade final e inicial
	currentSolutionValue = 0
	currentSolution = createInitialSolution(n, g, L, U, p)
	currentSolutionValue = solutionValue(currentSolution, g, A)
	print("Começou a criar solucoes iniciais")
	for i in range(0, nsi):
		s = createInitialSolution(n, g, L, U, p)
		if solutionValue(s, g, A) > currentSolutionValue:
			currentSolution = s
			currentSolutionValue = solutionValue(s, g, A)
	print("Terminou de criar solucoes iniciais")
	print("Valor da solução inicial: " + str(currentSolutionValue))
	print("Comecou a gerar temperatura inicial")
	T = simulatedAnnealingInitialTemperature(currentSolution, 1000000000, r, 100, pi, n, g, A, kChange) # o T é grande o suficiente para que, de início, a probabilidade de um movimento ruim ser aceito seja bem próxima de 1
																						 # como estamos rodando esse SA apenas para determinar uma temperatura inicial adequada, utilizamos um I pequeno (100)
	print("Terminou de gerar temperatura inicial")
	print("Comecou a gerar solucao final")
	s = simulatedAnnealing(currentSolution, T, r, I, pf, n, g, A, kChange)
	print("Terminou de gerar solucao final")
	return s, currentSolutionValue


seed = random.random()

parser = argparse.ArgumentParser()
parser.add_argument('OutputFile', type=str, nargs='+', help='caminho desejado para o arquivo que contém o log da execução do algoritmo; recomenda-se botar o caminho entre aspas')
parser.add_argument('InstanceFile', type=str, nargs='+', help='caminho para o arquivo que contém a instância do problema; recomenda-se botar o caminho entre aspas')
parser.add_argument('-r', type=float, nargs=1, help='fator de resfriamento')
parser.add_argument('-I', type=int, nargs=1, help='número de vizinhos criados em uma mesma temperatura')
parser.add_argument('-pf', type=float, nargs=1, help='probabilidade mínima de aceitação de movimentos ruins; caso a taxa de aceitação seja menor que pf, algoritmo para (resfria)')
parser.add_argument('-pi', type=float, nargs=1, help='probabilidade inicial desejada para a aceitação de movimentos ruins')
parser.add_argument('-seed', type=float, nargs=1, help='seed a ser usada pelo algoritmo; se nenhuma for passada, é gerada uma aleatoriamente')
parser.add_argument('-k', type=int, nargs=1, help='número de trocas para a vizinhança k-change')
parser.add_argument('-nsi', type=int, nargs=1, help='número de soluções iniciais a serem criadas pelo algoritmo; escolhe a melhor delas')
args = parser.parse_known_args()

if args[0].r is None:
	r = 0.99
else:
	r = args[0].r[0]

if args[0].I is None:
	I = 2500
else:
	I = args[0].I[0]

if args[0].pf is None:
	pf = 0.05
else:
	pf = args[0].pf[0]

if args[0].pi is None:
	pi = 0.85
else:
	pi = args[0].pi[0]

if args[0].k is None:
	kChange = 1
else:
	kChange = args[0].k[0]

if args[0].nsi is None:
	nsi = 10000
else:
	nsi = args[0].nsi[0]

if args[0].seed is not None:
	seed = args[0].seed[0]

random.seed(seed)

filename = ' '.join(args[0].InstanceFile)
n, g, A, L, U, p = readInstance(filename)

startTime = time.time()
s, initialSolutionValue = mainSimulatedAnnealing(r, I, n, g, A, L, U, p, pf, pi, kChange, nsi-1)
elapsedTime = time.time() - startTime

outname = ' '.join(args[0].OutputFile)
file = open(outname, "w")
file.write("Tempo levado:\n\t" + str(elapsedTime) + " segundos")
file.write("\n\nParâmetros:")
file.write("\n\tr  : " + str(r))
file.write("\n\tI  : " + str(I))
file.write("\n\tpf : " + str(pf))
file.write("\n\tpi : " + str(pi))
file.write("\n\tk  : " + str(kChange))
file.write("\n\tnsi: " + str(nsi))
file.write("\n\tseed: " + str(seed))
file.write("\n\nValor da solução inicial encontrada:\n\t" + str(initialSolutionValue))
file.write("\n\nValor da solução final encontrada:\n\t" + str(solutionValue(s, g, A)))
file.write("\n\nSolução encontrada:\n")
file.write("\t"+str(s))
file.close()

print("Valor da solução encontrada: " + str(solutionValue(s, g, A)))
print("Seed: " + str(seed))

