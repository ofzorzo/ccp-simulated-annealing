
function createGraphFromFile(filename)
	f = open(filename)
	lines = readlines(f)
	firstLine = split(lines[1])
	n = parse(Int64, firstLine[1]) #número de vértices
	g = parse(Int64, firstLine[2]) #número de grupos
	secondLine = split(lines[2])
    L = zeros(g) #limite inferior do grupo j
    U = zeros(g) #limite superior do grupo j
    for j=1:g
    	L[j] = parse(Float64, secondLine[j*2-1])
    	U[j] = parse(Float64, secondLine[j*2])
    end
    p = zeros(n) #peso do vértice i
    thirdLine = split(lines[3])
    for i=1:n
    	p[i] = parse(Float64, thirdLine[i])
    end
    numberOfLines = size(lines)[1]
    A = zeros(n,n) #matriz de adjacência em que cada elemento representa o peso da aresta entre o vértice u e v
    for lineIndex=4:numberOfLines
    	currentLine = split(lines[lineIndex])
    	u = parse(Int64, currentLine[1]) + 1
        v = parse(Int64, currentLine[2]) + 1
        A[u,v] = parse(Float64, currentLine[3])
    end
    return n, g, p, L, U, A
end

n, g, p, L, U, A = createGraphFromFile("D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins")
#teste = edges(graph)
#teste_zika = teste[4]
#print("$teste_zika\n")
#teste_zika2 = A[4]
#print("$teste_zika2")
#gplot(graph)

using JuMP
using GLPKMathProgInterface
m = Model(solver=GLPKSolverMIP())

@variable(m, x[1:n, 1:g], Bin) #g é o número de grupos
@variable(m, c[1:n, 1:n, 1:g], Bin) #g é o número de grupos
@objective( m, Max, sum( c[i,k,j]*A[i,k] for i in 1:n for k in 1:n for j in 1:g ) )
@constraints(m, begin
[i in 1:n], sum(x[i,j] for j in 1:g)==1
[j in 1:g], L[j]<=sum( x[i,j]*p[i] for i in 1:n )<=U[j]
[i in 1:n, k in 1:n, j in 1:g], c[i,k,j]<=(x[i,j]+x[k,j])/2 # isso daqui garante que vou ter tanto c[1,2,j] quanto c[2,1,j], então não preciso me preocupar com qual vértice escolher pra i e qual pra k na função objetivo

end)
solve(m)
