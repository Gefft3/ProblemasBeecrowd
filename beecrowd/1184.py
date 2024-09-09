entrada = input()

matrix = [[0 for i in range(12)] for j in range(12)]


for i in range(12):
    for j in range(12):
        if j < i:
            matrix[i][j] = float(input())
        else:
            n = float(input())
            matrix[i][j] = 0



if entrada == 'S':
    soma = 0.0
    for i in range(12):
        for j in range(12):
            if j < i:
                soma += matrix[i][j]
    print(f"{(soma):.1f}")
else:
    media = 0.0
    for i in range(12):
        for j in range(3):
            if j < i:
                media += matrix[i][j]

    print(f"{(media/66):.1f}")