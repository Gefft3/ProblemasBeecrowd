v = int(input())
c = 0
lista = ""
while c<v:
    n = input()
    if n=="P=NP":
        lista+="skipped\n"
        c+=1
    else:
        p1,p2 = map(int, n.split("+"))
        lista+= str(p1+p2)+'\n'
        c+=1
print(lista.rstrip())