n = int(input())
tent = 0 
soma = 0
lista = ""
while(n!=tent):
    num = int(input())
    for i in range(1, num):
        if (num%i) == 0 and num!=i:
            soma += i
    if soma == num:
        lista += str(num)+" eh perfeito\n"
        soma = 0
    else:
        lista += str(num)+" nao eh perfeito\n"
        soma = 0
    tent+=1

print(lista.rstrip("\n"))   