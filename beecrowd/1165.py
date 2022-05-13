n = int(input())

for h in range(n):
    i = int(input())
    c1 = 0
    for j in range(1,i):
        if i%j==0:
            c1+=1
    if c1 == 1:
        print(f"{i} eh primo")
    else:
        print(f"{i} nao eh primo")