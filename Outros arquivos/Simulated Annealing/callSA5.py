import subprocess

#pf
cmd14 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.15", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pf015v2.txt"]
process = subprocess.Popen(cmd14, stdout=subprocess.PIPE)

cmd15 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.10", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pf010v2.txt"]
process = subprocess.Popen(cmd15, stdout=subprocess.PIPE)

cmd17 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.01", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pf001v2.txt"]
process = subprocess.Popen(cmd17, stdout=subprocess.PIPE)