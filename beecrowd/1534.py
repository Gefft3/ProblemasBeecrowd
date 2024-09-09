lista = []
while True:
    try:
        lista.append(int(input()))
    except EOFError:
        break

# lista = [4,7]

for N in lista:
    for i in range(0, N):
        for j in range(0, N):
            aux = N//2+1
            if i == N - j - 1 or   ((i == N - j - 1) and (i == aux and j == aux)):
                print(2, end="")
            elif i == j:
                print(1, end="")
            else:
                print(3, end="")
        
        print()