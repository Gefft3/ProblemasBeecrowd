lista=""
while True:
    x,y = map(int, input().split())
    if x==0 or y == 0: break
    if x>0 and y>0:
        lista+="primeiro\n"
    elif x<0 and y>0:
        lista+="segundo\n"
    elif x<0 and y<0:
        lista+="terceiro\n"
    elif x>0 and y<0:
        lista+="quarto\n"
print(lista.rstrip())