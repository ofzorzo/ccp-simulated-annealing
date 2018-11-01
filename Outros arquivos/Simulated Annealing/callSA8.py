import subprocess

#nsi
cmd1 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/gbmv240_01v2.txt", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-nsi", "10000", "-r", "0.99", "-I", "2500", "-pf", "0.01", "-k", "2", "-pi", "0.95"]
process = subprocess.Popen(cmd1, stdout=subprocess.PIPE)

cmd2 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/gbmv240_02v2.txt", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_02.ins", "-nsi", "10000", "-r", "0.99", "-I", "2500", "-pf", "0.01", "-k", "2", "-pi", "0.95"]
process = subprocess.Popen(cmd2, stdout=subprocess.PIPE)

cmd3 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/gbmv240_03v2.txt", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_03.ins", "-nsi", "10000", "-r", "0.99", "-I", "2500", "-pf", "0.01", "-k", "2", "-pi", "0.95"]
process = subprocess.Popen(cmd3, stdout=subprocess.PIPE)

cmd4 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/gbmv240_04v2.txt", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_04.ins", "-nsi", "10000", "-r", "0.99", "-I", "2500", "-pf", "0.01", "-k", "2", "-pi", "0.95"]
process = subprocess.Popen(cmd4, stdout=subprocess.PIPE)

cmd5 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/gbmv240_05v2.txt", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_05.ins", "-nsi", "10000", "-r", "0.99", "-I", "2500", "-pf", "0.01", "-k", "2", "-pi", "0.95"]
process = subprocess.Popen(cmd5, stdout=subprocess.PIPE)