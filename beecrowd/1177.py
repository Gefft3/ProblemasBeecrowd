t = int(input())
v = []
for i in range(1000):
    for j in range(t):
        v.append(j)

for i in range(1000):
     print(f"N[{i}] = {v[i]}")