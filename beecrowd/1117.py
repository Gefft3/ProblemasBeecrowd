lista = ""
c = 0
while True: 
    if c == 2: break
    n1 = float(input())
    while True:
        if n1<0 or n1>10:
            lista+="nota invalida\n"
            n1 = float(input())
        else:
            c+=1
            break
    n2 = float(input())
    while True:
        if n2<0 or n2>10:
            lista+="nota invalida\n"
            n2 = float(input())
        else:
            c+=1
            break
media = round((n1+n2)/2,2)
lista+="media = "+str(media)
print(lista.rstrip())
    
