n = int(input())
c = 0
while c<n:
    x, y = map(int, input().split())
    s = 0
    c1 = 0
    if x%2==0:
        x = x+1    
    while c1<y:
        s += x
        x+=2
        c1+=1
    c+=1
    print(s)       