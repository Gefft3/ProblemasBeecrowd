x,y=map(int, input().split())
c=0
for i in range(1,y+1):
        if c == x-1:
            print(str(i),end="\n")
            c=0
        else:
            print(str(i),end=" ")
            c+=1