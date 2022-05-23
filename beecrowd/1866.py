n = int(input())
c = 0
while c<n:
    h = int(input())
    s = 0
    for i in range(1,h+1):
        if i%2==1:
            s+=1
        else:
            s-=1
    print(s)
    c+=1