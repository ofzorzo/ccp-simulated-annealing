import subprocess

#testa r
cmd = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.90", "-I", "2500", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/r090v2.txt"]
process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

cmd2 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.95", "-I", "2500", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/r095v2.txt"]
process = subprocess.Popen(cmd2, stdout=subprocess.PIPE)

#cmd3 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/r099v2.txt"]
#process = subprocess.Popen(cmd3, stdout=subprocess.PIPE)