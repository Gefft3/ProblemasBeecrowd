c = 0 
cont = 0
while(c<5):
    n = float(input())
    if n%2==0:
        cont=cont+1
    c+=1
print(f"{cont} valores pares")