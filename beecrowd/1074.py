n = int(input())
lista = ""
c = 0
while c<n:
    v = int(input())
    if v > 0:
        if v%2==0:
            lista+="EVEN POSITIVE\n"
        else:
            lista+="ODD POSITIVE\n"
    elif v < 0:
        if v%2==0:
            lista+="EVEN NEGATIVE\n"
        else:
            lista+="ODD NEGATIVE\n"
    else:
        lista+="NULL\n"
    c+=1
print(lista.rstrip()) 