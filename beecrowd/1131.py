vInt = 0
vGre = 0
emp = 0
r = 0
c = 0
while True:
    if r == 2: 
        print(f"{c} grenais")
        print(f"Inter:{vInt}")
        print(f"Gremio:{vGre}")
        print(f"Empates:{emp}")
        if vInt>vGre:
            print("Inter venceu mais")
        elif vGre>vInt:
            print("Gremio venceu mais")
        break
    i,g = map(int, input().split())

    if i > g:
        vInt+=1
        c+=1
    elif g > i:
        vGre+=1
        c +=1
    else:
        emp+=1
        c+=1
    r = int(input("Novo grenal (1-sim 2-nao)\n"))