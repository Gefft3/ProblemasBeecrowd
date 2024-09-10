def matrix(tamanho):
    m = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

    for linha in range(tamanho):
        for coluna in range(tamanho):
            if linha == coluna:
                m[linha][coluna] = 2
            elif linha == tamanho - coluna - 1:
                m[linha][coluna] = 3
            else:
                m[linha][coluna] = 0

    inicio = tamanho // 3
    fim = tamanho - inicio

    for linha in range(inicio, fim):
        for coluna in range(inicio, fim):
            m[linha][coluna] = 1

    m[tamanho // 2][tamanho // 2] = 4

    for linha in m:
        print("".join(map(str, linha)))
    print()

def main():
    try:
        while True:
            tamanho = int(input())
            matrix(tamanho)
    except EOFError:
        pass

if __name__ == "__main__":
    main()
