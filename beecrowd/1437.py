pontos = ["N", "L", "S","O"]
while True:
    posicao = 0
    n = int(input())
    if n == 0:break
    ent = input()
    ent = list(ent)
    for i in range(n):
        if ent[i]=='D':
            posicao+=1
        elif ent[i]=="E":
            posicao-=1
    posicao = posicao%4
    print(pontos[posicao])