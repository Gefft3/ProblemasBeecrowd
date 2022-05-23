test = 1
while True:
    x1,y1,x2,y2 = map(int, input().split())
    met = 0
    if x1==y1==x2==y2==0:break
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        if (x1<=x<=x2) and (y2<=y<=y1): 
            met+=1
    print("Teste {}".format(test))
    print("{}".format(met))
    test+=1