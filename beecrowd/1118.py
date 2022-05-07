c = 0
r = 0
while True: 
    if c == 2: break
    n1 = float(input())
    while True:
        if n1<0 or n1>10:
            print("nota invalida")
            n1 = float(input())
        else:
            c+=1
            break
    n2 = float(input())
    while True:
        if n2<0 or n2>10:
            print("nota invalida")
            n2 = float(input())
        else:
            c+=1
            break

    print(f"media = {(n1+n2)/2:.2f}")

    while True:
        if r < 1 or r>2:
            r = int(input("novo calculo (1-sim 2-nao)\n"))
        if r==1: 
            c=0
            r = 0
            break
        elif r==2: break
