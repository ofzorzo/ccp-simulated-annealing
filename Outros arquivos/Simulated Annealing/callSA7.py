import subprocess

#nsi
cmd15 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/nsi1v2.txt", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-nsi", "1",  "-r", "0.99", "-I", "2500", "-pf", "0.05", "-k", "1", "-pi", "0.85"]
process = subprocess.Popen(cmd15, stdout=subprocess.PIPE)

cmd17 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/nsi100v2.txt", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-nsi", "100",  "-r", "0.99", "-I", "2500", "-pf", "0.05", "-k", "1", "-pi", "0.85"]
process = subprocess.Popen(cmd17, stdout=subprocess.PIPE)

cmd16 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/nsi1000v2.txt", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-nsi", "1000", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-k", "1", "-pi", "0.85"]
process = subprocess.Popen(cmd16, stdout=subprocess.PIPE)