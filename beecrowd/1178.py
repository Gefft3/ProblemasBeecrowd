n = float(input())
v = [n]

for i in range(1,100):
    v.append(v[i-1]/2)
for i in range(100):
    print(f"N[{i}] = {v[i]:.4f}")