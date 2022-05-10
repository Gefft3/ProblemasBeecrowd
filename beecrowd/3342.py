n = int(input())
n = n*n
a, b = 0,0
for i in range(1,n+1):
    if i%2==0:
        b+=1
    else:
        a+=1
print(f"{a} casas brancas e {b} casas pretas")


