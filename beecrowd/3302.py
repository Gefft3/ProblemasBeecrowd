n = int(input())
lista = ''
c=0
while c<n:
    r = int(input()) 
    c+=1
    lista+="resposta "+str(c)+": "+str(r)+" \n"

print(lista.rstrip())