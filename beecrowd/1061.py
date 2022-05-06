scan = input().split()
diaI = int(scan[1]) 
scan = input().split()
hrI, minI, secI = int(scan[0]), int(scan[2]), int(scan[4])

scan = input().split()
diaF = int(scan[1]) 
scan = input().split()
hrF, minF, secF = int(scan[0]), int(scan[2]), int(scan[4])

iniT = (diaI*86400)+(hrI*3600)+(minI*60)+secI
fimT = (diaF*86400)+(hrF*3600)+(minF*60)+secF
t = fimT-iniT
diaT = t//86400
r = t%86400
hrT = r//3600
r = r%3600
minT = r//60
r = r%60
print(f"{diaT} dia(s)")
print(f"{hrT} hora(s)")
print(f"{minT} minuto(s)")
print(f"{r} segundo(s)")