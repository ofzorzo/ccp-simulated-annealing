using GLPKMathProgInterface
using JuMP
lucro = [17, 10, 15, 19, 7, 13, 9 ]
custo = [43, 28, 34, 48, 17, 23, 23 ]
m = Model(solver=GLPKSolverMIP(msg_lev=GLPK.MSG_ON, tm_lim=0))
@variable(m, fazer[1:7], Bin)
@objective(m, Max, sum(lucro[i]*fazer[i] for i=1:7))
@constraints(m, begin
sum(custo[i]*fazer[i] for i=1:7)<=100
fazer[1]+fazer[2] <= 1
fazer[3]+fazer[4] <= 1
fazer[3]+fazer[4] <= fazer[1]+fazer[2]
end)
solve(m)
println("Projetos a serem executados:
$(find(x->x==1,map(x->convert(Int,getvalue(x)), fazer))) com lucro total
$(getobjectivevalue(m)).")
