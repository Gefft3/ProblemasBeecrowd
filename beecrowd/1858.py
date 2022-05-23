n = int(input())
entrada = input().split()
posMenor = 0
for i in range(n):
    entrada[i] = int(entrada[i])
    if entrada[i] < entrada[posMenor]:
        posMenor = i
print(posMenor + 1)