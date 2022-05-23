test = 1
while True:
    operatores = []
    n = int(input())
    if n == 0: break
    entrada = input()
    numeros = entrada.replace('-',' ').replace('+',' ').split()
    for i in range(len(numeros)):
        numeros[i] = int(numeros[i])
    soma = numeros[0]
    for i in range(len(entrada)):
        if entrada[i]=="+" or entrada[i]=="-":
            operatores.append(entrada[i])
    for i in range(len(operatores)):
        if operatores[i]=='+':
            soma += numeros[i+1]
        else:
            soma -= numeros[i+1]
    print("Teste {}".format(test))
    print(soma)
    print()
    test+=1