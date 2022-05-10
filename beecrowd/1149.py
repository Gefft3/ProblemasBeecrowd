scan = input().split()
a = int(scan[0])
n = 0
for i in range(1, len(scan)):
    if int(scan[i]) > n:
        n = int(scan[i])
soma = 0
for i in range(0, n):
    soma += a+i
print(soma)