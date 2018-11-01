import subprocess

#k
cmd17 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-k", "2", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/k2v2.txt"]
process = subprocess.Popen(cmd17, stdout=subprocess.PIPE)

cmd16 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-k", "4", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/k4v2.txt"]
process = subprocess.Popen(cmd16, stdout=subprocess.PIPE)