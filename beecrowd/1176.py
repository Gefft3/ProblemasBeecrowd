v = []
antes = 0
atual = 0
prox = 1

n = int(input())

for i in range(61):
    v.append(atual)
    antes = atual
    atual = prox
    prox = atual+antes

for i in range(n):
    h = int(input())
    print(f"Fib({h}) = {v[h]}")
    