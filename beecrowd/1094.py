n = int(input())
cont = 0
sapo = 0
coelho = 0
rato = 0

while(n>cont):
    scan = input().split()
    if scan[1] == "C":
        coelho += int(scan[0])
    if scan[1] == "S":
        sapo += int(scan[0])
    if scan[1] == "R":
        rato += int(scan[0])
    cont+=1
total = sapo+coelho+rato 
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {((coelho/total)*100):.2f} %")
print(f"Percentual de ratos: {((rato/total)*100):.2f} %")
print(f"Percentual de sapos: {((sapo/total)*100):.2f} %")