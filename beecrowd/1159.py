
while True:
    n = int(input())
    if n == 0: break
    s = 0
    c = 0
    if n%2==1:
        n=n+1
    while c<5:
        s+=n
        n+=2
        c+=1
    print(s)
