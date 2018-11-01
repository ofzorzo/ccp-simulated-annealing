import subprocess

#testa r
cmd = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.90", "-I", "2500", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/r090.txt"]
process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

cmd2 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.95", "-I", "2500", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/r095.txt"]
process = subprocess.Popen(cmd2, stdout=subprocess.PIPE)

cmd3 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/r099.txt"]
process = subprocess.Popen(cmd3, stdout=subprocess.PIPE)

#testa I
cmd5 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "50", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/I50.txt"]
process = subprocess.Popen(cmd5, stdout=subprocess.PIPE)

cmd6 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "250", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/I250.txt"]
process = subprocess.Popen(cmd6, stdout=subprocess.PIPE)

cmd7 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "500", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/I500.txt"]
process = subprocess.Popen(cmd7, stdout=subprocess.PIPE)

cmd8 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "1000", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/I1000.txt"]
process = subprocess.Popen(cmd8, stdout=subprocess.PIPE)

cmd9 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/I2500.txt"]
process = subprocess.Popen(cmd9, stdout=subprocess.PIPE)

#pi
cmd11 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-pi", "0.90", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pi090.txt"]
process = subprocess.Popen(cmd11, stdout=subprocess.PIPE)

cmd13 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-pi", "1.00", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pi100.txt"]
process = subprocess.Popen(cmd13, stdout=subprocess.PIPE)

cmd12 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-pi", "0.95", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pi095.txt"]
process = subprocess.Popen(cmd12, stdout=subprocess.PIPE)

cmd10 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pi085.txt"]
process = subprocess.Popen(cmd10, stdout=subprocess.PIPE)

#pf
cmd14 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.15", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pf015.txt"]
process = subprocess.Popen(cmd14, stdout=subprocess.PIPE)

cmd15 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.10", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pf010.txt"]
process = subprocess.Popen(cmd15, stdout=subprocess.PIPE)

cmd17 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.01", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pf001.txt"]
process = subprocess.Popen(cmd17, stdout=subprocess.PIPE)

cmd16 = ['python', "simulatedAnnealingNewRepresentation.py", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/gbmv240_01.ins", "-r", "0.99", "-I", "2500", "-pf", "0.05", "-pi", "0.85", "-out", "D:/UFRGS/Quinto Semestre/Otimização Combinatória/Trabalho final/Outputs/pf005.txt"]
process = subprocess.Popen(cmd16, stdout=subprocess.PIPE)