a, b, c, d = map(int, input().split())
inicioTotal = (a*60)+b
fimTotal = (c*60)+d
if fimTotal<=inicioTotal:
    total = fimTotal-inicioTotal+1440
else:
    total = fimTotal-inicioTotal
hr = total//60
min = total%60

print(f"O JOGO DUROU {hr} HORA(S) E {min} MINUTO(S)")