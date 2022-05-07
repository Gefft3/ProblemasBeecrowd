c = 0 
contPar = 0
contImpar = 0
contPos = 0
contNeg = 0

while(c<5):
    n = float(input())
    if n%2==0:
        contPar+=1
    if n%2==1:
        contImpar+=1
    if n>0:
        contPos+=1
    if n<0:
        contNeg+=1
    c+=1

print(f"{contPar} valor(es) par(es)")
print(f"{contImpar} valor(es) impar(es)")
print(f"{contPos} valor(es) positivo(s)")
print(f"{contNeg} valor(es) negativo(s)")
