e, f ,c = map(int, input().split())
totalEmpty = e+f
totalSodas = 0


while totalEmpty >= c:
    totalSodas += 1
    totalEmpty = totalEmpty + 1 - c

print(totalSodas)
