vP = []
vImp = []

for i in range(0, 15):
    n = int(input())
    if n % 2 == 0:
        if len(vP) <= 5:
            vP.append(n)
        else:
            for j in range(len(vP)):
                print(f"par[{j}] = {vP[j]}")
            vP = [n]
    else:
        if len(vImp) <= 5:
            vImp.append(n)
        else:
            for j in range(len(vImp)):
                print(f"impar[{j}] = {vImp[j]}")
            vImp = [n]

for i in range(len(vImp)):
    print(f"impar[{i}] = {vImp[i]}")

for i in range(len(vP)):
    print(f"par[{i}] = {vP[i]}")