a, g, d, r = 0,0,0,0

while r!=4:
    r = int(input())
    if r ==1:
        a+=1
        r = 0
    elif r==2:
        g+=1
        r = 0
    elif r==3:
        d+=1
        r = 0
print("MUITO OBRIGADO")
print(f"Alcool: {a}")
print(f"Gasolina: {g}")
print(f"Diesel: {d}")