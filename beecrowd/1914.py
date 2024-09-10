n = int(input())

for i in range(n):
    nome1, escolha1, nome2, escolha2 = input().split()
    resultado1, resultado2 = map(int, input().split())

    if (resultado1 + resultado2) % 2 == 0:
        if escolha1 == 'PAR':
            print(nome1)
        else:
            print(nome2)
    else:
        if escolha1 == 'IMPAR':
            print(nome1)
        else:
            print(nome2)