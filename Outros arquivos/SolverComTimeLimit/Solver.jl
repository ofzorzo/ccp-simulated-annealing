
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
    A = zeros(n,n) #matriz de adjacência em que cada elemento representa o peso da aresta entre o vértice u e v; não posso fazer com que seja uma matriz espelhada pois acabaria duplicando o valor da função objetivo
    for lineIndex=4:numberOfLines
    	currentLine = split(lines[lineIndex])
    	u = parse(Int64, currentLine[1]) + 1 #vértice de índice u aqui tem índice u-1 na instância
        v = parse(Int64, currentLine[2]) + 1
        A[u,v] = parse(Float64, currentLine[3])
    end
    return n, g, p, L, U, A
end

n, g, p, L, U, A = createGraphFromFile("D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins")

using JuMP
using GLPKMathProgInterface
m = Model(solver=GLPKSolverMIP(msg_lev=GLPK.MSG_ON, tm_lim=7))

@variable(m, x[1:n, 1:g], Bin) #g é o número de grupos
@variable(m, c[1:n, 1:n, 1:g], Bin) #g é o número de grupos
@objective( m, Max, sum( c[i,k,j]*A[i,k] for i in 1:n for k in 1:n for j in 1:g ) ) # passa por todos i's, k's e j's, portanto a matriz A não pode ser espelhada, pois isso faria eu considerar o valor de uma aresta duas vezes
@constraints(m, begin
[i in 1:n], sum(x[i,j] for j in 1:g)==1
[j in 1:g], L[j]<=sum( x[i,j]*p[i] for i in 1:n )<=U[j]
[i in 1:n, k in 1:n, j in 1:g], c[i,k,j]<=(x[i,j]+x[k,j])/2 # isso daqui garante que vou ter tanto c[1,2,j] quanto c[2,1,j], então não preciso me preocupar com qual vértice escolher pra i e qual pra k na função objetivo

end)
solve(m)