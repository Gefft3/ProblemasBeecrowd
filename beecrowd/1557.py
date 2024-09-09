while True:
    tamanho = int(input())

    if tamanho == 0:
        break

    matriz = [[0] * tamanho for _ in range(tamanho)]

    elemento = 1

    for linha in range(tamanho):
        for coluna in range(tamanho):
            matriz[linha][coluna] = elemento
            elemento *= 2

        elemento = (matriz[linha][0]) * 2

    t = matriz[tamanho - 1][tamanho - 1]

    digitos = len(str(t))

    for linha in range(tamanho):
        for coluna in range(tamanho):
            if coluna == 0:
                print(f"{matriz[linha][coluna]:{digitos}}", end="")
            else:
                print(f" {matriz[linha][coluna]:{digitos}}", end="")
        print()

    print()
