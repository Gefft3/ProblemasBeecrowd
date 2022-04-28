n = float(input())
#notas
cem = n//100
r = round(n%100, 2)
cinq = r//50
r = round(r%50, 2)
vt = r//20
r = round(r%20, 2)
dez = r//10
r = round(r%10, 2)
cinc = r//5
r = round(r%5, 2)
dois = r//2
r = round(r%2, 2)
#moedas
m1 = r//1
r = round(r%1, 2)
m2 = r//0.5
r = round(r%0.5, 2)
m3 = r//0.25
r = round(r%0.25, 2)
m4 = r//0.1
r = round(r%0.1, 3)
m5 = r//0.05
r = round(r%0.05, 2)
m6 = r*100

print("NOTAS:")
print(f"{cem:.0f} nota(s) de R$ 100.00")
print(f"{cinq:.0f} nota(s) de R$ 50.00")
print(f"{vt:.0f} nota(s) de R$ 20.00")
print(f"{dez:.0f} nota(s) de R$ 10.00")
print(f"{cinc:.0f} nota(s) de R$ 5.00")
print(f"{dois:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{m1:.0f} moeda(s) de R$ 1.00")
print(f"{m2:.0f} moeda(s) de R$ 0.50")
print(f"{m3:.0f} moeda(s) de R$ 0.25")
print(f"{m4:.0f} moeda(s) de R$ 0.10")
print(f"{m5:.0f} moeda(s) de R$ 0.05")
print(f"{m6:.0f} moeda(s) de R$ 0.01")