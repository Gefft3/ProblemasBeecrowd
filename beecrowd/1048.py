s = float(input())
r = 0
if s<=400:
    r = s*0.15
    print(f"Novo salario: {s+r:.2f}") 
    print(f"Reajuste ganho: {r:.2f}") 
    print("Em percentual: 15 %")
elif s>400 and s<=800:
    r = s*0.12
    print(f"Novo salario: {s+r:.2f}") 
    print(f"Reajuste ganho: {r:.2f}") 
    print("Em percentual: 12 %")
elif s>800 and s<=1200:
    r = s*0.1
    print(f"Novo salario: {s+r:.2f}") 
    print(f"Reajuste ganho: {r:.2f}") 
    print("Em percentual: 10 %")
elif s>1200 and s<=2000:
    r = s*0.07
    print(f"Novo salario: {s+r:.2f}") 
    print(f"Reajuste ganho: {r:.2f}") 
    print("Em percentual: 7 %")
elif s>2000:
    r = s*0.04
    print(f"Novo salario: {s+r:.2f}") 
    print(f"Reajuste ganho: {r:.2f}") 
    print("Em percentual: 4 %")