import subprocess

cmd = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/instanciaTeste.ins", "-seed 0.6951820580649771", "-r 0.99", "-I 2500", "-pf 0.05", "-pi 0.85", "-out D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/teste1.txt"]#, "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/instanciaTeste.ins", "-r 0.99", "-I 2500", "-pf 0.05", "-pi 0.85", "-seed 0.6951820580649771", "-out D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/teste1.txt"]
process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
for line in process.stdout:
	print(line)