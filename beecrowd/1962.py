n = int(input())

for i in range(n):
    t = int(input())

    ano = 2015 - t
    if ano <= 0:
        ano = ano-1
    
    print(abs(ano), end = " ")

    if ano < 0:
        print("A.C")
    else:
        print("D.C")