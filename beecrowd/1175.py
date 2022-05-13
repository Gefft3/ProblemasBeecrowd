n = []
for i in range(4):
    n.append(int(input()))
v = n[::-1]
for i in range(4):
    print(f"N[{i}] = {v[i]}")
