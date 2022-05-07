m = 0
p = 0
c = 1

while True:
    if c==101:break
    n = int(input())
    if c==1:
        m = n
    if n>m:
        m=n
        p = c 
    c+=1

print(m)
print(p)