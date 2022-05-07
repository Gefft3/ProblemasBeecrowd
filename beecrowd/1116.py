n = int(input())
c = 0
lista = ''
while True: 
    if c==n: break
    x,y=map(int, input().split())
    if y == 0:
        lista+="divisao impossivel\n"
    else:
        lista+=str(round((x/y),1))+'\n'
    c+=1
print(lista.rstrip())
