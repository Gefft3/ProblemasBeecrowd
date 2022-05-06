soma = 0 
lista = ""
lista2 = ""
while True: 
    m, n = map(int, input().split())
    if m <= 0 or n <= 0: break
    if m<=n:
        a = m
        b = n
    else:
        a = n
        b = m
    for i in range(a,b+1):
        lista += str(i)
        soma += i
    lista = " ".join(lista)+" Sum="+str(soma)
    lista2 += lista+"\n"
    lista = ""
    soma = 0
print(lista2.rstrip())