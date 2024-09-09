entrada = input()

matrix = [[0 for i in range(12)] for j in range(12)]


for i in range(12):
    for j in range(12):
        if i < 11 - j and i > j:
            matrix[i][j] = float(input())
        else:
            n = float(input())
            matrix[i][j] = 0


soma = 0.0
for i in range(12):
    for j in range(12):
        if i < 11 - j and i > j:
            soma += matrix[i][j]

if entrada == 'S':
    print(f"{(soma):.1f}")
else:
    print(f"{(soma/30):.1f}")