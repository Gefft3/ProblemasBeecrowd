a,b = map(int, input().split())
r = a%abs(b)
q = int((a-r)/b)
print(q,r)