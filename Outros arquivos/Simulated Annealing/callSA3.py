import subprocess

#testa I
cmd5 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "50", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/I50v2.txt"]
process = subprocess.Popen(cmd5, stdout=subprocess.PIPE)

cmd6 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "250", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/I250v2.txt"]
process = subprocess.Popen(cmd6, stdout=subprocess.PIPE)

cmd7 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "500", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/I500v2.txt"]
process = subprocess.Popen(cmd7, stdout=subprocess.PIPE)

cmd8 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "1000", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/I1000v2.txt"]
process = subprocess.Popen(cmd8, stdout=subprocess.PIPE)