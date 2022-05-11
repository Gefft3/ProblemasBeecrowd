n = int(input())
c = 0 
while c<n: 
    a = int(input())
    r = (a/(4*3.14))**(1/2)
    print(r)
    if r<=12:
        print(f"vermelho = R$ {(a*0.09):.2f}")
    elif r<=15:
        print(f"azul = R$ {(a*0.07):.2f}")
    else:
        print(f"amarelo = R$ {(a*0.05):.2f}")
    c+=1