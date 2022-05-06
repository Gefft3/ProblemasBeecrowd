lista = ""
while True:
    n = int(input())
    if n == 0: break
    lista = lista+(' '.join(map(str, range(1, n + 1))))
    lista += "\n"
print(lista.rstrip('\n'))