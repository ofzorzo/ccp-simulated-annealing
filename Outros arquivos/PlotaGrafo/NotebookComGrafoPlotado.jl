
using LightGraphs
using GraphPlot

function createGraphFromFile(filename)
	f = open(filename)
	lines = readlines(f)
	firstLine = split(lines[1])
	n = parse(Int64, firstLine[1]) #número de vértices
	g = parse(Int64, firstLine[2]) #número de grupos
	graph = Graph(n)
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
    A = zeros(numberOfLines-3) #pesos de cada aresta
    for lineIndex=4:numberOfLines
    	currentLine = split(lines[lineIndex])
    	u = parse(Int64, currentLine[1]) + 1
        v = parse(Int64, currentLine[2]) + 1
        d_uv = parse(Float64, currentLine[3])
        A[lineIndex-3] = d_uv
        add_edge!(graph, u, v)
    end
    return n, g, p, L, U, A, graph
end

n, g, p, L, U, A, graph = createGraphFromFile("D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins")
teste = edges(graph)
#teste_zika = teste[4]
#print("$teste_zika\n")
#teste_zika2 = A[4]
#print("$teste_zika2")
gplot(graph)
