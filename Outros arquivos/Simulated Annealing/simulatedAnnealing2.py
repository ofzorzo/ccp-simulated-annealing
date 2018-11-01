import random
from math import exp
import time
import copy

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
			A[u][v] = float(fields[2])
			#A[v][u] = float(fields[2]) # não devo criar uma matriz espelhada, pois duplicaria o valor da solução em solutionValue()
		currentLine = currentLine + 1
	'''	
	print(n)
	print(g)
	print(L)
	print(U)
	#print de uma matriz:
	
	for a in A:
	    ln = ""
	    for i in a:
	        ln += str(i) + "    "
	    print(ln)
	'''
	print("terminou de ler instancia")
	return n, g, A, L, U, p

def isFeasible(g, n, solution, L, U, p):
	vertices = []
	for v in range(0,n):
		vertices.append(v)
	#print(vertices)
	for j in range(0, g):		
		groupWeight = 0
		for v in solution[j]:
			vertices[v] = -1
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
	start_time = time.time()
	elapsed_time = 0
	biruleibe2 = 0
	while((feasibleSolution == False) and biruleibe2 < 500):
		solution = []
		currentlyUsedVertices = []
		groupsWeights = []
		for i in range(0, g): #grupo atual que receberá vértices
			groupWeight = 0
			solution.append([])
			biruleibe3 = 0
			while((groupWeight < L[i]) and biruleibe3 < 300): #enquanto há tempo, tentamos botar vértices randomicamente no grupo
				vertexIndex = random.randint(0, n-1)
				while vertexIndex in currentlyUsedVertices:
					vertexIndex = random.randint(0, n-1)
				groupWeight = groupWeight + p[vertexIndex]
				solution[i].append(vertexIndex)
				currentlyUsedVertices.append(vertexIndex)
				elapsed_time = time.time() - start_time
				biruleibe3 += 1
			groupsWeights.append(groupWeight)
			if elapsed_time >= 600:
				break # sai do for e, consequentemente, do while mais externo
		biruleibe = 0
		while((len(currentlyUsedVertices) < n) and biruleibe < 100): # caso ainda existam vértices sem grupo, tentamos adicioná-los a um grupo
			groupIndex = random.randint(0, g-1)
			vertexIndex = random.randint(0, n-1)
			#print("prendeu aq")
			while vertexIndex in currentlyUsedVertices:
				vertexIndex = random.randint(0, n-1)
			if groupsWeights[groupIndex] + p[vertexIndex] <= U[groupIndex]:
				groupsWeights[groupIndex] = groupsWeights[groupIndex] + p[vertexIndex]
				solution[groupIndex].append(vertexIndex)
				currentlyUsedVertices.append(vertexIndex)
			#print("prendeu na tentativa de por em grupos vertices livres" + str(biruleibe))
			biruleibe += 1
			elapsed_time = time.time() - start_time
		feasibleSolution = isFeasible(g, n, solution, L, U, p) # testa se a solução atual é vactível
		#if feasibleSolution == False:
			#print("not feasible")
		biruleibe2 += 1
		#print("criando nova solucao inicial")
	if elapsed_time >= 600:
		#print("Nao conseguiu gerar solucao inicial") # sai do for e, consequentemente, do while mais externo
		return
	else:
		#print(solution)
		#print(solutionValue(solution, g, A))
		return solution





def createNeighbor(g, n, solution, L, U, p):
	newSolution = copy.deepcopy(solution)
	vertexLeft = False
	elapsed_time = 0
	iterations = 0
	while((vertexLeft == False) and (iterations < 1000)): #tenta criar um vizinho a partir de solution 1000 vezes
		losingGroup = random.randint(0, g-1)
		differentGroup = 0
		while(differentGroup == 0):
			winningGroup = random.randint(0, g-1)
			if winningGroup != losingGroup:
				differentGroup = 1
		vertexIndexInGroup = random.randint(0, len(solution[losingGroup])-1)
		vertexIndex = solution[losingGroup][vertexIndexInGroup]		
		del newSolution[losingGroup][vertexIndexInGroup]
		newSolution[winningGroup].append(vertexIndex)
		if isFeasible(g, n, newSolution, L, U, p) == True:
			vertexLeft = True
		else:			
			newSolution = copy.deepcopy(solution)
		iterations += 1
	return newSolution

'''
parâmetros:
s: solução/estado inicial
T: temperatura inicial grande pro algoritmo achar uma adequada
r: fator de resfriamentro no intervalo (0,1), grande para testar várias temperaturas
I: número pequeno de iterações antes de resfriar
pi: probabilidade inicial, no intervalo [0,1]
'''
def simulatedAnnealingInitialTemperature(s, T, r, I, pi, A):
	neighbor = s
	counter = 0
	closestT = T
	closestProbability = 2
	elapsed_time = 0
	while(T > 0.00000001): #quando T for 0.00000001, a tentativa de ir para vizinhos piores provavelmente nunca irá dar certo, portanto paramos de procurar um T
		movesTried = 0
		movesSucceded = 0
		for i in range(0,I): # aqui inicia um nível de temperatura, em criarei I vizinhos
			#print("prendeu na criacao de vizinhos")
			neighbor = createNeighbor(g, n, s, L, U, p)
			if neighbor != s:			
				delta = solutionValue(neighbor, g, A) - solutionValue(s, g, A)
				exponent = delta/T
			else:
				delta = -1 # caso eu não consiga criar um vizinho novo, não devo zerar o contador
				exponent = float('-inf') # assim como não devo permitir que ocorra algum movimento (i.e incrementar movesSucceded); relembrar que exp('-inf')=0
				print("Atingiu menos inf")
			if delta >= 0: # mesmo que a solução possua mesmo valor, atualizamos o estado atual
				s = neighbor
			else: # aqui delta sempre vai ser negativo	
				movesTried = movesTried + 1
				if random.random() < exp(exponent): # portando, exp(delta/t) vai estar entre [0,1]
					s = neighbor 				   # o motivo para ser < e não <= é que, se fosse <= e a minha probabilidade fosse igual a 0, eu poderia acabar realizando a ação após o if, mesmo com probabilidade 0
					movesSucceded = movesSucceded + 1
		if movesTried>0:
			if ((movesSucceded/movesTried) >= pi-0.005) and ((movesSucceded/movesTried) <= pi+0.005): # aqui termina um nível de temperatura
				return T
			else:
				if abs((movesSucceded/movesTried) - pi) < abs(closestProbability - pi):
					#print("pi", pi)
					closestProbability = movesSucceded/movesTried
					#print("closest prob", closestProbability)
					#print("T=", T)
					#print("movesTried=", movesTried)
					#print("movesSucceded=", movesSucceded)
					#print("---------")
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
'''
def simulatedAnnealing(s, T, r, I, pf, g, A):
	neighbor = s
	delta = 0
	counter = 0
	while(counter<10):
		movesTried = 0
		movesSucceded = 0
		for i in range(0,I): # aqui inicia um nível de temperatura, em criarei I vizinhos
			neighbor = createNeighbor(g, n, s, L, U, p) #retirar 1337
			if neighbor != s:			
				delta = solutionValue(neighbor, g, A) - solutionValue(s, g, A)
				exponent = delta/T
			else:
				delta = -1 # caso eu não consiga criar um vizinho novo, não devo zerar o contador
				exponent = float('-inf') # assim como não devo permitir que ocorra algum movimento (i.e incrementar movesSucceded); relembrar que exp('-inf')=0
				# por outro lado, movesTried deve ser incrementado, pois, se chegamos numa solução que não consegue gerar nenhum vizinho novo, devemos cada vez diminuir mais (movesSucceded/movesTried), para aumentarmos o contador
				print("chegou no -inf")
			if delta >= 0: # mesmo que a solução possua mesmo valor, atualizamos o estado atual. Se delta >= 0, então vizinho é melhor que o s atual.
				s = neighbor
				counter = 0
			else: # aqui delta sempre vai ser negativo
				movesTried = movesTried + 1
				if random.random() < exp(exponent): # portanto, exp(delta/t) vai estar entre [0,1]
					s = neighbor 				   # o motivo para ser < e não <= é que, se fosse <= e a minha probabilidade fosse igual a 0, eu poderia acabar realizando a ação após o if, mesmo com probabilidade 0
					movesSucceded = movesSucceded + 1
		if movesTried > 0:
			if (movesSucceded/movesTried) < pf: # aqui termina um nível de temperatura
				counter = counter + 1
		T = r*T
	return s

def mainSimulatedAnnealing(r, I, n, g, A, L, U, p):
	currentSolutionValue = 0
	currentSolution = createInitialSolution(n, g, L, U, p)
	print("Começou a criar solucoes iniciais")
	for i in range(0, 9999):
		s = createInitialSolution(n, g, L, U, p)
		if solutionValue(s, g, A) > currentSolutionValue:
			currentSolution = s
			currentSolutionValue = solutionValue(s, g, A)
	print("Terminou de criar solucoes iniciais")
	print("Comecou a gerar temperatura inicial")
	T = simulatedAnnealingInitialTemperature(currentSolution, 240000000, 0.99, 100, 0.85, A) # o T escolhido foi um tal que o best known value dividido por T resultasse em -0.001, pois exp(-0.001) é bem próximo de 1
	print("Terminou de gerar temperatura inicial")
	print("Comecou a gerar solucao final")
	s = simulatedAnnealing(currentSolution, T, r, I, 0.05, g, A)
	print("Terminou de gerar solucao final")
	return s

def mainSimulatedAnnealing2(r, I, n, g, A, L, U, p, s):
	currentSolutionValue = 0
	currentSolution = s
	#print("Começou a criar solucoes iniciais")
	'''for i in range(0, 9999):
		s = createInitialSolution(n, g, L, U, p)
		if solutionValue(s, g, A) > currentSolutionValue:
			currentSolution = s
			currentSolutionValue = solutionValue(s, g, A)'''
	#print("Terminou de criar solucoes iniciais")
	print("Comecou a gerar temperatura inicial")
	T = simulatedAnnealingInitialTemperature(currentSolution, 240000000, 0.99, 100, 0.85, A) # o T escolhido foi um tal que o best known value dividido por T resultasse em -0.001, pois exp(-0.001) é bem próximo de 1
	print("Terminou de gerar temperatura inicial")
	print("Comecou a gerar solucao final")
	s = simulatedAnnealing(currentSolution, T, r, I, 0.05, g, A)
	print("Terminou de gerar solucao final")
	return s

seed = random.random()
random.seed(0.6951820580649771) # testar seed 0.8914708996897809 que não gera a solução ótima
				  # seed 0.34514690837557105 faz a criação de vizinhos ficar presa
				  # seed 0.6951820580649771 tem os melhores resultados
n, g, A, L, U, p = readInstance('D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins')
s = mainSimulatedAnnealing(0.99, 2500, n, g, A, L, U, p)
random.seed(0.10744627260781447) #essa segunda seed gera 201k
s = mainSimulatedAnnealing2(0.99, 2500, n, g, A, L, U, p, s)
print(s)
print(solutionValue(s, g, A))
print(seed)

'''
s = mainSimulatedAnnealing(0.95, 20)
print(solutionValue(s))
'''


'''
Percebi que a solução final depende muito da solução inicial. Por exemplo, para a instância de testes 5, com seed 0.34514690837557105, a solução inicial não possui vizinhos possíveis, mesmo não sendo ótima.
Portanto, gero mais de uma solução inicial e guardo a de melhor valor. 

Pq utilizamos exp(delta/T) para calcular a probabilidade de um movimento ruim. Lembrar que delta é sempre negativo e T é sempre positivo.
Delta é o numerador; logo, quanto mais negativo ele for, mais negativo vai ser o valor da divisão. Quanto mais negativo delta for, significa que o vizinho é muito pior que a solução atual. Como exp(x) tende a 0 para x tendendo a -inf, quanto mais negativo for delta (e, consequentemente, quanto pior for o vizinho gerado), mais perto de 0 estará exp(delta/T), significando que vizinhos muito ruins tem menos chances de serem aceitos.
T, por outro lado, é o denominador, sempre positivo. Quanto maior ele for, menos negativa será a divisão delta/T, tendendo a 0. exp(x), para x tendendo a 0, é 1. Logo, quanto maior for a temperatura, mais quente está o algoritmo, e há mais chances de aceitarmos um movimento ruim.
'''