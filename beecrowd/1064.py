n = 0
count = 0
soma = 0 
while(n<6):
    num = float(input())
    if num > 0:
        count += 1
        soma += num
    n+=1
media = soma/count
print(f"{count} valores positivos")
print(f"{media:.1f}")
