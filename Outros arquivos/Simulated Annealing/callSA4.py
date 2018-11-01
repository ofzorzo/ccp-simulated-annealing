import subprocess

#pi
cmd11 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-pi", "0.90", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pi090v2.txt"]
process = subprocess.Popen(cmd11, stdout=subprocess.PIPE)

cmd13 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-pi", "1.00", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pi100v2.txt"]
process = subprocess.Popen(cmd13, stdout=subprocess.PIPE)

cmd12 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-pi", "0.95", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pi095v2.txt"]
process = subprocess.Popen(cmd12, stdout=subprocess.PIPE)